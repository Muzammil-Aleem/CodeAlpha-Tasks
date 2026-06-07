import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading
import pyperclip
import pyttsx3

API_URL = "https://api.mymemory.translated.net/get"

LANGUAGES = {
    "Auto Detect":          "auto",
    "Afrikaans":            "af",
    "Albanian":             "sq",
    "Arabic":               "ar",
    "Bengali":              "bn",
    "Bulgarian":            "bg",
    "Chinese (Simplified)": "zh",
    "Chinese (Traditional)":"zh-TW",
    "Croatian":             "hr",
    "Czech":                "cs",
    "Danish":               "da",
    "Dutch":                "nl",
    "English":              "en",
    "Estonian":             "et",
    "Finnish":              "fi",
    "French":               "fr",
    "German":               "de",
    "Greek":                "el",
    "Gujarati":             "gu",
    "Hebrew":               "iw",
    "Hindi":                "hi",
    "Hungarian":            "hu",
    "Indonesian":           "id",
    "Italian":              "it",
    "Japanese":             "ja",
    "Korean":               "ko",
    "Latvian":              "lv",
    "Lithuanian":           "lt",
    "Malay":                "ms",
    "Marathi":              "mr",
    "Norwegian":            "no",
    "Persian":              "fa",
    "Polish":               "pl",
    "Portuguese":           "pt",
    "Punjabi":              "pa",
    "Romanian":             "ro",
    "Russian":              "ru",
    "Serbian":              "sr",
    "Slovak":               "sk",
    "Slovenian":            "sl",
    "Spanish":              "es",
    "Swahili":              "sw",
    "Swedish":              "sv",
    "Tamil":                "ta",
    "Telugu":               "te",
    "Thai":                 "th",
    "Turkish":              "tr",
    "Ukrainian":            "uk",
    "Urdu":                 "ur",
    "Vietnamese":           "vi",
    "Welsh":                "cy",
}
LANG_NAMES = list(LANGUAGES.keys())

BG        = "#0D0F14"
CARD      = "#151820"
ACCENT    = "#00E5FF"
ACCENT2   = "#FF4081"
TEXT_PRI  = "#F0F4FF"
TEXT_SEC  = "#7B8299"
BORDER    = "#1E2230"
BTN_HOVER = "#1a2030"

F_HEAD  = ("Georgia",    24, "bold")
F_SUB   = ("Georgia",    10, "italic")
F_LABEL = ("Consolas",    8, "bold")
F_TEXT  = ("Segoe UI",   12)
F_BTN   = ("Consolas",   10, "bold")
F_SMALL = ("Consolas",    8)

PLACEHOLDER = "Type or paste text here…"


def translate_text(text, src, tgt):
    params = {"q": text, "langpair": f"{src}|{tgt}"}
    r = requests.get(API_URL, params=params, timeout=12)
    r.raise_for_status()
    d = r.json()
    if d.get("responseStatus") == 200:
        return d["responseData"]["translatedText"], None
    return None, d.get("responseDetails", "Translation failed.")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LinguaX  ·  AI Language Translator")
        self.configure(bg=BG)
        self.geometry("1100x700")
        self.minsize(860, 600)

        self._tts     = None
        self._tts_lk  = threading.Lock()
        self._after_id = None        

        self._setup_styles()
        self._build()
        self._anim_start()

    def _setup_styles(self):
        s = ttk.Style(self)
        s.theme_use("clam")
        s.configure("Dark.TCombobox",
                     fieldbackground=CARD, background=CARD,
                     foreground=TEXT_PRI, selectforeground=TEXT_PRI,
                     selectbackground="#1E2230", bordercolor=BORDER,
                     arrowcolor=ACCENT, lightcolor=CARD, darkcolor=CARD)
        s.map("Dark.TCombobox",
              fieldbackground=[("readonly", CARD)],
              background=[("readonly", CARD)],
              foreground=[("readonly", TEXT_PRI)])
        s.configure("Cyan.Horizontal.TProgressbar",
                     troughcolor=CARD, background=ACCENT,
                     bordercolor=BORDER, lightcolor=ACCENT, darkcolor=ACCENT)

    def _build(self):
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)

        hdr = tk.Frame(self, bg=BG)
        hdr.grid(row=0, column=0, sticky="ew", padx=32, pady=(22, 0))

        self._lbl_lingua = tk.Label(hdr, text="LINGUA", font=F_HEAD, bg=BG, fg=ACCENT)
        self._lbl_lingua.pack(side="left")
        tk.Label(hdr, text="X",  font=F_HEAD, bg=BG, fg=ACCENT2).pack(side="left")
        tk.Label(hdr, text="  · Universal Language Translator",
                 font=F_SUB, bg=BG, fg=TEXT_SEC).pack(side="left", pady=(6, 0))
        tk.Label(hdr, text="MyMemory API & No Key Needed",
                 font=F_LABEL, bg=BG, fg=TEXT_SEC).pack(side="right", pady=(8, 0))

        tk.Frame(self, bg=ACCENT, height=1).grid(
            row=0, column=0, sticky="ews", padx=32, pady=(0, 0))

        lang = tk.Frame(self, bg=BG)
        lang.grid(row=1, column=0, sticky="ew", padx=32, pady=(14, 6))
        lang.columnconfigure(0, weight=1)
        lang.columnconfigure(2, weight=1)

        src_f = tk.Frame(lang, bg=BG)
        src_f.grid(row=0, column=0, sticky="ew")
        tk.Label(src_f, text="SOURCE LANGUAGE", font=F_LABEL,
                 bg=BG, fg=TEXT_SEC).pack(anchor="w")
        self.src_var = tk.StringVar(value="English")
        ttk.Combobox(src_f, textvariable=self.src_var, values=LANG_NAMES,
                     state="readonly", style="Dark.TCombobox",
                     font=F_TEXT).pack(fill="x", pady=(4, 0))

        swap_f = tk.Frame(lang, bg=BG)
        swap_f.grid(row=0, column=1, padx=18, pady=(16, 0))
        self._swap_btn = tk.Button(swap_f, text="⇄", font=("Segoe UI", 17),
                                   bg=CARD, fg=ACCENT, bd=0, relief="flat",
                                   padx=12, pady=5, cursor="hand2",
                                   activebackground=BTN_HOVER, activeforeground=ACCENT2,
                                   command=self._swap)
        self._swap_btn.pack()
        self._hover(self._swap_btn, ACCENT2, ACCENT)

        tgt_f = tk.Frame(lang, bg=BG)
        tgt_f.grid(row=0, column=2, sticky="ew")
        tk.Label(tgt_f, text="TARGET LANGUAGE", font=F_LABEL,
                 bg=BG, fg=TEXT_SEC).pack(anchor="w")
        self.tgt_var = tk.StringVar(value="French")
        ttk.Combobox(tgt_f, textvariable=self.tgt_var, values=LANG_NAMES,
                     state="readonly", style="Dark.TCombobox",
                     font=F_TEXT).pack(fill="x", pady=(4, 0))

        btn_f = tk.Frame(self, bg=BG)
        btn_f.grid(row=3, column=0, sticky="ew", padx=32, pady=(6, 0))

        btn_specs = [
            ("⚡  TRANSLATE",    self._do_translate,    ACCENT,  BG,       BTN_HOVER),
            ("⎘  COPY",          self._copy,            CARD,    ACCENT,   BTN_HOVER),
            ("🔊  SPEAK INPUT",   self._speak_input,     CARD,    TEXT_PRI, BTN_HOVER),
            ("🔊  SPEAK OUTPUT",  self._speak_output,    CARD,    "#00E5FF",BTN_HOVER),
            ("✕  CLEAR",         self._clear,           CARD,    ACCENT2,  BTN_HOVER),
        ]
        for label, cmd, bg_, fg_, abg in btn_specs:
            b = tk.Button(btn_f, text=label, font=F_BTN, bg=bg_, fg=fg_,
                          bd=0, relief="flat", padx=16, pady=10,
                          cursor="hand2", command=cmd,
                          activebackground=abg, activeforeground=fg_)
            b.pack(side="left", padx=(0, 8))

        stat_f = tk.Frame(self, bg=BG)
        stat_f.grid(row=4, column=0, sticky="ew", padx=32, pady=(4, 0))

        self._status_var = tk.StringVar(value="Ready  —  type text and press Translate (or wait for auto-translate)")
        self._count_var  = tk.StringVar(value="0 chars · 0 words")

        tk.Label(stat_f, textvariable=self._status_var, font=F_SMALL,
                 bg=BG, fg=TEXT_SEC, anchor="w").pack(side="left")
        tk.Label(stat_f, textvariable=self._count_var, font=F_SMALL,
                 bg=BG, fg=TEXT_SEC, anchor="e").pack(side="right")

        self._prog = ttk.Progressbar(self, mode="indeterminate",
                                     style="Cyan.Horizontal.TProgressbar")

        tk.Frame(self, bg=BG, height=12).grid(row=5, column=0)

        panels = tk.Frame(self, bg=BG)
        panels.grid(row=2, column=0, sticky="nsew", padx=32, pady=(0, 6))
        panels.columnconfigure(0, weight=1)
        panels.columnconfigure(1, weight=1)
        panels.rowconfigure(1, weight=1)

        tk.Label(panels, text="INPUT TEXT", font=F_LABEL,
                 bg=BG, fg=TEXT_SEC).grid(row=0, column=0, sticky="w", padx=(0, 6))
        tk.Label(panels, text="TRANSLATION", font=F_LABEL,
                 bg=BG, fg=TEXT_SEC).grid(row=0, column=1, sticky="w", padx=(6, 0))

        in_card = tk.Frame(panels, bg=CARD, highlightthickness=1,
                           highlightbackground=BORDER)
        in_card.grid(row=1, column=0, sticky="nsew", padx=(0, 6), pady=(4, 0))
        self.inp = tk.Text(in_card, font=F_TEXT, bg=CARD, fg=TEXT_SEC,
                           insertbackground=ACCENT, relief="flat", bd=0,
                           wrap="word", padx=14, pady=12,
                           selectbackground=ACCENT, selectforeground=BG)
        self.inp.pack(fill="both", expand=True)
        self.inp.insert("1.0", PLACEHOLDER)
        self.inp.bind("<FocusIn>",   self._ph_in)
        self.inp.bind("<FocusOut>",  self._ph_out)
        self.inp.bind("<KeyRelease>", self._on_key)

        out_card = tk.Frame(panels, bg=CARD, highlightthickness=1,
                            highlightbackground=BORDER)
        out_card.grid(row=1, column=1, sticky="nsew", padx=(6, 0), pady=(4, 0))
        self.out = tk.Text(out_card, font=F_TEXT, bg=CARD, fg=ACCENT,
                           relief="flat", bd=0, wrap="word",
                           padx=14, pady=12, state="disabled",
                           selectbackground=ACCENT2, selectforeground=BG)
        self.out.pack(fill="both", expand=True)

    def _ph_in(self, _=None):
        if self.inp.get("1.0", "end-1c") == PLACEHOLDER:
            self.inp.delete("1.0", "end")
            self.inp.config(fg=TEXT_PRI)

    def _ph_out(self, _=None):
        if not self.inp.get("1.0", "end-1c").strip():
            self.inp.insert("1.0", PLACEHOLDER)
            self.inp.config(fg=TEXT_SEC)

    def _get_input(self):
        t = self.inp.get("1.0", "end-1c").strip()
        return "" if t == PLACEHOLDER else t

    def _on_key(self, _=None):
        txt = self._get_input()
        words = len(txt.split()) if txt else 0
        self._count_var.set(f"{len(txt)} chars · {words} words")

        if self._after_id:
            self.after_cancel(self._after_id)
        if txt:
            self._after_id = self.after(1200, self._do_translate)
        else:
            self._after_id = None
            self._set_out("")

    def _swap(self):
        s, t = self.src_var.get(), self.tgt_var.get()
        if s != "Auto Detect":
            self.src_var.set(t)
            self.tgt_var.set(s)

    def _do_translate(self):
        text = self._get_input()
        if not text:
            messagebox.showwarning("Empty", "Please enter text to translate.")
            return

        src_code = LANGUAGES.get(self.src_var.get(), "en")
        tgt_code = LANGUAGES.get(self.tgt_var.get(), "fr")
        if src_code == "auto":
            src_code = "en"
        if src_code == tgt_code:
            messagebox.showinfo("Same language", "Source and target are the same.")
            return

        self._status_var.set("⏳  Translating…")
        self._prog.grid(row=6, column=0, sticky="ew", padx=32, pady=(2, 6))
        self._prog.start(8)
        self._set_out("")

        def worker():
            try:
                res, err = translate_text(text, src_code, tgt_code)
                self.after(0, lambda: self._done(res, err))
            except Exception as ex:
                self.after(0, lambda: self._done(None, str(ex)))

        threading.Thread(target=worker, daemon=True).start()

    def _done(self, result, err):
        self._prog.stop()
        self._prog.grid_remove()
        if err or result is None:
            self._status_var.set(f"✗  {err}")
            messagebox.showerror("Error", str(err))
        else:
            self._set_out(result)
            self._status_var.set(
                f"✓  {self.src_var.get()}  →  {self.tgt_var.get()}")

    def _set_out(self, text):
        self.out.config(state="normal")
        self.out.delete("1.0", "end")
        if text:
            self.out.insert("1.0", text)
        self.out.config(state="disabled")

    def _copy(self):
        t = self.out.get("1.0", "end-1c").strip()
        if not t:
            messagebox.showinfo("Nothing to copy", "Translate something first.")
            return
        try:
            pyperclip.copy(t)
            prev = self._status_var.get()
            self._status_var.set("✓  Copied to clipboard!")
            self.after(2000, lambda: self._status_var.set(prev))
        except Exception as e:
            messagebox.showerror("Copy failed", str(e))

    def _tts_engine(self):
        if self._tts is None:
            try:
                self._tts = pyttsx3.init()
            except Exception:
                pass
        return self._tts

    def _speak(self, text):
        if not text:
            return
        def run():
            with self._tts_lk:
                e = self._tts_engine()
                if e:
                    try:
                        e.say(text)
                        e.runAndWait()
                    except Exception:
                        pass
        threading.Thread(target=run, daemon=True).start()

    def _speak_input(self):
        self._speak(self._get_input())

    def _speak_output(self):
        self._speak(self.out.get("1.0", "end-1c").strip())

    def _clear(self):
        self.inp.delete("1.0", "end")
        self.inp.insert("1.0", PLACEHOLDER)
        self.inp.config(fg=TEXT_SEC)
        self._set_out("")
        self._count_var.set("0 chars · 0 words")
        self._status_var.set("Ready  —  type text and press Translate (or wait for auto-translate)")
        if self._after_id:
            self.after_cancel(self._after_id)
            self._after_id = None

    def _hover(self, w, on, off):
        w.bind("<Enter>", lambda e: w.config(fg=on))
        w.bind("<Leave>", lambda e: w.config(fg=off))

    def _anim_start(self):
        cols = [ACCENT, "#00BFFF", "#4FC3F7", ACCENT2, "#FF80AB", ACCENT]
        self._ai = 0
        def step():
            self._lbl_lingua.config(fg=cols[self._ai % len(cols)])
            self._ai += 1
            self.after(700, step)
        step()


if __name__ == "__main__":
    App().mainloop()
# 🌐 LinguaX — Universal Language Translator

A sleek, dark-themed desktop translator built with **Python + Tkinter**.  
Uses the **MyMemory API** — completely **free**, no API key, no sign-up.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🌍 50+ Languages | Arabic, Urdu, Hindi, French, Japanese, Korean & more |
| ⚡ Fast Translation | Background threads — UI never freezes |
| 🔊 Text-to-Speech | Speak both source and translated text |
| ⎘ One-Click Copy | Copy translation to clipboard instantly |
| ⇄ Swap Languages | Instantly flip source ↔ target |
| 📊 Word Counter | Live character + word count |
| 🎨 Beautiful UI | Animated header, dark glass aesthetic |

---

## 🛠 Requirements

- **Python 3.8+** — [Download here](https://python.org/downloads)
- Internet connection (for translation API)
- Windows 10/11 recommended (works on Linux/Mac too)

---

## 🚀 How to Run (Windows — Easiest)

### Option A: Double-click launcher
1. Download / unzip the project folder
2. Double-click **`run_windows.bat`**
3. App launches automatically ✅

### Option B: Manual (any OS)
```bash
# 1. Open terminal in the project folder
# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

### Option C: Linux / Mac
```bash
chmod +x run.sh
./run.sh
```

---

## 📦 Dependencies

| Package | Purpose | Cost |
|---|---|---|
| `requests` | HTTP calls to translation API | Free |
| `pyttsx3` | Text-to-speech engine | Free |
| `pyperclip` | Clipboard copy/paste | Free |
| `tkinter` | GUI (built into Python) | Free |

All installed automatically via `requirements.txt`.

---

## 🌐 Translation API

**MyMemory** — `https://api.mymemory.translated.net`

- ✅ **Free** — no API key needed
- ✅ **50 languages** supported
- ✅ 10,000 words/day free tier
- ✅ No sign-up required

---

## 🖥 How to Use

1. **Type** your text in the left panel
2. **Choose** source language (or keep "English")
3. **Choose** target language
4. Click **⚡ TRANSLATE** (or it translates after typing)
5. Use **⎘ COPY** to copy the translation
6. Use **🔊 SPEAK** buttons for text-to-speech
7. Use **⇄** to swap languages
8. Use **✕ CLEAR** to reset everything

---

## 🗂 Project Structure

```
translator/
├── app.py              ← Main application
├── requirements.txt    ← Python dependencies
├── run_windows.bat     ← Windows launcher
├── run.sh              ← Linux/Mac launcher
└── README.md           ← This file
```

---

## ❓ Troubleshooting

**"ModuleNotFoundError"** → Run `pip install -r requirements.txt`

**"No module named tkinter"** (Linux) → Run `sudo apt install python3-tk`

**Clipboard not working** (Linux) → Run `sudo apt install xclip`

**TTS not working** → pyttsx3 needs system TTS: on Windows it uses SAPI5 (built-in)

---

Made with ❤️ using Python & MyMemory API

import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from faqs import FAQS
from flask import Flask, request, jsonify, send_from_directory, Response
import os

# ── Stopwords (pure Python — no NLTK needed) ─────────────────────────────────
_STOPWORDS = {
    "a","an","the","is","it","in","on","at","to","for","of","and","or","but",
    "not","are","was","were","be","been","being","have","has","had","do","does",
    "did","will","would","could","should","may","might","this","that","these",
    "those","i","you","he","she","we","they","me","him","her","us","them",
    "my","your","his","its","our","their","what","which","who","how","when",
    "where","why","with","from","by","as","if","so","up","out","about","into",
    "can","get","just","also","like","use","used","using",
}

def _preprocess(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    tokens = [t for t in text.split() if t not in _STOPWORDS and len(t) > 1]
    return " ".join(tokens)

# ── Build TF-IDF index ────────────────────────────────────────────────────────
_questions_raw   = [f["q"] for f in FAQS]
_questions_clean = [_preprocess(q) for q in _questions_raw]

_vectorizer   = TfidfVectorizer()
_tfidf_matrix = _vectorizer.fit_transform(_questions_clean)

THRESHOLD = 0.12

def get_answer(user_q: str) -> dict:
    clean = _preprocess(user_q)
    if not clean:
        return {"found": False, "answer": "Please type a question!", "confidence": 0, "matched_question": ""}
    vec   = _vectorizer.transform([clean])
    sims  = cosine_similarity(vec, _tfidf_matrix).flatten()
    idx   = int(sims.argmax())
    score = float(sims[idx])
    if score < THRESHOLD:
        return {
            "found": False,
            "answer": "I'm sorry, I don't have an answer for that. Try rephrasing your question!",
            "confidence": round(score, 4),
            "matched_question": ""
        }
    return {
        "found": True,
        "answer": FAQS[idx]["a"],
        "confidence": round(score, 4),
        "matched_question": _questions_raw[idx]
    }

# ── Flask app ─────────────────────────────────────────────────────────────────
app = Flask(__name__, static_folder=".")

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(force=True, silent=True) or {}
    q = data.get("question", "").strip()
    if not q:
        return jsonify({"error": "No question provided."}), 400
    return jsonify(get_answer(q))

@app.route("/faqs")
def faqs():
    """Return all FAQ questions for the suggestion chips."""
    return jsonify([{"question": f["q"]} for f in FAQS])

if __name__ == "__main__":
    import threading, webbrowser, time
    PORT = 5000
    url  = f"http://127.0.0.1:{PORT}"

    def _open_browser():
        time.sleep(1.2)
        webbrowser.open(url)

    threading.Thread(target=_open_browser, daemon=True).start()

    print(f"\n{'='*52}")
    print(f"  FAQ Chatbot starting …")
    print(f"  Opening browser at {url}")
    print(f"  Press CTRL+C to stop")
    print(f"{'='*52}\n")

    app.run(port=PORT, debug=False)

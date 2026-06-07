# 🤖 FAQ Chatbot — Python & Tech Q&A

A lightweight, offline-capable FAQ chatbot built with **Flask** and **TF-IDF + Cosine Similarity**. Ask anything about Python, programming, or general tech — no external AI API required, no internet connection needed after setup.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0%2B-black?style=flat-square&logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4%2B-orange?style=flat-square&logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## ✨ Features

- **NLP-powered matching** — TF-IDF vectorisation + cosine similarity finds the best answer even for loosely worded questions
- **218 curated FAQs** — covers Python core, data science, web dev, Git, databases, networking, algorithms, and more
- **Zero external API calls** — runs entirely on your machine; no OpenAI key, no internet needed
- **Confidence score** — every answer shows a match percentage and the question it was matched to
- **Suggestion chips** — clickable sample questions to get started instantly
- **Clean dark UI** — responsive chat interface that works on desktop and mobile
- **Auto-opens browser** — just run one command and the app launches

---

## 📸 Preview
<img width="1197" height="881" alt="image" src="https://github.com/user-attachments/assets/18a70b88-a429-4861-9851-eb559db4a6ed" />

---

## 🗂️ Project Structure

```
faq-chatbot/
│
├── app.py            # Flask server + TF-IDF NLP logic + routes
├── faqs.py           # 218 FAQ entries (question + answer pairs)
├── index.html        # Chat UI (served by Flask)
└── requirements.txt  # Python dependencies
```

---

## ⚙️ How It Works

```
User question
     │
     ▼
Preprocessing  ──►  lowercase, strip punctuation, remove stopwords
     │
     ▼
TF-IDF Vector  ──►  transform question into a numeric vector
     │
     ▼
Cosine Similarity ──►  compare against all 218 FAQ vectors
     │
     ▼
Best Match  ──►  return answer if confidence ≥ 12%, else "not found"
```

**Why TF-IDF + Cosine Similarity?**

- No GPU, no heavy model download, no API key
- Instant startup — the index builds in milliseconds
- Still handles paraphrased and incomplete questions well
- Perfect for a focused, domain-specific FAQ dataset

---

## 🚀 Quick Start

### 1 — Clone the repository

```bash
git clone https://github.com/your-username/faq-chatbot.git
cd faq-chatbot
```

### 2 — (Recommended) Create a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### 4 — Run the chatbot

```bash
python app.py
```

The browser opens automatically at **http://127.0.0.1:5000**. Press `CTRL+C` to stop the server.

---

## 📦 Dependencies

| Package | Version | Purpose |
|---|---|---|
| `flask` | ≥ 3.0 | Web server & REST API |
| `scikit-learn` | ≥ 1.4 | TF-IDF vectoriser & cosine similarity |

> **No NLTK required.** Preprocessing is handled with pure Python (regex + a custom stopword list), so there are no data downloads or `nltk_data` folders needed.

---

## 🌐 API Reference

The Flask server exposes two endpoints:

### `GET /`
Serves the chat UI (`index.html`).

### `POST /ask`
Accepts a JSON body and returns the best matching answer.

**Request**
```json
{ "question": "What is a virtual environment?" }
```

**Response (match found)**
```json
{
  "found": true,
  "answer": "A virtual environment is an isolated Python installation…",
  "confidence": 0.8731,
  "matched_question": "What is a virtual environment?"
}
```

**Response (no match)**
```json
{
  "found": false,
  "answer": "I'm sorry, I don't have an answer for that. Try rephrasing your question!",
  "confidence": 0.04,
  "matched_question": ""
}
```

### `GET /faqs`
Returns all FAQ questions (used to populate suggestion chips in the UI).

**Response**
```json
[
  { "question": "What is Python?" },
  { "question": "What is pip?" },
  ...
]
```

---

## 📚 FAQ Categories

The 218 questions in `faqs.py` span:

- **Python Core** — syntax, data types, OOP, decorators, generators, comprehensions
- **Standard Library** — `os`, `sys`, `re`, `json`, `datetime`, `collections`, `itertools`
- **Web Development** — Flask, REST APIs, HTTP, JSON, authentication
- **Data Science** — NumPy, pandas, scikit-learn, matplotlib, machine learning concepts
- **Databases** — SQL, SQLite, ORMs, indexing, transactions
- **Computer Science** — algorithms, data structures, Big-O, recursion, sorting
- **DevOps & Tools** — Git, virtual environments, pip, Docker basics, CLI
- **Networking & Security** — HTTP/HTTPS, APIs, SSL, hashing, encryption basics
- **General CS Concepts** — OOP, functional programming, concurrency, memory management

---

## 🛠️ Customisation

### Add your own FAQs

Open `faqs.py` and add entries to the `FAQS` list:

```python
{"q": "Your question here?",
 "a": "Your detailed answer here."},
```

The TF-IDF index rebuilds automatically on the next server start — no other changes needed.

### Adjust the confidence threshold

In `app.py`, change `THRESHOLD` (default `0.12`) to tune sensitivity:

```python
THRESHOLD = 0.12   # lower = more permissive, higher = stricter
```

### Change the port

```python
PORT = 5000   # change to any available port
```

---

## 🤝 Contributing

Contributions are welcome! To add FAQs, fix bugs, or improve the UI:

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add: your change"`
4. Push and open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — free to use, modify, and distribute.

---

## 👤 Author

**Muzammil Aleem**  
Feel free to connect or open an issue if you run into any problems.

# 🕷️ NLP Web Scraper

A Python Flask app that crawls websites, extracts metadata, performs sentiment analysis, and exposes a REST API and HTML interface.

---

## 🧰 Features

- Web scraping using `requests` + `BeautifulSoup`
- Sentiment analysis with `TextBlob`
- Named Entity Recognition (NER) using `spaCy`
- REST API with Swagger UI
- Data persistence in PostgreSQL
- Simple HTML form for interactive testing

---

## 🖥️ Tech Stack

- Python
- Flask
- SQLAlchemy
- PostgreSQL (via Docker)
- BeautifulSoup
- spaCy + TextBlob

---

## ⚙️ Setup Instructions (Windows/Linux/macOS)

### 🐳 Step 1: Start PostgreSQL via Docker

> Make sure Docker Desktop is installed and running.

```bash
docker compose up -d
```

This will:

- Start a PostgreSQL 13 container
- Create a database named `nlp_scraper`
- Expose port 5432

You can edit `docker-compose.yml` if needed.

---

### 🐍 Step 2: Set up the Python Environment

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# or
source venv/bin/activate     # Linux/macOS

# Install required packages
pip install -r requirements.txt

# Download additional corpora
python -m textblob.download_corpora
python -m spacy download en_core_web_sm
```

> If you get `ModuleNotFoundError: No module named 'flask_sqlalchemy'`, run:
>
```bash
pip install flask_sqlalchemy
```

---

### 🗃️ Step 3: Initialize the Database Tables

In Python shell:

```python
from app import app, db

with app.app_context():
    db.create_all()
```

This will create the `scrape_results` table in your PostgreSQL DB.

---

### ▶️ Step 4: Run the App

```bash
python run.py
```

- Visit the UI at: http://localhost:5000
- Access Swagger API docs at: http://localhost:5000/apidocs

---

## 📦 Included Files

- `app/`: Flask routes, scraper, analysis, DB models
- `templates/index.html`: HTML frontend
- `docker-compose.yml`: PostgreSQL container
- `config.py`: DB config
- `.env`: Optional PostgreSQL settings
- `requirements.txt`: All Python dependencies

---

## 🚀 Example API Call (using curl)

```bash
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

---

## ✅ Next Steps

- Add Dockerfile to containerize Flask app (optional)
- Add authentication or rate-limiting (if deploying)

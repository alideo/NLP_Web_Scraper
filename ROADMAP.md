# 🗺️ NLP Web Scraper – Project Roadmap

A feature-rich web scraping and NLP pipeline that extracts metadata, analyzes sentiment, and exposes results via API and UI.

---

## ✅ Phase 1: Foundational – Core MVP

- [x] Web scraping with `requests` + `BeautifulSoup`
- [x] Sentiment analysis using `TextBlob`
- [x] Named Entity Recognition (NER) with `spaCy`
- [x] Basic Flask API (`/api/analyze`)
- [x] PostgreSQL persistence
- [x] Simple HTML form UI
- [x] Swagger documentation using `flasgger`
- [x] Dockerized PostgreSQL with `docker-compose`

---

## 🚧 Phase 2: Intermediate – Usability & Scalability

- [ ] Dockerize Flask app with production-ready `Dockerfile`
- [ ] Add duplicate URL detection before scraping
- [ ] Batch scraping support via task queue (e.g., Celery + Redis)
- [ ] URL normalization and validation
- [ ] Add Full Text Search (PostgreSQL or ElasticSearch)
- [ ] Export results to CSV/JSON
- [ ] Search and filter UI for stored results
- [ ] Basic logging and request tracking

---

## 🚀 Phase 3: Advanced – Intelligence & Automation

- [ ] Topic modeling with BERTopic or LDA
- [ ] Page content summarization (e.g., T5 or BART)
- [ ] Emotion detection (e.g., NRCLex or huggingface models)
- [ ] Language detection + auto-translation
- [ ] Add JWT authentication for secure API access
- [ ] Visual dashboard with sentiment trends & entity frequency (Chart.js)
- [ ] Admin panel for result management
- [ ] Slack/Discord bot integration
- [ ] CI/CD setup with GitHub Actions
- [ ] Unit testing with `pytest`

---

## 🔮 Stretch Goals

- [ ] LLM-powered content classification and summarization
- [ ] RAG-based Q&A interface over scraped content
- [ ] Public API key support for 3rd-party consumption

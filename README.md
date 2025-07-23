# NLP Web Scraper

## Setup Instructions

```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m textblob.download_corpora
python -m spacy download en_core_web_sm

# Set up PostgreSQL and create database
# Update config.py with your DB credentials

# Run the app
python run.py
```

- Access UI at http://localhost:5000
- Swagger Docs at http://localhost:5000/apidocs

import os
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/nlp_scraper")
SQLALCHEMY_TRACK_MODIFICATIONS = False

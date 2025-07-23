from app import db

class ScrapeResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, unique=True, nullable=False)
    title = db.Column(db.String)
    sentiment = db.Column(db.String)
    entities = db.Column(db.Text)

from textblob import TextBlob
import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_text(text):
    blob = TextBlob(text)
    sentiment = "positive" if blob.sentiment.polarity > 0 else "negative"
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return sentiment, entities

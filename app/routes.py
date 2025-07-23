from flask import request, jsonify, render_template
from app import app, db
from app.scraper import scrape_metadata
from app.analyzer import analyze_text
from app.models import ScrapeResult
from flasgger import swag_from

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        title, text = scrape_metadata(url)
        sentiment, entities = analyze_text(text)
        result = ScrapeResult(url=url, title=title, sentiment=sentiment, entities=str(entities))
        db.session.add(result)
        db.session.commit()
        return render_template("index.html", result=result)
    return render_template("index.html")

@app.route("/api/analyze", methods=["POST"])
@swag_from({
    'parameters': [
        {
            'name': 'url',
            'in': 'json',
            'type': 'string',
            'required': True,
            'description': 'URL to analyze'
        }
    ],
    'responses': {
        200: {
            'description': 'Analysis result',
            'examples': {
                'application/json': {
                    'url': 'http://example.com',
                    'title': 'Example Title',
                    'sentiment': 'positive',
                    'entities': [['Example', 'ORG']]
                }
            }
        }
    }
})
def analyze_api():
    url = request.json.get("url")
    title, text = scrape_metadata(url)
    sentiment, entities = analyze_text(text)
    result = ScrapeResult(url=url, title=title, sentiment=sentiment, entities=str(entities))
    db.session.add(result)
    db.session.commit()
    return jsonify({
        "url": url,
        "title": title,
        "sentiment": sentiment,
        "entities": entities
    })

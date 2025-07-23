from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)
swagger = Swagger(app)

from app import routes, models

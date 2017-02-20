from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_pagedown import PageDown

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

pagedown = PageDown(app)

from app import views,controller,models

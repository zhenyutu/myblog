from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), index = True, unique = True)
    password = db.Column(db.String(64), index = True, unique = True)




class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key = True)
    markDownEdit = db.Column(db.Text)
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    title = db.Column(db.String(128))
    category = db.Column(db.String(32))
    tag = db.Column(db.String(32))

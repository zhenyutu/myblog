from app import db
from datetime import datetime
from markdown import markdown
import bleach

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), index = True, unique = True)
    password = db.Column(db.String(64), index = True, unique = True)




class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key = True)
    markDownEdit = db.Column(db.Text)
    htmlEdit = db.Column(db.Text)
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    title = db.Column(db.String(128))
    category = db.Column(db.String(32))
    tag = db.Column(db.String(32))
    describe = db.Column(db.Text)

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        target.htmlEdit = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True))

db.event.listen(Article.markDownEdit, 'set', Article.on_changed_body)

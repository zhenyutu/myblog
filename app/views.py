from app import app
from app import form
from app import db,models
from flask import render_template

@app.route('/')
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/index', methods=['GET','POST'])
def index():
    postForm = form.PostForm()
    article = models.Article(markDownEdit = postForm.markDownEdit.data,title = postForm.title.data,category = postForm.category.data,tag = postForm.tag.data)
    db.session.add(article)
    db.session.commit()
    articles = models.Article.query.order_by(models.Article.timestamp.desc()).all()
    return render_template("index.html",articles = articles)

@app.route('/create')
def create():
    return render_template("create.html")

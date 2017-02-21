from app import app
from app import db,models,form
from flask import render_template
from flask import request

@app.route('/')
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/index', methods=['GET','POST'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = models.Article.query.order_by(models.Article.timestamp.desc()).paginate(page, per_page=app.config['FLASKY_POSTS_PER_PAGE'],error_out=False)
    articles = pagination.items
    return render_template("index.html",articles = articles,pagination = pagination)

@app.route('/create')
def create():
    postForm = form.PostForm()
    return render_template("create.html",form = postForm)

@app.route('/article/<int:id>')
def article(id):
    article = models.Article.query.get_or_404(id)
    return render_template("article.html",article = article)

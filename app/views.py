from app import app
from app import db,models,form,service
from app import controller
from flask import render_template
from flask import request
import re

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = models.Article.query.order_by(models.Article.timestamp.desc()).paginate(page, per_page=app.config['FLASKY_POSTS_PER_PAGE'],error_out=False)
    articles = pagination.items
    recentArticles = models.Article.query.order_by(models.Article.timestamp.desc())[0:7]
    allArticles = models.Article.query.all();
    return render_template("index.html",articles = articles,pagination = pagination,tags = list(service.splitTags(allArticles)),recentArticles = recentArticles)

@app.route('/create')
def create():
    postForm = form.PostForm()
    print('in the create:')
    print(controller.loginState)
    if controller.loginState == True:
        return render_template("create.html",form = postForm)
    else:
        return render_template("login.html")

@app.route('/article/<int:id>')
def article(id):
    article = models.Article.query.get_or_404(id)
    return render_template("article.html",article = article)

@app.route('/category', methods=['GET','POST'])
def category():
    kind = request.args.get('kind')
    page = request.args.get('page', 1, type=int)
    pagination = models.Article.query.filter(models.Article.category == kind).order_by(models.Article.timestamp.desc()).paginate(page, per_page=app.config['FLASKY_POSTS_PER_PAGE'],error_out=False)
    articles = pagination.items
    allArticles = models.Article.query.all();
    recentArticles = models.Article.query.order_by(models.Article.timestamp.desc())[0:7]
    return render_template("category.html",articles = articles,pagination = pagination,tags = list(service.splitTags(allArticles)),recentArticles = recentArticles)

@app.route('/Tag', methods=['GET','POST'])
def Tag():
    kind = request.args.get('kind')
    page = request.args.get('page', 1, type=int)
    pagination = models.Article.query.filter(models.Article.category == kind).order_by(models.Article.timestamp.desc()).paginate(page, per_page=app.config['FLASKY_POSTS_PER_PAGE'],error_out=False)
    articles = pagination.items
    allArticles = models.Article.query.all();
    recentArticles = models.Article.query.order_by(models.Article.timestamp.desc())[0:7]
    tagArticle = service.isContainTag(allArticles,kind)

    return render_template("tag.html",articles = articles,pagination = pagination,recentArticles=recentArticles,tags = list(service.splitTags(allArticles)),tagArticle=tagArticle)

@app.route('/about')
def about():
    return render_template("about.html")

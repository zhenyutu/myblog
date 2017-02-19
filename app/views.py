from app import app
from flask import render_template

@app.route('/')
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/index')
def index():
    user={'name':'tuzhenyu'}
    return render_template("index.html",user=user)

@app.route('/create')
def create():
    return render_template("create.html")

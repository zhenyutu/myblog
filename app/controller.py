from app import app
from app import service,form,models,db
from flask import render_template,json,request
from flask import redirect,url_for

loginState = False

@app.route("/api/login", methods=['POST'])
def loginForm():
    data = json.loads(request.form.get("data"));
    state = service.loginCheck(str(data['username']),str(data['password']));
    global loginState

    if state == True:
        print('in the loginForm:')
        print(loginState)
        loginState = True
        return "success";
    else:
        loginState = False
        return "fail";

@app.route('/postForm', methods=['GET','POST'])
def postForm():
    postForm = form.PostForm()
    article = models.Article(markDownEdit = postForm.markDownEdit.data,title = postForm.title.data,category = postForm.category.data,tag = postForm.tag.data,describe = postForm.describe.data)
    db.session.add(article)
    db.session.commit()
    return redirect(url_for('index'))

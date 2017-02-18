from app import app
from app import service
from flask import render_template,json,request

@app.route("/api/login", methods=['POST'])
def loginForm():
    data = json.loads(request.form.get("data"));
    state = service.loginCheck(str(data['username']),str(data['password']));

    if state == True:
        return "success";
    else:
        return "fail";

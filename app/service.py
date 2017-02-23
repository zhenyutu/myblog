from app import db,models
import re

def loginCheck(name,password):
    user_list = models.User.query.all();
    try:
        user = models.User.query.filter_by(username=name).first();
    except:
        print("--------------------------------------");
    if user != None:
        if(password == user.password):
            return True;
        else:
            return False;
    else:
        return False;

def splitTags(allArticles):
    tags = set([])
    for article in allArticles:
        for tag in article.tag.split(', '):
            tags.add(tag)
    return tags

def isContainTag(articles,kind):
    articleList = []
    for article in articles:
        for tag in article.tag.split(', '):
            if tag == kind :
                articleList.append(article)
    return articleList

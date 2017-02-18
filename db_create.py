#!flask/bin/python
from app import db,models

db.create_all()

user_tom = models.User(username='tom',password='123123')
user_jim = models.User(username='jack',password='456456')

db.session.add(user_tom)
db.session.add(user_jim)
db.session.commit()

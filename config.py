import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_ON_REARDOWN = True

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

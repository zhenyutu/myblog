import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_ON_REARDOWN = True

#　跨域CSRF校验
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# 分页数目
FLASKY_POSTS_PER_PAGE = 3

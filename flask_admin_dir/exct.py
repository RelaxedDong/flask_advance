#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/9 9:00

from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_babelex import Babel

babel = Babel()
db = SQLAlchemy()
admin = Admin(name='我的站点')

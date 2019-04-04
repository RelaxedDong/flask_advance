#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/9 8:48

from flask import Flask
import os
from exct import admin,db,babel
from flask_admin_dir import views


from flask_admin_dir.models.flask_admin_models import Article

from flask_admin_dir import config

app = Flask(__name__,static_folder=os.path.dirname(os.path.dirname(__file__)+'/views/static/'))

print(os.path.dirname(os.path.dirname(__file__)+'/views/static/'))

def create_app():
    app.config.from_object('config.Development_Enviroment')
    admin.init_app(app)
    babel.init_app(app)
    db.init_app(app)
    admin.add_view(views.MyView(name=u'123'))
    admin.add_view(views.UserView(db.session,name='用户管理'))
    admin.add_view(views.MessageAdmin(db.session,name='文章管理'))
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/9 10:10
import os
class Development_Enviroment():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1/firstsqlalchemy"
    #跟踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'

class Online_Enviroment():
    DEBUG = False
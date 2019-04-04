#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/8 21:53


class Development_Enviroment():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1/firstsqlalchemy"
    #跟踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Online_Enviroment():
    DEBUG = False
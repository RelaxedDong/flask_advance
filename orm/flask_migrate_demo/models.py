#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/11 19:48
from exct import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(150),nullable=False)
    age = db.Column(db.Integer)
    address = db.Column(db.String(100))
    mother = db.Column(db.String(100))
    ha = db.Column(db.String(10))
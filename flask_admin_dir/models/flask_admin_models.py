#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/9 10:09
import datetime
from exct import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(150),nullable=False)
    age = db.Column(db.Integer,default=0)
    address = db.Column(db.String(100))
    face = db.Column(db.String(100))

    def __repr__(self):
        return self.username

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text())
    create_time = db.Column(db.DateTime,default=datetime.datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    author = db.relationship("User",backref='articles')





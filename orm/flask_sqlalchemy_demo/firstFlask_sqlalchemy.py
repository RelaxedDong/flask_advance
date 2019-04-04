#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/8 21:26

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object("config.Development_Enviroment")

db.init_app(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(150),nullable=False)


@app.route("/")
def index():
    db.create_all()
    return 'index'

if __name__ == '__main__':
    app.run()
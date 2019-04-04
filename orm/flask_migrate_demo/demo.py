#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/11 19:42

from flask import Flask
import config
from models import *
app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run()
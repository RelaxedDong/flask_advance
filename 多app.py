#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2018/12/29 17:46

from flask import Flask
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import  run_simple

app1 = Flask(__name__)
app2 = Flask(__name__)


@app1.route('/index1')
def index1():
    return 'index1'


@app2.route('/index2')
def index2():
    return 'index2'

# app1:不加任何后缀
# 127.0.0.1:5000/index1
dm = DispatcherMiddleware(app1, {
    # 前缀
# 127.0.0.1:5000/app2/index2
    '/app2': app2,
})

if __name__ == '__main__':
    run_simple('localhost', 5000, dm)

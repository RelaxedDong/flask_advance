#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/27 15:24


from flask import Flask,views,request,session
import functools
#Flask.run()

app = Flask(__name__)

def index():
    print(app.view_functions)
    return 'hello'


@app.route('/login')
def login():
    return 'login'

app.add_url_rule('/', 'index')
app.view_functions['index'] = index

if __name__ == '__main__':
    app.run()
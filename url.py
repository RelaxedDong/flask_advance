#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/27 15:24


from flask import Flask,views,request,session,url_for
import functools
#Flask.run()
Flask.add_url_rule

app = Flask(__name__)

def index():
    print(app.view_functions)
    print(url_for('index'))
    return 'hello'


@app.route('/login')
def login():
    return 'login'

app.add_url_rule('/', 'index')

# def add_url_rule(self, rule, endpoint=None, view_func=None,pt **oions):

app.view_functions['index'] = index

if __name__ == '__main__':
    app.run()
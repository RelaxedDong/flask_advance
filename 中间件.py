#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2018/12/26 11:39

from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

class MyWggi(object):
    def __init__(self,old_wsgi_app):
        self.old_wsgi_app = old_wsgi_app
    def __call__(self, environ, start_response):
        print('开始之前')
        ret = self.old_wsgi_app(environ, start_response)
        print('结束之后')
        return ret

if __name__ == '__main__':
    app.wsgi_app = MyWggi(app.wsgi_app)
    app.run()
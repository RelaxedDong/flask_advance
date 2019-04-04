#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/27 10:48

from flask import Flask,views,request,session
import functools
#Flask.run()
Flask.__call__
app = Flask(__name__)
app.secret_key = '123'

def login_required(f):
    @functools.wraps(f) #设置元信息
    def inner(*args,**kwargs):
        print(args,kwargs)
        return f(*args,**kwargs)
    return inner

# @app.route("/")
# @login_required
# def index(username=None):
#     print(username)
#     return 'index'

class Index(views.MethodView):
    decorators = [login_required,]
    def get(self):
        print(request)
        return 'index'
app.add_url_rule('/',view_func=Index.as_view('index'))

class Index(views.View):
    methods = ['GET','POST',]
    decorators = [login_required]
    def dispatch_request(self):
        if request.method == 'GET':
            print('视图函数')
            return 'this is index'
        else:
            return 'post'

# app.add_url_rule('/',view_func=Index.as_view('index'))
#
class Login(views.View):
    methods = ['GET']
    decorators = [login_required]
    def dispatch_request(self):
        session['name'] = 'donghao'
        return 'login success'
app.add_url_rule('/login',view_func=Login.as_view('login'))
#
# @app.before_request
# def before_request():
#     name = session.get('name')
#     if request.path == '/login':
#         return None
#     if name:
#         return None
#     else:
#         return '请先登录'


@app.before_request
def process_before1(*args,**kwargs):
    print('process_before1')
    # return '拦截'

@app.before_request
def process_before2(*args,**kwargs):
    print('process_before2')

@app.after_request
def process_after1(resp):
    #response 对象
    print('process_after1')
    return resp

@app.after_request
def process_after2(resp):
    print('process_after2')
    return resp
#before_request拦截返回后，视图函数不执行，after_request执行


@app.errorhandler(404)
def not_find(args):
    print(args)
    return 'this is 404',404

#模板函数
@app.template_global()
def ab(a1,a2):
    return a1+a2

# @app.template_context_processors


#过滤器
@app.template_filter()
def hello():
    pass
if __name__ == '__main__':
    app.run(debug=True)

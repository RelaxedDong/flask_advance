from flask import flash,Flask,request,make_response,session,redirect,url_for
import config
from functools import wraps
app = Flask(__name__)
app.config.from_object(config)
#
# def wrapper(func):
#     # @wraps(func)#设置函数元信息
#     def inner(*args,**kwargs):
#         print(inner.__name__)
#         if not session.get('username'):
#             redirect('/login')
#         return func(*args,**kwargs)
#     return inner
# from _thread import get_ident
#
# @app.route('/index/',endpoint='l1')
# @wrapper
# def index():
#     if request.method == 'GET':
#         # 请求相关信息
#         # request.method
#         # request.args
#         # request.form
#         # request.values
#         # request.cookies
#         # request.headers
#         # request.path
#         # request.full_path
#         # request.script_root
#         # request.url
#         # request.base_url
#         # request.url_root
#         # request.host_url
#         # request.host
#         # request.files
#         # obj = request.files['the_file_name']
#         # obj.save('/var/www/uploads/' + secure_filename(f.filename))
#
#         # 响应相关信息
#         # return "字符串"
#         # return render_template('html模板路径',**{})
#         # return redirect('/admin.html')
#
#         # response = make_response(render_template('admin.html'))
#         # response是flask.wrappers.Response类型
#         # response.delete_cookie('key')
#         # response.set_cookie('key', 'value')
#         # response.headers['X-Something'] = 'A value'
#         # return response
#         return '123'
#
# @app.route('/session/',endpoint='l2')
# @wrapper
# def mysession():
#     # session['name'] = 'donghao'
#     # return '设置成功'
#     session.pop('name',None)
#
#     return '删除成功'

@app.route('/')
def index():
    return '123'

if __name__ == '__main__':
    app.run()

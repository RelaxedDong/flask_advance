#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/4 10:19

from flask import Flask,render_template

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    print('before_first_request')

@app.before_request
def before_request():
    print('before_request')

@app.teardown_appcontext
def teardown_appcontext(*args,**kwargs):
    print(args,kwargs)
    print('teardown_appcontext')

@app.after_request
def after_request(response):
    print(response)
    return response


@app.template_filter('myfilter')
def template_filter(s):
    print(s)
    return s

@app.context_processor#上下文处理器。返回的字典中的键可以在模板上下文中使用
def context_processor():
    return {
        'username':'donghao',
        'age':21
    }

@app.errorhandler(404)
def errorhandler(error):
    print(error)
    return """<h1>page not find</h1>""",404

def say_hello(s):
    print("---s is ---",s)
    return 'hello'

app.add_template_filter(say_hello,'say_hello')

@app.add_template_global
def myfunc(value):
    return 'this is  add_template_global'

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)





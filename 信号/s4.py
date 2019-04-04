#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/3 21:19
from flask import before_render_template,\
    Flask,render_template,template_rendered,request_started,request_finished,got_request_exception
from flask import signals
"""
template_rendered = _signals.signal('template-rendered')
before_render_template = _signals.signal('before-render-template')
request_started = _signals.signal('request-started')
request_finished = _signals.signal('request-finished')
request_tearing_down = _signals.signal('request-tearing-down')
got_request_exception = _signals.signal('got-request-exception')
appcontext_tearing_down = _signals.signal('appcontext-tearing-down')
appcontext_pushed = _signals.signal('appcontext-pushed')
appcontext_popped = _signals.signal('appcontext-popped')
message_flashed = _signals.signal('message-flashed')
"""
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    a = 1/0
    return 'login'
# before_render_template_func
def before_render_template_func(*args,**kwargs):
    #print(args)
    #print(kwargs)
    print('------模板渲染之前------')


#template_rendered
def template_rendered_func(*args,**kwargs):
    #print(args)
    #print(kwargs)
    print('------模板渲染完成------')


def request_started_func(*args,**kwargs):
    #print(args)
    #print(kwargs)
    print('------request_started------')

def request_finished_func(*args, **kwargs):
    # print(args)
    # print(kwargs)
    print('------request_finished------')

#报错信号
def got_request_exception_func(*args,**kwargs):
    print(args)
    print(kwargs)
    print('------got_request_exception_func------')


before_render_template.connect(before_render_template_func)
template_rendered.connect(template_rendered_func)
request_started.connect(request_started_func)
request_finished.connect(request_finished_func)
got_request_exception.connect(got_request_exception_func)

@app.before_request
def before_request():
    print('before_request')

@app.before_first_request
def before_first_request():
    print('before_first_request')
# ......
Flask.wsgi_app
if __name__ == '__main__':
    app.run(debug=True)


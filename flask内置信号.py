#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/3 20:00

from flask import Flask,template_rendered,render_template,got_request_exception,request_started

app = Flask(__name__)

# def template_rendered_func(sender,**kwargs):
#     print(sender)
#     print(kwargs)
#
# template_rendered.connect(template_rendered_func)

# def got_request_exception_func(sender,*arge,**kwargs):
#     print(sender)
#     print(arge)
#     print(kwargs)
# got_request_exception.connect(got_request_exception_func)

def request_started_func(sender,*args,**kwargs):
    print(sender)
    print(args)
    print(kwargs)

@app.route('/')
def index():
    a = 1/0
    return render_template('signal.html')

if __name__ == '__main__':
    app.run()
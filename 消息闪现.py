#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2018/12/25 22:01

from flask import Flask,flash,get_flashed_messages,message_flashed,render_template,request

app = Flask(__name__)
app.secret_key = 'ajsfl'


@app.route('/set/')
def set():
    flash('的啦风景阿里山的肌肤')
    return 'hello'

app.app_context()

@app.route('/get/')
def get():
    date = get_flashed_messages()
    print(date)
    return 'hello'

@app.route('/')
def index():
    return render_template('index.html')


@app.template_global()
def sb(a1,a2):
    return a1+a2

@app.template_filter()
def db(a1,a2,a3):
    return a1+a2+a3

@app.template_filter('fl_address')
def fl_address(a):
    return '123'


if __name__ == '__main__':
    app.run()

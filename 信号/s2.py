#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/3 20:59
from flask import Flask,request,g
from s3 import login_signal

app = Flask(__name__)

@app.route("/login")
def login():
    username = request.args.get('name')
    if username:
        g.username = username
        login_signal.send("sender")
        return 'login success'
    else:
        return 'login fail'


if __name__ == '__main__':
    app.run(debug=True)
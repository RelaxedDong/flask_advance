#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/3 21:01
from blinker import Namespace
from flask import g,request
from datetime import datetime

NameSpace = Namespace()

login_signal = NameSpace.signal('login')

def login_func(sender):
    ip = request.remote_addr
    login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("login_log.txt",'a') as f:
        f.write("{0}*{1}*{2}\n".format(g.username,login_time,ip))

login_signal.connect(login_func)
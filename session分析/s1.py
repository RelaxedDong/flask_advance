#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/29 21:21

from flask import Flask,session
Flask.__call__
Flask.open_session

app = Flask(__name__)
app.secret_key = 'jasldfjlxljf'

@app.route("/")
def index():
    session['xxx'] = 213
    return 'index'
"""
请求进来：获取随机字符串，去‘数据库’中获取原来的个人数据，否则创建一个空容器 --->内存 对象（随机字符串，（放置数据的容器））
视图：操作内存中的对象（随机字符串，（容器））
相应：内存中的 对象(随机字符串,(容器))
      将数据保存到‘数据库’中
      把随机字符串写在用户cookie中
"""

if __name__ == '__main__':
    pass
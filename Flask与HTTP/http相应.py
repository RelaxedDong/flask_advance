#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/13 17:28

"""
报文首部：状态行（协议，状态码，原因短语）
(HTTP/1.1  200  ok)

报文首部：各种首部字段
(
Content-type: text/heml;charset=utf8
Content-Length:22
Server: Werkzeug/0.12.2  Python/3.6.4
Date:xxxx
)

空行

报文主体

(
<h1>hello</h1>
)


"""


"""
视图函数可以返回最多由三个元素组成的元组：响应主
体、状态码、首部字段

@app.route('/hello')
def hello():
...
return '<h1>Hello, Flask!</h1>', 201


@app.route('/hello')
def hello():
    ...
    return '', 302, {'Location', 'http://www.example.com'}



如果你想手动返回错误响应，更方便的方法
是使用Flask提供的abort（）函数
from flask import Flask, abort...
@app.route('/404')
def not_found():
    abort(404)

返回类型
response.mimetype = 'text/plain'


1.纯文本MIME类型：text/plain

2.HTMLMIME类型：text/html
3.XMLMIME类型：application/xml
4.JSONMIME类型：application/json
"""



















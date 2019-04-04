# #encoding:utf-8
# # __author__ = 'donghao'
# # __time__ = 2018/12/28 14:03
#
from flask import Flask,request,render_template
Flask.__call__
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return 'hello world'
#
# if __name__ == '__main__':
#     app.run()
# from werkzeug.local import  Local
# from threading import Thread
#
#
# class Mylocal(Local):
#     def __setattr__(self, name, value):
#         ident = self.__ident_func__()
#         storage = self.__storage__
#         try:
#             storage[ident][name] = value
#             print('try:',storage)
#         except KeyError:
#             storage[ident] = {name: value}
#             print('KeyError',storage)
#
# local = Mylocal()
# local.request = 'abc'
#
# class Mythread(Thread):
#     def run(self):
#         local.request = '123'
#         print('子线程',local.request)
#
# mythread = Mythread()
# mythread.start()
# mythread.join()
# print('主线程',local.request)

# from functools import partial
#
# class Foo(object):
#     def __init__(self):
#         self.name = 'donghao'
#     def __getattr__(self, item):
#         return item
#
# fo = Foo()
# def func(args):
#     print(args)
#     return getattr(fo,args)
#
#
# my = partial(func,'name')
#
# print(my())
from functools import partial

class HttpRequest(object):
    def __init__(self):
        self.method = "GET"
        self.body = b"name=abc@age=123"


class Foo(object):

    def __init__(self):
        self.request = HttpRequest()
        self.session = {"login":True,"is_super":False}

foo = Foo()

def func(args):
    return getattr(foo,args)

re_func = partial(func,'request')
se_func = partial(func,'session')


class LocalProxy(object):

    def __init__(self,local):
        self._local = local

    def _get_current_object(self):
        return self._local()

    def __getitem__(self, item):
        return getattr(self._get_current_object(),item)

request = LocalProxy(re_func)
ret = request._get_current_object().method
print(ret)

ret = request['method']
print(ret)

session = LocalProxy(se_func)
print(session._get_current_object())




#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2018/12/25 21:14

# def wrapper(func):
#     def inner(*args,**kwargs):
#         print(args)
#         print(kwargs.get('username'))
#         return func(*args,**kwargs)
#     return inner
#
# @wrapper
# def test(username='donghao'):
#     pass
#
# test(username='donghao')

#
# class Myroute():
#     def route(self,rule,**options):
#         def decorator(f):
#             endpoint = options.pop('endpoint', None)
#             if endpoint is None:
#                 print(f.__name__)
#             return f
#         return decorator
#
# app = Myroute()
# @app.route('/',methods=['GET','POST'])
# def index():
#     print('hahaha')
#
# class Person(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     def __call__(self, friend):
#         print( 'My name is %s...' % self.name)
#         print( 'My friend is %s...' % friend)
# p1 = Person(name='donghao',gender='女')
# # p1('Time')
# from werkzeug.serving import run_simple
#
# def run_simple(host,port,f,**options):
#     print(f())
#     print(options)
#
# class Flask():
#     def __init__(self,name):
#         self.name = name
#
#     def run(self):
#         host = '127.0.0.1'
#         port = '5000'
#         options = {}
#         run_simple(host, port, self, **options)
#
#     def __call__(self, *args, **kwargs):
#         print('我执行了')
#
# app = Flask(__name__)
# app.run()
def with_metaclass(meta):
    return meta("A", (object,), {})

class Base(object):
    def __call__(self, *args, **kwargs):
        print('我执行了')
        return type.__call__(self, *args, **kwargs)

class B(with_metaclass(Base)):
    def __init__(self,name):
        self.name = name

b = B('donghao')
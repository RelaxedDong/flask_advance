#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/29 19:25

# #python3写法
# class Foo(metaclass=type):
#     pass
#
# #python2 写法
# class Foo1():
#     __metaclass__ = type
#     pass


class MyType(type):
    def __init__(self,*args,**kwargs):
        print('init')
        super(MyType, self).__init__(*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print('call,调用类的__new__，再调用__init__')
        return super(MyType, self).__call__(*args,**kwargs)

class Foo(metaclass=MyType):
    pass

class Bar(Foo):
    pass

b = Bar()
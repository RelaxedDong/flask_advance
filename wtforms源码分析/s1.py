#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/29 19:54


class MyType(type):
    def __init__(self,*args,**kwargs):
        print('init')
        super(MyType, self).__init__(*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print('call')
        return super(MyType, self).__call__(*args,**kwargs)

# MyType("Base",(object,),{})是由MyType创建： metaclass = MyType
# type可以创建类,metaclass=type，MyType也可以创建类，metaclass=type

# class Base(metaclass=MyType):
#     pass

# 等价于
# Base = MyType("Base",(object,),{})

class Foo(MyType("Base",(object,),{})):
    pass

class Bar(Foo):
    pass

f = Bar()

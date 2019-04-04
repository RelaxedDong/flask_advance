#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/29 20:05

class MyType(type):
    def __init__(self,*args,**kwargs):
        print('init')
        super(MyType, self).__init__(*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print('call')
        return super(MyType, self).__call__(*args,**kwargs)


def with_metaclass(base):
    return MyType('MyType',(base,),{})

class Foo(with_metaclass(object)):
    pass

f = Foo()
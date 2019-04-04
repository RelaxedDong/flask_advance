#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/22 13:41

# class Mytype(type):
#     def __init__(self,*arge,**kwargs):
#         print('__init__')
#         super(Mytype, self).__init__(*arge,**kwargs)
#
#     def __call__(self, *args, **kwargs):
#         print(' Mytype  __call__')
#         return super(Mytype, self).__call__( *args, **kwargs)
#     def __new__(cls, *args, **kwargs):
#         print('我执行了')
#         # return super(Mytype, cls).__new__(cls,*args,**kwargs)
#         return type.__new__(cls,*args,**kwargs)
#
# class Foo(metaclass=Mytype):
#     pass
#
# class Bar(Foo):
#     pass
#
#
# f = Bar()
class Mytype(type):
    def __init__(self,*arge,**kwargs):
        print('__init__')
        super(Mytype, self).__init__(*arge,**kwargs)

    def __call__(self, *args, **kwargs):
        print(' Mytype  __call__')
        return super(Mytype, self).__call__( *args, **kwargs)
    def __new__(cls, *args, **kwargs):
        print('我执行了')
        # return super(Mytype, cls).__new__(cls,*args,**kwargs)
        return type.__new__(cls,*args,**kwargs)

# #Mytype('base',(object,),{})是Mytype创建
# #相当于metaclass = Mytype
# Base = Mytype('base',(object,),{})
#
# class Foo(Base):
#     pass
#
# f = Foo()

def with_metaclass(arg,base):
    return Mytype('Base',(base,),{})


class Foo(with_metaclass(Mytype,object)):
    pass
f = Foo()
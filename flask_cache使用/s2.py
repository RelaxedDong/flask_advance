#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/13 16:00


"""
另一个设置跳过缓存的方法是使用cached装饰器中的unless参数。
它接收一个可调用对象作为输入，如果可调用对象返回True则不使用缓
存。我们可以创建一个is_login（）函数，赋值给unless，即
cached（unless=is_login），这个函数会返回current_user.is_authenticated
的值。这样当用户登录后就会取消缓存
"""
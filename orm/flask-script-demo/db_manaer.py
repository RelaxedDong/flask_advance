#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/9 20:48
from flask_script import Manager

db_manager = Manager()
@db_manager.command
def hahaha():
    print('hahaha')
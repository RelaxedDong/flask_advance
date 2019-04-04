#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/9 20:29
import os,sys
from demo import app
from flask_script import Manager
from db_manaer import db_manager
manager = Manager(app)
manager.add_command('db',db_manager)
# sys.path.append(os.path.dirname(__file__))
@manager.command
def hello():
    print('hello world')

@manager.option('-u', '--url', dest='url')
@manager.option('-n', '--name', dest='name')
def helloa(name, url):
    print("hello", name, url)

if __name__ == '__main__':
    manager.run()
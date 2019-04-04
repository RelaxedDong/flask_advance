#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/3 19:22
from blinker import Namespace

#Namespace命名空间

#1.定义信号
Myspace = Namespace()
fire_signal = Myspace.signal('fire') #fire为信号名称

# 2.监听信号
# fire_bullet 接受参数：发送者sender
def fire_bullet(sender,username):
    print(sender)
    print('开始射击')
    print(username)


fire_signal.connect(fire_bullet)

#3.发送信号
fire_signal.send('xxx',username='donghao')
















#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/20 16:31

from flask import Flask, render_template
from flask_socketio import SocketIO,emit,send
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO()
socketio.init_app(app)

@app.route('/admin/')
def admin():
    return render_template('admin.html')

@app.route('/front/')
def front():
    return render_template('front.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

def ack(value):
    #客户端传递
    print( value)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    emit('response',('foo', 'bar', '快过年了哟，祝大家新年快乐~(管理员)'),broadcast=True, callback=ack)

# @socketio.on('send'):
#     pass

# 函数形式
import json
def return_json(data):
    emit('return_json',json.dumps(data))

socketio.on_event('return_json', return_json)
if __name__ == '__main__':
    app.run(debug=True)


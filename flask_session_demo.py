#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/4 12:36


from flask import Flask
from redis import Redis
from flask_session import RedisSessionInterface,MemcachedSessionInterface

app = Flask(__name__)
app.secret_key = 'asjdfl'

#conn = Redis(host='xxx',port='xxx')
#app.session_interface = RedisSessionInterface(conn,key_prefix='__')


@app.route('/')
def index():
    return '123'

if __name__ == '__main__':
    app.run(debug=True)

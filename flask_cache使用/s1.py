#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/13 15:11
from flask import Flask,request,url_for
from flask_caching import Cache
import config
import time

app = Flask(__name__)
app.config.from_object(config)
cache = Cache(app)


@app.route('/')
@cache.cached(60*10,query_string=True)
def index():
    time.sleep(2)
    name = request.args.get('name')
    return 'hello %s'%name

# @cache.cached(key_prefix='add')   # 结果一致
# def add(a,b):
#     time.sleep(2)
#     return a+b


@cache.memoize() # 只有发生传入同样参数 的调用才会使用缓存。
def add(a,b):
    time.sleep(2)
    return a+b


#cache.clear()  清楚所有缓存

@app.route('/me')
@cache.cached(60*10,query_string=True)
def me():
    """
    我们使用cache.delete（）方法删除缓存。
    视图函数缓存的键默认为“view/<请求路径
    request.path>”，这里我们使用url_for（）函数构建缓存的键，删除对应
    的缓存。另一方面，如果你在cached（）装饰器中通过key_prefix参数传
    入了自定义的键前缀，那么在删除时传入这个键即可
    """
    name = request.args.get('name')
    print(name)
    if name:
        cache.delete('view/%s' % url_for('me'))

        return 'cache has been delete'
    time.sleep(2)
    return 'my index view'

"""
对于使用memorize（）装饰器设置的缓存，你可以使用
delete_memorized（）方法来删除缓存，传入函数对象。另外，你还可
以调用cache.clear（）来清除程序中的所有缓存
"""

if __name__ == '__main__':
    app.run(debug=True)
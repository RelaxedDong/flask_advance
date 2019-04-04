#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/2 19:40
from flask import Response,Flask,jsonify

app = Flask(__name__)

class Myresponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        """这个方法只有视图函数返回非字符，非元祖，非Response对象才会调用"""
        if isinstance(response,dict):
            response = jsonify(response)
        return super(Myresponse, cls).force_type(response,environ)

app.response_class = Myresponse

@app.route("/")
def index():
    return {'username':'donghao'}


if __name__ == '__main__':
    app.run(debug = True)




#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/26 20:20
from flask import Flask,url_for,request,make_response
from werkzeug.routing import Rule,Map
from werkzeug.serving import run_simple
Flask.session_interface
from werkzeug.routing import BaseConverter
app = Flask(__name__)
class RegexConverter(BaseConverter):
    def __init__(self,*args,**kwargs):
        super(RegexConverter, self).__init__(*args,**kwargs)
        regex = '\d+'

    def to_python(self, value):
        print(value)
        return value

    def to_url(self, value):
        print('to url',value)
        return value
app.url_map.converters['regex'] = RegexConverter

@app.route('/detail/<regex:id>')
def index(id):
    print(url_for('index',id='1234567'))
    return id


from flask import stream_with_context, request, Response

@app.route('/stream')
def streamed_response():
    def generate():
        yield 'Hello '
        yield request.args['name']
        yield '!'
    return Response(stream_with_context(generate()))

if __name__ == '__main__':
    app.run(debug=True,use_evalex=True)  #use_evalex开启网页调试模式
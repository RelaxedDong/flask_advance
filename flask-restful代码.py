#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/3 20:42

from flask import Flask
from flask_restful import Api,Resource,reqparse,inputs,fields,marshal_with

app = Flask(__name__)

api = Api(app)

class Index(Resource):
    def get(self):
        return {"username":"donghao"}


class Article(object):
    def __init__(self,title,content):
        self.title = title
        self.content = content

article=  Article('abc','alsdjflasjdfl')
class ArticleView(Resource):
    source = {
        'title': fields.String,
    }

    @marshal_with(source)
    def get(self):
        return article


class LoginView(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('username',type=int,help='用户名错误',default='hahaha')
        parse.add_argument('password',type=str,help='密码错误',required=True)
        parse.add_argument('home_page',type=inputs.url,help='链接错误',required=True)
        parse.add_argument('gender',type=str,help='性别',choices=('male','female'))
        args = parse.parse_args()
        print(args)
        return {'args':args}

api.add_resource(Index,'/')
api.add_resource(ArticleView,'/article/')
api.add_resource(LoginView,'/login/')

if __name__ == '__main__':
    app.run(debug=True)


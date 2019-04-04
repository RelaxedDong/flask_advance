#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2018/12/28 14:03

from flask import Flask
Flask.route()

class Myroute(Flask):
    def route(self, rule, **options):
        #rule:'/'
        #**options :{'methods': ['POST', 'GET'], 'endpoint': 'index'}
        def decorator(f):
            print(f)
            endpoint = options.pop('endpoint', None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator


app = Myroute(__name__)

@app.route('/',methods=['POST','GET'],endpoint='index')
def index():
    return 'hello world'





if __name__ == '__main__':
    app.run(debug=True)

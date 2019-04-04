#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/4 12:36


from flask import Flask,request,render_template,g,session

app = Flask(__name__)
app.secret_key = 'asjdfl'


# @app.before_request
# def before_request():
#       if not hasattr(g,'user'):
#           setattr(g,'user','xxxx')



@app.before_first_request
def before_first_request():
    print('before_first_request')

@app.context_processor
def context_processor():
    if hasattr(g,'user'):
        return {'username':'donghao'}
    else:
        return {}

@app.teardown_appcontext
def teardown_appcontext(exc=None):
    print('teardown_appcontext')

@app.route('/')
def index():
    print('我执行了')
    #特殊的空字典
    #在local的ctx中找到session
    #在字典中写值
    #在字典中取值
    session['xxx'] = 123
    # session['xxx']
    return render_template('钩子函数index.html')


@app.route('/list/')
def list():
    print(g.user)
    return 'list'

if __name__ == '__main__':
    app.run(debug=True)

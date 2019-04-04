#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/13 15:52

from flask import Flask,render_template,request,send_from_directory
from wtforms import Form,StringField,IntegerField
from wtforms.validators import Length,EqualTo,URL,UUID,Required,NumberRange
import os
template_folder = os.path.dirname(__file__)

class RegisterForm(Form):
    name = StringField(validators=[Length(min=3,max=10,message='用户名为3~10个字符')])
    password1= StringField(validators=[Length(min=6,max=10,message='密码为3~10个字符')])
    password2 = StringField(validators=[EqualTo("password1",message='两次密码不一致')])

app = Flask(__name__,template_folder=template_folder+'/templates')


@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            name = form.name.data
            password = form.password1.data
            print(name, password)
            return '注册成功'
        else:
            print(form.errors)
            return '注册失败'


class SettingForm(Form):
    username = StringField(validators=[Required('请输入用户名')],label='用户名')
    age = IntegerField(validators=[NumberRange(min=0,max=110)],label='年龄')

@app.route('/setting/',methods=['GET','POST'])
def setting():
    form = SettingForm(request.form)
    if request.method == 'GET':
        return render_template('setting.html',form=form)
    else:
        if form.validate():
            username = form.username.data
            age = form.age.data
            print(username,age)
            return 'ok'
        else:
            print(form.errors)
            return '失败'

from werkzeug.datastructures import  FileStorage,ImmutableDict,CombinedMultiDict
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField,FileAllowed,FileRequired

class UploadForm(Form):
    avatar = FileField(validators=[FileAllowed(['png','jpg','jpeg']),FileRequired()])
    desc = StringField(validators=[Required()])

@app.route('/upload/',methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        form = UploadForm(CombinedMultiDict([request.form,request.files]))
        if form.validate_on():
            desc = form.desc.data
            file = request.files.get('avatar')
            # file.save(dst=secure_filename(file.filename))
            print(desc)
            print(file.filename)
            return 'ok'
        else:
            print(form.errors)
            return '失败'

@app.route('/images/<filename>/')
def images(filename):
    return send_from_directory(directory=os.path.dirname(__file__),filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
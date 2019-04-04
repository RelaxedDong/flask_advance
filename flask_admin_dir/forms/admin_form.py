#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/9 10:55

from flask_admin.form import BaseForm
from wtforms import StringField,IntegerField,FileField
from wtforms.validators import input_required,Length,number_range

class UserForm(BaseForm):
    username = StringField(validators=[input_required(message='请填入用户名')])
    age = IntegerField(validators=[number_range(min=0,max=100,message='年龄错误'),input_required(message='请输入年龄')])
    address = StringField(validators=[Length(max=10,min=2,message='长度错误'),input_required(message='请填入地址')])
    face = FileField()
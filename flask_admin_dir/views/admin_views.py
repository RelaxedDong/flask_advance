#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/9 8:57
from ..exct import admin

from flask_admin import BaseView, expose
from flask import url_for
from flask_admin.contrib.sqla import ModelView
from flask_admin_dir.models.flask_admin_models import User,Article
from wtforms.fields import SelectField
from exct import db
from flask_admin_dir.forms import admin_form
from wtforms import form
from flask_admin.form.upload import ImageUploadField
from flask_admin.form import thumbgen_filename
from sqlalchemy.event import listens_for
import os.path as op
import  os
from jinja2 import Markup,escape
from jinja2.filters import do_mark_safe
class MyView(BaseView):
#这里类似于app.route()，处理url请求
    @expose('/')
    def index(self):
        return self.render('admin-index.html')

class UserView(ModelView):
    can_create = True
    column_filters = ('username','age','address')
    column_display_pk = True
    column_list = ('username','age','address','face')
    column_labels = {'username':"用户名",'age':'年龄','address':'地址','face':'头像'}
    def __init__(self,session,**kwargs):
        super(UserView, self).__init__(User,session,**kwargs)
    form_extra_fields = {
        'face': ImageUploadField('Image',
                                     base_path='../static',
                                     relative_path='uploadFile/',
                                     thumbnail_size=(60, 60, True))
    }
    def _list_thumbnail(view, context, model, name):
        if not model.face:
            return ''
        print(model.face)
        return Markup('<img src="%s">' % url_for('static',
                                                 filename=thumbgen_filename(model.face)))

    column_formatters = {
        'face': _list_thumbnail
    }

class ArticleView(ModelView):
    can_create = True
    column_filters = ('title','content','author','create_time')
    def __init__(self,session,**kwargs):
        super(ArticleView, self).__init__(Article,session,**kwargs)


'富文本'
from wtforms import TextAreaField
from wtforms.widgets import TextArea
class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()

class MessageAdmin(ArticleView):
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']
    form_overrides = {
        'content': CKTextAreaField
    }


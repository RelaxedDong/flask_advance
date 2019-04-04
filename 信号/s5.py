#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/3 21:37

# 模板信号相关：
# 调用render_template之前：

"""
def _render(template, context, app):
    \"""Renders the template and fires the signal\"""
    before_render_template.send(app, template=template, context=context)
    #渲染前调用
    rv = template.render(context)

    template_rendered.send(app, template=template, context=context)

     #渲染完成调用
    return rv
"""


# before_render_template.send(app, template=template, context=context)


#wsgi_app:
"""
    def full_dispatch_request(self):
        \"""Dispatches the request and on top of that performs request
        pre and postprocessing as well as HTTP exception catching and
        error handling.

        .. versionadded:: 0.7
        \"""
        self.try_trigger_before_first_request_functions()
        try:
            request_started.send(self)  #开始请求之前执行
            
            rv = self.preprocess_request()  #钩子函数
"""

# 视图错误
"""
def handle_exception(self, e):
    \"""Default exception handling that kicks in when an exception
    occurs that is not caught.  In debug mode the exception will
    be re-raised immediately, otherwise it is logged and the handler
    for a 500 internal server error is used.  If no such handler
    exists, a default 500 internal server error message is displayed.

    .. versionadded:: 0.3
    \"""
    exc_type, exc_value, tb = sys.exc_info()

    got_request_exception.send(self, exception=e) #错误的信号
    
    handler = self._find_error_handler(InternalServerError())"""
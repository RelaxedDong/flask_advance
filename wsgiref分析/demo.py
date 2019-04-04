#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/29 14:17

def hello_world_app(environ, start_response):
    start_response("200 OK", [('Content-Type','text/html; charset=utf-8')])
    return ['<h1>hello world</h1>'.encode('utf-8')]



from wsgiref.simple_server import make_server
httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")
httpd.serve_forever()

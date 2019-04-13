#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/13 17:07


"""
报文首部 ：
(请求行  GET/ hello HTTP/1.1)

报文首部：各种首部字段
(
HOST: helloflask.com
Connection:keep-alive
Cache-Control: max-age=0
User-Agent: ......
Accept: test/heml,applicaion/xheml_xml,applicaion/xmal...
)

空行

报文主体:
name:donghao
"""

"""
报文由报文首部和报文主体组成，两者由空行分隔，请求报文的主
体一般为空。如果URL中包含查询字符串，或是提交了表单，那么报文
主体将会是查询字符串和表单数据。

报文首部包含了请求的各种信息和设置，比如客户端的类型、是否
设置缓存、语言偏好等



路由匹配
为了便于将请求分发到对应的视图函数，程序实例中存储了一个路
由表（app.url_map），其中定义了URL规则和视图函数的映射关系。
当请求发来后，Flask会根据请求报文中的URL（path部分）来尝试与这个
表中的所有URL规则进行匹配，调用匹配成功的视图函数。如果没有找
到匹配的URL规则，说明程序中没有处理这个URL的视图函数，Flask会
自动返回404错误响应（Not Found，表示资源未找到）



Flask内置的URL变量转换器（6种）
string：不包含斜线的字符串
int：   整形
float： 浮点数
path：  包含斜线的字符串
any：   匹配一系列给定值中的一个元素
uuid：  uuid字符串
"""
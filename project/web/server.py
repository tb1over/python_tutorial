# -*- coding: utf-8 -*-

# 负责启动WSGI服务器

from wsgiref.simple_server import make_server

from hello import application

httpd = make_server('', 8000, application)
print('Server HTTP on port 8000...')

#开始监听HTTP请求
httpd.serve_forever()
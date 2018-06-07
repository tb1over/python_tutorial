
# -*- coding:utf8 -*-

# 从app模块导入app变量
# 注意循环引用问题
from app import app


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World!'
# -*- coding:utf8 -*-

# 从app模块导入app变量
# 注意循环引用问题
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [{
        'author': {
            'username': 'Chris Paul'
        },
        'body': 'half chanmpion?'
    }, {
        'author': {
            'username': 'Stephen Curry'
        },
        'body': 'excuce me? Paul'
    }, {
        'author': {
            'username': 'James Harden'
        },
        'body': 'I am the MVP of 2017-2018 season'
    }]
    return render_template('index.html', user=user, title='首页', posts=posts)

# -*- coding:utf8 -*-

from flask import render_template, flash, redirect, url_for

# 从app模块导入app变量
# 注意循环引用问题
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'NXNUCC'}
    posts = [
        {
            'author' : {'username': 'Chris Paul'},
            'body' : 'half chanmpion?'
        },
        {
            'author':{'username': 'Stephen Curry'},
            'body' : 'excuce me? Paul'
        },
        {
            'author' : {'username': 'James Harden'},
            'body' : 'I am the MVP of 2017-2018 season'
        },
        {
            'author': {'username': 'Draymond Green'},
            'body' : '看脚'
        }
    ]
    return render_template('index.html', title='首页', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('登陆的用户名为: {}'.format(form.username.data))
        flash('登陆的密码为：%s' %  (form.password.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='登陆', form=form)
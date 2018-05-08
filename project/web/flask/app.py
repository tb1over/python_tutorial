# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__) # app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递__name_

# 使用app.route装饰器会将URL和执行的视图函数的关系保存到app.url_map属性上。 
# 处理URL和视图函数的关系的程序就是路由
@app.route('/', methods=['GET', 'POST']) 
def home():
    return render_template('home.html')  # render_template()函数来实现模板的渲染

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()
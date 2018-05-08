# chapt14 web frame 
在使用WSGI框架时，一个Web App，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应。

但是如何处理HTTP请求不是问题，问题是如何处理100个不同的URL。

每一个URL可以对应GET和POST请求，当然还有PUT、DELETE等请求，但是我们通常只考虑最常见的GET和POST请求。

一个最简单的想法是从environ变量里取出HTTP请求的信息，然后逐个判断：
```python
def application(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method=='GET' and path=='/':
        return handle_home(environ, start_response)
    if method=='POST' and path='/signin':
        return handle_signin(environ, start_response)
    ...
```
发现上述代码的问题了吧？

# 1. Web框架——Flask
```python
$ pip install flask
```
下面使用flask框架写一个很简单的演示应用，处理3个URL，分别是：

- GET /：首页，返回Home；
- GET /signin：登录页，显示登录表单；
- POST /signin：处理登录表单，显示登录结果。


Flask通过Python的装饰器在内部自动地把URL和函数给关联起来

```python
# project/web/flask_demo.py
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()
```
# 2. Flask框架总结
有了Web框架，在编写Web应用时，注意力就从WSGI处理函数转移到URL+对应的处理函数，这样，编写Web App就更加简单了。

在编写URL处理函数时，除了配置URL外，从HTTP请求拿到用户数据也是非常重要的。Web框架都提供了自己的API来实现这些功能。Flask通过request.form['name']来获取表单的内容。


# 3. 模板技术 
Web框架把我们从WSGI中拯救出来了。现在，只需要不断地编写函数，带上URL，就可以继续Web App的开发了。

但是还有什么问题，不知道大家有没有发现？

所有的页面HTML代码都是通过Python动态生成，返回给用户。

使用模板，我们需要预先准备一个HTML文档，这个HTML文档不是普通的HTML，而是嵌入了一些变量和指令，然后，根据我们传入的数据，替换后，得到最终的HTML，发送给用户：

![](https://cdn.liaoxuefeng.com/cdn/files/attachments/001400339839622665127663fb840b5870864895b103c2f000)

这就是传说中的MVC：Model-View-Controller，中文名“模型-视图-控制器”。

Python处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；

包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。

MVC中的Model在哪？Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。

上面的例子中，Model就是一个dict：
```python
{ 'name': 'Michael' }
```

使用MVC思想，重构上述例子：
```python
# project/web/flask/app.py
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html') # render_template()函数来实现模板的渲染

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
```
```html
<!-- Home.html -->
<!-- form.html -->
<!-- signin-ok.html-->
```
在Jinja2模板中，我们用{{ name }}表示一个需要替换的变量。很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用{% ... %}表示指令。

比如循环输出页码：
```html
{% for i in page_list %}
    <a href="/page/{{ i }}">{{ i }}</a>
{% endfor %}
```

除了Jinja2，常见的模板还有：
- Mako：用<% ... %>和${xxx}的一个模板；
- Cheetah：也是用<% ... %>和${xxx}的一个模板；
- Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。

## MVC小结
有了MVC，就分离了Python代码和HTML代码。HTML代码全部放到模板里，写起来更有效率。

# 4. 作业
结合以上例子，还有之前学习过的数据库访问技术、hashlib技术等知识点，完成一个具有用户注册、登陆的例子，要求用户名和密码保存在MySQL数据库中，密码字段要求md5加盐之后存储。
# 1. microblog - Hello World

## Installing Python

## Installing Flask

To install a package on your machine, you use pip as follows:
```
$ pip install <package-name> 
```
 The pip tool is going to download the package from PyPI[https://pypi.org/], and then add it to your Python installation

 ```python
$ mkdir microblog
$ cd microblog

pip install flask

# confirm the enviroment
import flask
 ```

 ## A "Hello World" Flask Application
 In Python, a sub-directory that includes a ```__init__.py``` file is considered a package, and can be imported. When you import a package, the ```__init__.py``` executes and defines what symbols the package exposes to the outside world.
 ### (1)  Create a package called app
 ```
mkdir app
 ```
 ### (2) Create ```__init__.py```

```python
# app/__init__.py
from flask import Flask

# 通过Flask类，实例化一个application object
# app : Flask的实例化对象，属于app模块的一个部分(成员)
app = Flask(__name__)

# app 代表app模块(app 目录)
from app import routes
```
```___name__```代表当前程序名称，还记得下列程序的写法吗：
```python

#module.py
def main():
    print "we are in %s"%__name__
if __name__ == '__main__':
    main()

# python module.py
# output?

```

```python
#anothermodle.py
from module import main
main()

# output?
```
“Make a script both importable and executable”
- 1、```__name__```这个系统变量显示了当前模块执行过程中的名称，如果当前程序运行在这个模块中，```__name__``` 的名称就是```__main__```如果不是，则为这个模块的名称。
- 2、```__main__```一般作为函数的入口，类似于C语言，尤其在大型工程中，常常有if ```__name__``` == ```"__main__"```来表明整个工程开始运行的入口。

### (3) Create routes.py 
```python
from app import app


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World!'
```
the @app.route decorator creates an association between the URL given as an argument and the function.

### (4) Crate microblog.py

为了完成程序，需要一个顶层的脚本来定义Flask程序实例
```python
# microblog.py
from app import app
# or app.run()
# python microblog.app
```
The Flask application instance is called app and is a member of the app package. The from app import app statement imports the app variable that is a member of the app package.

整个工程看起来长这样：
```
microblog/
  app/
    __init__.py
    routes.py
  microblog.py
```

### (5) run
```
export/set FLASK_APP=microblog.py

flask run

http://localhost:5000/

http://localhost:5000/index
```
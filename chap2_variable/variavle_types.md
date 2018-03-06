
<!-- TOC -->

- [1. hello_world.py](#1-hello_worldpy)
- [2. 变量](#2-变量)
    - [2.2 变量的命名和使用](#22-变量的命名和使用)
    - [2.2 避免命名错误](#22-避免命名错误)
- [3. 字符串](#3-字符串)
    - [3.1 修改字符串大小写](#31-修改字符串大小写)
    - [3.2 合并(拼接)字符串](#32-合并拼接字符串)
    - [3.3 使用制表符或换行符](#33-使用制表符或换行符)
    - [3.4 删除空白](#34-删除空白)
- [4. 数字](#4-数字)
    - [4.1 整数](#41-整数)
    - [4.2 浮点数](#42-浮点数)
    - [4.3 str()类型转换](#43-str类型转换)
- [5. 注释](#5-注释)

<!-- /TOC -->

# 1. hello_world.py
```python
print("Hello Python world!")
``` 
# 2. 变量
```python
message = 'Hello Python world!'
print(messge)
```
添加了一个名为messaged的变量.每个变量存储y一个值.
```python
message = 'Hello Python world'
print(message)

messge = 'Hello wonderful world'
print(message)
```
## 2.2 变量的命名和使用
- 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头,但不能以数字打头
- 变量名不能包含空格,但可使用下划线来分隔其中的单词
- 不要将 Python 关键字和函数名用作变量名,即不要使用 Python 保留用于特殊用途的单词,如 print
- 变量名应既简短又具有描述性
- 慎用小写字母 l 和大写字母 O
## 2.2 避免命名错误
```python
message = 'Hello Python World'
print(messge)
```
# 3. 字符串
字符串是程序中很多时候都在处理的数据结构。Python中使用引号(单、双都可)的都是字符串.
```python
'this is a string'
"this is also a string"
```

```python
'I told my friend, "Python is my favorite language!"'

"The language 'Python' is named after Monty Python, not the snake."

"One of Python's strengths is its diverse and supportive community."
```
## 3.1 修改字符串大小写
```python
name = "nxnu"
print(name.title())

print(name.upper())

print(name.lower())
```

## 3.2 合并(拼接)字符串
```python
first_name = 'nxnu'
last_name = 'sjxy'
full_name =  first_name + ' ' + last_name

print(full_name)
print('Hello ' + full_name + ' !')
```
## 3.3 使用制表符或换行符
```python
print('\tPython')

print('Language:\nPython\nHTML\nCSS\nJavascript')
```
## 3.4 删除空白
```python
favorite_language = 'Python '

favorite_language = favorite_language.rstrip()
# lstrip()  
# strip()
```

# 4. 数字
## 4.1 整数
```python
2 + 3   # 5
3 - 2   # 1
2 * 3   # 6
3 / 2   # 1.5 python2中，结果为1

3 ** 2  # 9
3 ** 3  # 27
10 ** 6 # 1000000

2 + 3 * 4 # 12
(2 + 3) *4 # 20

```
## 4.2 浮点数
```py
0.1 + 0.1  # 0.2
0.2 + 0.2  # 0.4
2 * 0.1    # 0.2
2 * 0.2    # 0.4

0.2 + 0.1  # 0.3???
3 * 0.1    # 0.3 ????
```
## 4.3 str()类型转换
下面代码有无问题？
```py
# birthday.py
age =  23
message = 'Hello ' + age + 'rd Birthday!'

print(message)
``` 
```py
massage = 'Hello ' + str(age) + 'rd Birthday!'
```
# 5. 注释
在 Python 中,注释用井号( # )标识。井号后面的内容都会被 Python 解释器忽略
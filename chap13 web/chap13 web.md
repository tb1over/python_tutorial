# chap13 Web Develop Introduction

<!-- TOC -->

- [chap13 Web Develop Introduction](#chap13-web-develop-introduction)
- [1. Web应用工作原理](#1-web应用工作原理)
    - [1.1. 从一个简单的网页浏览开始](#11-从一个简单的网页浏览开始)
    - [1.2. 名词定义](#12-名词定义)
        - [1.2.1. 客户端](#121-客户端)
        - [1.2.2. 服务器](#122-服务器)
        - [1.2.3. IP地址](#123-ip地址)
        - [1.2.4. DNS](#124-dns)
        - [1.2.5. 域名](#125-域名)
        - [1.2.6. 端口号](#126-端口号)
        - [1.2.7. HTTP](#127-http)
        - [1.2.8. URL](#128-url)
    - [1.3. 代码到页面生成过程](#13-代码到页面生成过程)
        - [1.3.1. 输入URL](#131-输入url)
        - [1.3.2. 域名解析](#132-域名解析)
        - [1.3.3. 向Web服务器发送请求](#133-向web服务器发送请求)
        - [1.3.4. Web服务器响应请求](#134-web服务器响应请求)
        - [1.3.5. 完成请求](#135-完成请求)
        - [1.3.6. 浏览器解析渲染生成页面。](#136-浏览器解析渲染生成页面)
- [2. Web应用程序结构](#2-web应用程序结构)
    - [2.1. B/S模型](#21-bs模型)
    - [2.2. 基本Web应用程序配置](#22-基本web应用程序配置)
        - [2.2.1. 客户端(Browser)](#221-客户端browser)
        - [2.2.2. 服务器(Server)](#222-服务器server)
        - [2.2.3. 数据库(DataBase)](#223-数据库database)
            - [2.2.3.1. Web应用结构示意](#2231-web应用结构示意)
- [3. HTTP协议](#3-http协议)
    - [3.1. 简介](#31-简介)
    - [3.2. URL/URI](#32-urluri)
    - [3.3. HTTP Request](#33-http-request)
        - [3.3.1. request headers](#331-request-headers)
        - [3.3.2. request method](#332-request-method)
        - [3.3.3. HTTP Response](#333-http-response)
        - [3.3.4. Response headers](#334-response-headers)
        - [3.3.5. Status Codes](#335-status-codes)
- [4. Web Server](#4-web-server)
    - [4.0 什么是Web Server](#40-什么是web-server)
        - [4.0.1 On the hardware side](#401-on-the-hardware-side)
        - [4.0.2 On the software side](#402-on-the-software-side)
    - [4.1 IIS](#41-iis)
    - [4.2 Tomcat](#42-tomcat)
    - [4.3 Apache](#43-apache)
    - [4.4 nginx](#44-nginx)
- [5. 参考资料](#5-参考资料)
- [6. 深入学习](#6-深入学习)
- [7. 作业](#7-作业)
- [8. WSGI: Web Server Gateway Interface](#8-wsgi-web-server-gateway-interface)
    - [8.1 运行WSGI服务](#81-运行wsgi服务)

<!-- /TOC -->
# 1. Web应用工作原理
## 1.1. 从一个简单的网页浏览开始
当在浏览器的地址栏里输入某个地址(域名/IP)，访问该站点的时候，背后发生了什么事情呢？
```
www.github.com
```
## 1.2. 名词定义
### 1.2.1. 客户端
在计算机上运行并连接到互联网的应用程序，如Chrome或Firefox。其主要作用是进行用户交互，并将其转换为对另一台称为Web服务器的计算机的请求。虽然我们通常使用浏览器访问网络，但您可以将整个计算机视为客户端 - 服务器模型的“客户端”。每个客户端计算机都有一个唯一的地址，称为IP地址，其他计算机可以用来识别它。
### 1.2.2. 服务器
连接到互联网且具有IP地址的机器。服务器等待来自其他机器（例如客户机）的请求并对其进行响应。不同于您的计算机（即客户端），服务器也具有IP地址并安装运行特殊的服务器软件，确定如何响应来自浏览器的请求。 Web服务器的主要功能是将网页存储，处理和传送给客户端。有许多类型的服务器，包括Web服务器，数据库服务器，文件服务器，应用程序服务器等
### 1.2.3. IP地址
互联网协议地址。 TCP / IP网络上的设备（计算机，服务器，打印机，路由器等）的数字标识符。互联网上的每台计算机都有一个IP地址，用于识别和与其他计算机通信。 IP地址有四组数字，以小数点分隔（例如244.155.65.2）。这被称为“逻辑地址”。为了在网络中定位设备，通过TCP / IP协议软件将逻辑IP地址转换为物理地址。这个物理地址（即MAC地址）内置在您的硬件中。
### 1.2.4. DNS
域名系统。跟踪计算机的域名及其在互联网上相应IP地址的分布式数据库。不要担心“分布式数据库”如何工作：只需要知道输入```www.github.com```, 而不是IP地址就行了。
### 1.2.5. 域名
用于标识一个或多个IP地址。使用域名（例如```www.github.com```, ）访问互联网上的网站。在浏览器中键入域名时，DNS使用它来查找该给定网站的IP地址。
### 1.2.6. 端口号
一个16位整数，用于标识服务器上的特定端口，并始终与IP地址相关联。它可以用来识别服务器上可以转发网络请求的特定进程.
### 1.2.7. HTTP
超文本传输协议。 Web浏览器和Web服务器用于通过互联网进行通信的协议。
### 1.2.8. URL
统一资源定位符。 URL识别特定的Web资源。一个简单的例子是https://github.com/tb1over. URL指定协议（“https”），主机名（```github.com```）和文件名（某人的个人资料页面）。用户可以从域名为github.com的网络主机通过HTTP获取该URL所标识的Web资源。
## 1.3. 代码到页面生成过程
### 1.3.1. 输入URL
 浏览器解析URL中包含的信息。包括协议（“https”），域名（“github.com”）和资源（“/”）。 在这种情况下，“.com”之后没有指示特定的资源，所以浏览器知道检索主（索引）页面

![](http://p0.qhimg.com/t01c869ebeabdd534c1.png)

### 1.3.2. 域名解析 
浏览器与DNS服务器通信，解析域名```www.github.com```对应的IP地址（媒人）

![](http://p0.qhimg.com/t0131e28807f376490e.gif)

浏览器获得```github.com```对应的IP地址

浏览器从URL中获取IP地址和给定的端口号（HTTP协议默认为端口80，HTTPS默认为端口443），并打开TCP套接字连接。 此时，Web服务器终于可以连接
![](http://p0.qhimg.com/t01f981a5ba2985f958.png)

### 1.3.3. 向Web服务器发送请求

![](http://p0.qhimg.com/t011fb50edbb274e338.png)

### 1.3.4. Web服务器响应请求

Web服务器接收请求并查找该HTML页面。 如果页面存在，则Web服务器准备响应并将其发送回您的浏览器。 如果服务器找不到请求的页面，它将发送一个HTTP 404错误消息，代表“找不到页面”。
![](http://p0.qhimg.com/t0101a1197df9353e5d.png) 

Web浏览器将接收到HTML页面，然后通过它从上到按下解析寻找列出的其他资源，如图像，CSS文件，JavaScript文件等。

### 1.3.5. 完成请求

浏览器完成加载HTML页面中列出的所有其他资源后，页面将最终加载到浏览器窗口中，并且连接将被关闭。

### 1.3.6. 浏览器解析渲染生成页面。

![](http://p0.qhimg.com/t01580da28230348db3.jpg)
# 2. Web应用程序结构
## 2.1. B/S模型
通过网络通信的客户端和服务器的这一想法称为“客户端 - 服务器”模型。 这让浏览网站（如此）和与Web应用程序（如GitHub）进行交互变为可能。
## 2.2. 基本Web应用程序配置
### 2.2.1. 客户端(Browser)

客户端是用户与之交互的。 因此，“客户端”代码对用户实际看到的大部分内容负责。 这包括：
- 定义网页的结构(HTML) 
- 设置网页的外观(CSS)
- 实现响应用户交互的机制（点击按钮，输入文本等）(JavaScript)

### 2.2.2. 服务器(Server)
Web应用程序中的服务器监听来自客户端的请求。 设置HTTP服务器时，将其设置监听一个端口号。端口号始终与计算机的IP地址相关联。

设置了HTTP服务器来侦听特定的端口，服务器将等待来自该特定端口的客户端请求，执行该请求所描述的操作，并通过HTTP发送响应请求的数据。

### 2.2.3. 数据库(DataBase)
 数据库是存储信息的地方，可以轻松访问，管理和更新信息。
 - 关系型：
    - Oracle
    - MySQL
    - PostgreSQL
    - SQLServer Access 
    - DB2
    - SQLite
    - ......
- 非关系型(NoSQL)
    - MongoDB
    - Redis 
    - ......

![](https://github.com/tb1over/js_tutorial/blob/master/img/DB-Engines%20Ranking.jpg?raw=true)

各大数据库使用情况。[DB-Engines Ranking](https://db-engines.com/en/ranking)


#### 2.2.3.1. Web应用结构示意
![](http://p0.qhimg.com/t017ec73fc3eddd9971.png)

![](http://p0.qhimg.com/t01a36cc19ec9076f2f.png)

![](http://p0.qhimg.com/t01c360c3a400b88362.png)


# 3. HTTP协议
## 3.1. 简介
HTTP协议是Hyper Text Transfer Protocol（超文本传输协议）的缩写,是用于从万维网（WWW:World Wide Web ）服务器传输超文本到本地浏览器的传送协议。

HTTP协议工作于客户端-服务端架构为上。浏览器作为HTTP客户端通过URL向HTTP服务端即WEB服务器发送所有请求。Web服务器根据接收到的请求后，向客户端发送响应信息。

![](http://upload-images.jianshu.io/upload_images/2964446-5a35e17f298a48e1.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 3.2. URL/URI
URL,全称是UniformResourceLocator, 中文叫统一资源定位符,是互联网上用来标识某一处资源的地址;

URI,统一资源标识符（Uniform Resource Identifiers),用来标示一个资源.

区别与联系：URL是一种具体的URI,URL不止标示出了资源，而且还指明了如何Locate这个资源。

## 3.3. HTTP Request
### 3.3.1. request headers

- Accept
- Accept-Encoding
- Host
- User-Agent
- ...... 

### 3.3.2. request method
- GET
- POST
- PUT
- DELETE
- TRACE
- HEAD

### 3.3.3. HTTP Response

### 3.3.4. Response headers

- Cache-Control
- Date
- ......

### 3.3.5. Status Codes
- 2**
- 3**
- 4**
- 5**

```js
常见状态代码、状态描述、说明：
200 OK      //客户端请求成功
400 Bad Request  //客户端请求有语法错误，不能被服务器所理解
401 Unauthorized //请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用 
403 Forbidden  //服务器收到请求，但是拒绝提供服务
404 Not Found  //请求资源不存在，eg：输入了错误的URL
500 Internal Server Error //服务器发生不可预期的错误
503 Server Unavailable  //服务器当前不能处理客户端的请求，一段时间后可能恢复正常
```

# 4. Web Server 

## 4.0 什么是Web Server

### 4.0.1 On the hardware side
a web server is a computer that stores web server software and a website's component files (e.g. HTML documents, images, CSS stylesheets, and JavaScript files). It is connected to the Internet and supports physical data interchange with other devices connected to the web.
### 4.0.2 On the software side
a web server includes several parts that control how web users access hosted files, at minimum an HTTP server. An HTTP server is a piece of software that understands URLs (web addresses) and HTTP (the protocol your browser uses to view webpages). It can be accessed through the domain names (like mozilla.org) of websites it stores, and delivers their content to the end-user's device.

![](https://mdn.mozillademos.org/files/8659/web-server.svg)

At the most basic level, whenever a browser needs a file hosted on a web server, the browser requests the file via HTTP. When the request reaches the correct web server (hardware), the HTTP server (software) accepts request, finds the requested document (if it doesn't then sends page 404), and sends it back to the browser, also through HTTP.
## 4.1 IIS
![](http://www.monitis.com/blog/wp-content/uploads/2012/03/iis7.jpg)
## 4.2 Tomcat
![](http://tomcat.apache.org/res/images/tomcat.png)

## 4.3 Apache
![](https://www.unixmen.com/wp-content/uploads/2015/03/Apache-http-server.png)

## 4.4 nginx 
![](https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/crop%3D39%2C0%2C520%2C343%3Bc0%3Dbaike80%2C5%2C5%2C80%2C26/sign=8c66573091504fc2b610ea45d8eede3d/e1fe9925bc315c6097e0b0d787b1cb1349547795.jpg)

# 5. 参考资料

[1. How the Web Works Part III: HTTP & REST](http://www.zcfy.cc/original/4136)

[2. Web Server from MDN](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server)

[3. Web Server from Wikipedia](https://en.wikipedia.org/wiki/Web_server)


# 6. 深入学习

# 7. 作业

-  写一篇使用chrome(firefox...)浏览器对某个URL的调试访问过程(GET/POST)，要求分析HTTP协议通信过程，分析请求信息、响应信息、使用的HTTP方法。
-  翻译参考资料3中维基百科关于Web Server的定义。
- HTTP方法的详细作用、使用场景，比如HTTP GET与HTTP POST


# 8. WSGI: Web Server Gateway Interface
一个Web应用的本质就是：
- 浏览器发送一个HTTP请求；
- 服务器收到请求，生成一个HTML文档；
- 服务器把HTML文档作为HTTP响应的Body发送给浏览器；
- 浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。
最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。

如果要动态生成HTML，就需要把上述步骤自己来实现。不过，接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，要花很长时间读HTTP规范。

正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。所以，需要一个统一的接口，让我们专心用Python编写Web业务。

这个接口就是WSGI。

WSGI接口定义非常简单，它只要求实现一个函数，就可以响应HTTP请求:
```python
'''
environ：一个包含所有HTTP请求信息的dict对象；
start_response：一个发送HTTP响应的函数。
'''
def application(environ, start_response):   
    start_response('200 OK', [('Content-Type', 'text/html')])  # HTTP Response Header
    return [b'<h1>Hello, web!</h1>']                           # HTTP Response Body
```

OK! 有了WSGI之后，Web应用流程变为如下步骤:
- 定义符合WSGI标准的HTTP处理函数:application；
- 从environ中拿到HTTP请求消息；
- 处理HTTP请求(构造HTML);
- HTTP Response (start_response(), 返回body)

好消息，Python中内置了一个WSGI服务器，该模块叫wsgiref, 是一个Python编写的WSGI服务器的实现。仅供开发和测试使用，不能用于生产环境。

## 8.1 运行WSGI服务

```python
# hello.py
# -*- coding: utf-8 -*-

'''
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, Python Web!</h1>']
    '''

def application(environ, start_response):
    print(environ['PATH_INFO'])
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
```

```python
# server.py

# -*- coding: utf-8 -*-

# 负责启动WSGI服务器

from wsgiref.simple_server import make_server

from hello import application

httpd = make_server('', 8000, application)
print('Server HTTP on port 8000...')
#开始监听HTTP请求
httpd.serve_forever()
```
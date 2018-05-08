#coding:utf-8
from urllib import request
# 创建request对象  
req = request.Request('http://baike.baidu.com/item/Android')  
  
# 添加数据  
#req.add_header('User-Agent', 'Mozilla/5.0')  
  
# 发送请求获取结果  
res = request.urlopen(req)  
  
# 获取状态码  
statusCode = res.getcode()  
print(statusCode)  
  
# 读取内容  
content = res.read().decode('utf-8')  
print(content)  
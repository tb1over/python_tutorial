from urllib import request
from bs4 import BeautifulSoup

'''
pip install beautifulsoup4
'''

# 创建request对象  
req = request.Request('http://xwzx.nxnu.edu.cn/yw.htm')  
  
# 添加数据  
req.add_header('User-Agent', 'Mozilla/5.0')  
  
# 发送请求获取结果  
res = request.urlopen(req)  
  
# 获取状态码  
statusCode = res.getcode()  
print(statusCode)  
  
# 读取内容  
soup = BeautifulSoup(res.read(), "html.parser") 
# print(soup.prettify()) 
table = soup.find_all('table')
for t in table:
    if t.has_attr('class') and t.attrs['class'][0] == 'winstyle155541':
        print(t )
        print('\n\n')

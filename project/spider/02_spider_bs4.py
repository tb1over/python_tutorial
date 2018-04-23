from urllib import request
from bs4 import BeautifulSoup
from bs4 import NavigableString

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
#statusCode = res.getcode()  
#print(statusCode)  

def get_information(tr_tag):
    if isinstance(tr_tag, NavigableString):
        return

    for t in tr_tag.children:  # contents
        if isinstance(t, NavigableString):
            continue
        # print(t)
        a = t.find('a')
        if a is not None:
            print(a['title'])
            print(a['href'])
        
        span_time = t.find('span', "timestyle155541")
        if span_time is not None:
            print(span_time.get_text())
      
    
# 读取内容  
soup = BeautifulSoup(res.read(), "html.parser") 
#print(soup.body) 
table = soup.find_all('table')
for t in table:
    if t.has_attr('class') and t.attrs['class'][0] == 'winstyle155541':
        #print(t.contents[1]['id'])
        for child in list(t.children)[0:-2]:        # table的所有子元素
            #print(child.name)  # tr
            get_information(child)
            print('\n')

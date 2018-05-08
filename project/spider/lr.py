#coding=utf-8
import requests
import re
import csv
from bs4 import BeautifulSoup

csvdata = {}
rows = []
for i in range(1,8):
    url = "http://jw.nxnu.edu.cn/gz/"+str(i)+".htm"
    r = requests.get(url)
    html = r.content.decode("utf-8")
    soup = BeautifulSoup(html,"html.parser")
    Pc = soup.find_all("a",attrs={"class":"f43186"})
    for pc in Pc:
        url = pc['href']
        title = pc.get_text()
        Pachong = requests.get(str(url).replace("..","http://jw.nxnu.edu.cn"))
        Ppachong = BeautifulSoup(Pachong.content.decode("utf-8"),"html.parser")
        time = Ppachong.find("span",attrs={"class":"timestyle43191"}).get_text()
        content = Ppachong.find("td",attrs={'class':"contentstyle43191"}).get_text()
        print("--------------------------------------")
        print(title)
        csvdata['Title'] = pc.get_text()
        print(time)
        csvdata['Time'] = Ppachong.find("span",attrs={"class":"timestyle43191"}).get_text()
        print(content)
        csvdata['Content'] = Ppachong.find("td",attrs={'class':"contentstyle43191"}).get_text()
        rows.append(csvdata)
        csvdata = {}
	
headers = {'Title', 'Time', 'Content'}
with open('lry.csv','w',newline='',encoding='gb18030') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
#-*-coding:utf-8-*-
'''
html_downloader.py 上面爬虫流程图中的[下载器]
负责对指定的 URL 网页内容进行下载获取，这里只是简单处理了 HTTP CODE 200，实质应该依据 400、500 等分情况进行重试等机制处理。
'''

from urllib import request

class HtmlDownLoader(object):
    def download(self, url):
        if url is None:
            return None
        # response = urllib.request.urlopen(url)
        req = request.Request(url)
        response = request.urlopen(req) 

        if response.getcode() != 200:
            return None
        return response.read()
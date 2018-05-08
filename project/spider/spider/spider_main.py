#-*-coding:utf-8-*-

'''
spider_main.py 上面爬虫流程图中的[调度器]
面向对象写法，调度器负责循环从 UrlManager 获取爬取链接，然后交给 HtmlDownLoader 下载，然后把下载内容交给 HtmlParser 解析，然后把有价值数据输出给 HtmlOutput 进行应用。
'''

import url_manager
import html_downloader
import html_parser
import html_output

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.out_put = html_output.HtmlOutput()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s" % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content,
                                                       "utf-8")
                self.urls.add_new_urls(new_urls)
                self.out_put.collect_data(new_data)
                #默认只爬取了深度 30，不然太慢，自己可以修改。
                if count >= 30:
                    break
                count = count + 1
            except Exception as e:
                print("craw failed!\n" + str(e))
        self.out_put.output_html()


if __name__ == "__main__":
    rootUrl = "http://baike.baidu.com/item/Android"
    objSpider = SpiderMain()
    objSpider.craw(rootUrl)
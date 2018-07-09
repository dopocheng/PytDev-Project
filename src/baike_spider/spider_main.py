#coding: utf8
'''
爬虫总调
Created on 2018年7月9日
@author: dopoc
'''
from baike_spider import url_manager, html_downloader, html_outputer, html_parser

class SpiderMain(object):
    
    def __init__(self):
        #初始化
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        
    def craw(self,root_url):
        count = 1#计数
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            #  print 'while####'
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)#打印条目
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count == 100:
                    break
                count += 1
        
            except:
                print 'craw faild'
            
        self.outputer.output_html()
#必须写在类后面      
if __name__== "__main__":
    #爬虫入口URL
    root_url = "https://baike.baidu.com/item/Python/407313"
    #爬虫总调度编写
    obj_spider = SpiderMain()
    #爬虫启动
    obj_spider.craw(root_url)
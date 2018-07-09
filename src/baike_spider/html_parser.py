#coding: utf8
'''
Created on 2018年7月9日

@author: dopoc
'''
#解析器
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
    
    def parse(self, page_url, html_cont):#解析出新的数据和url列表
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf8')
        new_urls = self.get_new_urls(page_url, soup)
        new_data = self.get_new_data(page_url, soup)
        return new_urls, new_data
    
    def get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item/\w+'))#r"/view/\d+\.htm" r'/item/\w+'
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    def get_new_data(self, page_url, soup):
        res_data = {}
        
        #url
        res_data['url'] = page_url  
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node =soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()  
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        #urllib2.urlopen()方法对于有的链接会超时，可以加个异常判断，跳过这一条
        try:
            summary_node = soup.find('div', class_="lemma-summary")
            res_data['summary'] = summary_node.get_text()
            
        except:
            print 'summary_node error!'
        
        return res_data
    
    
#coding: utf8
import urllib2

#网页下载器
class HtmlDownloader():
    
    def download(self,url):
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
    
        if response.getcode() != 200:#判断请求是否失败
            return None
        return response.read()#返回下载好的内容
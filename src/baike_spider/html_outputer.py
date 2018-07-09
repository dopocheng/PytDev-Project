#coding: utf8
"""
Created on 2018年7月9日

@author: dopoc
"""

#输出器
class HtmlOutputer():
    def __init__(self):
        self.datas = []
        
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    
    def output_html(self):
        fout = open("output.html", "w")
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        
#       默认编码 ascii
        for data in self.datas:
            #处理ie下乱码问题
            fout.write('<meta charset="utf-8"')
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data["url"])
            fout.write("<td>%s</td>" % data["title"].encode("utf-8"))
            try:#处理异常
                fout.write("<td>%s</td>" % data["summary"].encode("utf-8"))
            except:
                print 'output summary error'
            fout.write("</tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
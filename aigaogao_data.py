import re
import urllib.request
import xml.dom.minidom
import requests
from bs4 import BeautifulSoup
def createurl():
    filename = 'e:\\download\\merge.txt'
    file = open(filename,mode='r',encoding='UTF-8')
    text = file.read()
    file.close()
    url_list = []
    mergekeyvalue = re.split('\)',text)
    for verystock in mergekeyvalue:
        tempstock = re.split('\(',verystock)
        if len(tempstock) > 0 and tempstock[0] and tempstock[1]:
            url_list.append('http://aigaogao.com/tools/history.html?s='+tempstock[1])
    return url_list

url_list=createurl()
# print(url_list)

def getHtml(url):
    while True:
        try:
            html = urllib.request.urlopen(url, timeout=5).read()
            break
        except:
            print("超时重试")
    html = html.decode('utf8')
    return html

res = r'<td>(.*?)</td><td>(.*?)</td>'
# for itemurl in url_list:
    # getHtmlContent = getHtml(itemurl)
    # getHtmlContent = getHtml('http://aigaogao.com/tools/history.html?s=900956')
    # dom = xml.dom.minidom.parse(getHtmlContent)
    # dom.getElementById('ctl16_summarydiv')
    # print(dom.getElementById('ctl16_summarydiv'))
    # texts = re.findall(res, getHtmlContent, re.S|re.M)
    # for m in texts:
    #     print (m[0],m[1])

# getHtmlContent = getHtml('http://aigaogao.com/tools/history.html?s=900956')
# print(getHtmlContent)
# dom = xml.dom.minidom.parse(getHtmlContent)
# print(dom)
# dom.getElementById('ctl16_summarydiv')
# print(dom.getElementById('ctl16_summarydiv'))
r = requests.get(url='http://aigaogao.com/tools/history.html?s=900956')
a = BeautifulSoup(r.text,"html.parser")
print(r.text)
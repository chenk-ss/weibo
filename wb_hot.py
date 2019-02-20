#!/user/bin/python3
#-*-coding:UTF-8-*-

#获取https://s.weibo.com/top/summary?cate=realtimehot微博热搜

import urllib.request
import re
from bs4 import BeautifulSoup as bs

def open_url(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
    page=urllib.request.urlopen(req)
    html=page.read().decode('utf-8')
    #print(html)
    return html

def hot_search(html):
    soup=bs(html,"lxml")
    title=soup.find("title")
    print(title.string)
    list1=soup.find_all("a",attrs={"href":re.compile("weibo\?q"),"recursive":False})
    print(len(list1))
    k=0
    for i in list1:
        if i.text is not None:
            print(str(k)+":"+i.text)
        k+=1
    

if __name__=='__main__':
    #微博热搜地址
    url='https://s.weibo.com/top/summary?cate=realtimehot'
    html=open_url(url)
    hot_search(html)
    a=input("-----按任意键退出------")

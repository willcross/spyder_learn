import requests
from bs4 import BeautifulSoup

def nav2pageurl(pageurl):
    #this function is for wyckofftrade.com blog page download,if other website,need make some modify
    
    res = requests.get(pageurl)
    res.encoding=res.apparent_encoding
    
    soup = BeautifulSoup(res.text,'html.parser')
    
   
    urlist = []
   
    
    c2 =  soup.find('div',class_='page_navi').descendants 
    for i in c2:
        if i.name==u'a':
                print(i)
                urlist.append( i.get('href'))
    out =list(set(urlist))
    out.sort()
    return out
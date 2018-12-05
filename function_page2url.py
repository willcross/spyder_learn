import requests
from bs4 import BeautifulSoup

def page2url(pageurl):
    #this function is for wyckofftrade.com blog page download,if other website,need make some modify
    
    res = requests.get(pageurl)
    res.encoding=res.apparent_encoding
    
    soup = BeautifulSoup(res.text,'html.parser')
    
   
    urlist = []
    filenamelist=[]
    #c1 = soup.find('div',class_='blog-list').children
    # for i in c1:
        # if i.name:
            
            # print('---------------------')
            # if i.name == u'div':
                # for j in i.children:
                    # if j.name==u'a':
                        # print(j)
                        # if j.get('class')==[u'title'] :
                                    # urlist.append = j.get('href')
                                    # filenamelist.append = j.get('title')
    c2 =  soup.find('div',class_='blog-list').descendants 
    for i in c2:
        if i.name==u'a':
                print(i)
                if i.get('class')==[u'title'] :
                            urlist.append( i.get('href'))
                            filenamelist.append( i.get('title'))
    return urlist,  filenamelist
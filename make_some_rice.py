
import tushare as ts
import time
import requests
def price_predict(l1,l2,t1,t2):
    #l1 is oldest; l2 is nearest ; t1 is timerange between l2 and l1
    #t2 is timerange between wanted days and l2
    k = (l2-l1)/(t1-1)
    out = k*(t2-1)+l2
    return out
    
    
    
def print_price(id):
    id = str(id)
    out = ts.get_hist_data(id,ktype='D')
    c = float(out['close'][0])
    h = float(out['high'][0])
    l = float(out['low'][0])
  
    print ['price','percent' ,'high','low']
    while True:
        df = ts.get_realtime_quotes(id)
        price = float(df['price'][0])
        high = float(df['high'][0])
        low = float(df['low'][0])
        percent = round((price-c)/c*100,2)
        # print df[['price','high','low']]
        print ['----','----' ,'----','----']
        print [price,percent,high,low]
        time.sleep(30)
        
def print_price2(id):
    id = str(id)
    if id[0]=='6':
        url = 'http://hq.sinajs.cn/list=sh'+id
    else:
        url = 'http://hq.sinajs.cn/list=sz'+id
    
    
  
    print ['price','percent' ,'high','low','time']
    r=[]
    while True:
        r= requests.get(url)
        out = (r.text).split(',')
        o = float(out[1])
        c = float(out[2])
        price = float(out[3])
        
        high = float(out[4])
        low = float(out[5])
        percent = round((price-c)/c*100,2)
        timee = out[31]
        # print df[['price','high','low']]
        print ['----','----' ,'----','----','-----']
        print [price,'|',percent,'|',high,'|',low,'|',timee]
        time.sleep(10)
        r=[]
def price_pre_parall(h1,h2,tr1,l1,tr2):
    #h1 is high one h2 is high two tr1 is timerange between h1 and h2
    #l1 is low one you predicted is l2 tr2 is timerange between l1 and l2
    k = float((h1-h2)/(tr1-1))
    l2 = l1-k*(tr2-1)
    return l2
    
    
    
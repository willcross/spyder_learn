# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 01:05:40 2019
 
@author: Administrator
"""
from dianshutu_v7 import *
def plot_tdx_data(code,kaishihang):
#filename = r'E:\tdx\T0002\export\002359.xls'
#filename = r'D:\learning material\make_rice\pnf code\999999.xls'
#filename = r'E:\tdx\T0002\export\603713.xls'
#filename = r'E:\tdx\T0002\export\RBL9.xls'
#filename = r'E:\tdx\T0002\export\880431.xls'
    filename = r"E:\tdx\T0002\export""\\"+code+r'.xls'
     
    kaishihang = 100
     
     
    f = open(filename, 'rb')
    lines = f.readlines()
    out = []
    high = []
    low =[]
    counter= 0
    for line in lines:
        counter = counter+1
        if counter>=5:
            hehe = line.split('\t')
            if len(hehe)>4  :
                high.append(float(hehe[2]))
                low.append(float(hehe[3]))
                 
    f.close()  
    high = high[kaishihang:]
    low = low[kaishihang:]
    maxx = max(high)
    minn = min(low)
    if maxx<=5:
        step = 0.25
    elif maxx<=20:
        step = 0.5
    elif maxx<=100:
        step = 1
    elif maxx<=200:
        step = 2
    elif maxx<=500:
        step = 4
    elif maxx<=1000:
        step = 5
    elif maxx<=25000:
        step = 50
    else:
        step = 500
    lower = round(minn)-step
    upper = round(maxx)+step
    ruler = arange(lower,upper,step)
    #ruler = arange(5,20,0.5)
    plot_dianshutu(high,low,ruler)
if __name__=="main":
    plot_tdx_data('880472',100)
#plot_dianshutu(out[130:],arange(4,20,0.5))
#plot_dianshutu(high[kaishihang:],low[kaishihang:],arange(2000,4000,25))
#plot_dianshutu(out[kaishihang:],arange(20,60,1))
#plot_dianshutu(high[kaishihang:],low[kaishihang:],arange(3000,5000,50))
#plot_dianshutu(high[kaishihang:],low[kaishihang:],arange(300,900,5))
#plot_dianshutu(high[kaishihang:],low[kaishihang:],arange(5,24,.5))
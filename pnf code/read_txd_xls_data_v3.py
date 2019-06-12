# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 01:05:40 2019

@author: Administrator
"""


#filename = r'E:\tdx\T0002\export\002359.xls'
filename = r'D:\learning material\make_rice\pnf code\999999.xls'
#filename = r'E:\tdx\T0002\export\603713.xls'
kaishihang = 20
from dianshutu_v6 import *

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


#plot_dianshutu(out[130:],arange(4,20,0.5))
plot_dianshutu(high[kaishihang:],low[kaishihang:],arange(2000,4000,50))
#plot_dianshutu(out[kaishihang:],arange(20,60,1))
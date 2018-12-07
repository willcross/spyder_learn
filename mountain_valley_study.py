# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:55:48 2018

@author: WeicZhang
"""

import tushare as ts
import numpy as np
import matplotlib.pyplot as plt
def peak_high(list):
    out=[]
    index=[]
    for i in range(0,len(list)-2):
        if list[i+1]>=list[i] and list[i+1]>=list[i+2]:
            out.append(list[i+1])
            index.append(i+1)
    return out, index 
def fractal_law(a,b):
    length = abs(b-a)
    if a<b:
         a1 = a+length*2/3.0
         b1 = b-length*2/3.0
    else:
         a1 = a-length*2/3.0
         b1 = b+length*2/3.0
    return [a,a1,b1,b]
def use_law(list1):
    n =len(list1)
    out=[0]*(3*n-2)
    for i in range(0,n-1):
        temp = fractal_law(list1[i],list1[i+1])
        
        out[3*i]=list1[i]
        out[3*i+1]=temp[1]
        out[3*i+2]=temp[2]
        temp=[]
        #print out
    out[-1]=list1[-1]
    return out
a = use_law([100,1]);plt.plot(a)        
a = use_law(a);plt.plot(a)
def fractal_up(list1):
    #upward fractal
    out={}
    out['index']=[]
    out['value']=[]
    if len(list1)<5:
        raise ValueError('length should be greater than 4!')
    for i in xrange(len(list1)-5):
        if list1[i+2]>list1[i] and list1[i+2]>list1[i+1] and list1[i+2]>list1[i+3] and list1[i+2]>list1[i+4]:
            out['index'].append(i+2)
            out['value'].append(list1[i+2])
    return out        
def fractal_down(list1):
    #downward fractal
    out={}
    out['index']=[]
    out['value']=[]
    if len(list1)<5:
        raise ValueError('length should be greater than 4!')
    for i in xrange(len(list1)-5):
        if list1[i+2]<list1[i] and list1[i+2]<list1[i+1] and list1[i+2]<list1[i+3] and list1[i+2]<list1[i+4]:
            out['index'].append(i+2)
            out['value'].append(list1[i+2])       
    return out        
         
df = ts.get_hist_data('002359',start='2018-10-01',end='2018-12-05')
df = df.sort_index()
high = df[['high']].values
openn = df[['open']].values
low = df[['low']].values
close = df[['close']].values

#length = range(0,len(high))
length = np.arange(0,len(high))
plt.scatter(length,high,c='r',marker='*',alpha=1)
#plt.plot(length,low,c='k',marker='p')
peak1,index1 = peak_high(high)
plt.scatter(length[index1],peak1,c='b',marker='o',alpha=1)
plt.show()


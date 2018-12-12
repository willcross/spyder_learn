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
def wave_func(list1,fudu):
    # fudu is percent of rise or falls like 1%, 5%
    #rules: a. first or last b. it's a node c. rise/fall amplitude higher than given fudu
    
    index=[]
    value=[]
    temp=[]
    tempindex=[]
    for i in xrange(len(list1)):
        if i==0 or i==len(list1)-1:
            temp.append(list1[i])
            tempindex.append(i)
        elif (list1[i]==max((list1[i-1:i+2])) or -list1[i]== max(-(list1[i-1:i+2]))  ):
            temp.append(list1[i])
            tempindex.append(i)
    
    for i in xrange(len(temp)):
        if i==0 or i==len(temp)-1:
            index.append(tempindex[i])
            value.append(temp[i])
        elif abs(temp[i+1]- temp[i] )/temp[i]*100>fudu and  \
            (temp[i]==max((temp[i-1:i+2])) or temp[i]== min((temp[i-1:i+2]))  ):
            index.append(tempindex[i])
            value.append(temp[i])
    for i in xrange(len(value)):
        if i==0 or i==len(value)-1:
            pass
        elif (value[i]!=max((value[i-1:i+2])) or value[i]!= min((value[i-1:i+2]))  ):
            value.pop()
    return value,index

def wave_func2(list1,fudu):
    # fudu is percent of rise or falls like 1%, 5%
    #rules: a. first or last b. it's a node c. rise/fall amplitude higher than given fudu
    
    index=[]
    out=[]
   
    pivot = list1[0]
    index.append(0)
    out.append(pivot)
    last_pivot_id = 0
    up_down = 0
  
    for i in range(1,len(list1)):
        data = list1[i]
        # We don't have a trend yet
        if up_down == 0:
            if data < pivot*(1-fudu/100.0):
                out.append(pivot)
                index.append(last_pivot_id)
                
                pivot, last_pivot_id = data, i
                
                up_down = -1
            elif data > pivot *(1+fudu/100.0):
                out.append(pivot)
                index.append(last_pivot_id)
                pivot, last_pivot_id = data, i
                
                up_down = 1

        # Current trend is up
        elif up_down == 1:
            # If got higher than last pivot, update the swing
            if data > pivot :
                # Remove the last pivot, as it wasn't a real one
               
                pivot, last_pivot_id = data, i
            elif data < pivot  *(1-fudu/100.0):
                out.append(pivot)
                index.append(last_pivot_id)
                pivot, last_pivot_id = data, i
                up_down = -1

        # Current trend is down
        elif up_down == -1:
             # If got lower than last pivot, update the swing
            if data < pivot:
                # Remove the last pivot, as it wasn't a real one
              
                pivot, last_pivot_id = data, i
            elif data > pivot*(1+fudu/100.0):
                out.append(pivot)
                index.append(last_pivot_id)
                pivot, last_pivot_id = data, i
                # Change the trend indicator
                up_down = 1
    index.append(i)
    out.append(list1[-1])
    return index,out

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

value,index = wave_func(close,1)
plt.scatter(length[index],value,c='c',marker='o',alpha=1)

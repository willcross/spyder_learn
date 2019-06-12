# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:39:38 2019

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:20:46 2019

@author: WeicZhang
"""

import tushare as ts
from dianshutu_v7 import *
import sys
def print_pnf(code,stepp=None):
    df = ts.get_hist_data(code)
    dff = df.sort_index(ascending=True)
    high = dff['high'].values.tolist()
    low = dff['low'].values.tolist()
    
    #high.reverse()
    #low.reverse()
    #high = high[378:]
    #low = low[378:]
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
    #lower = round(minn)-step
    #upper = round(maxx)+step
    
    if stepp==None:
        pass
    else:
        step = stepp
    lower = (round(minn/step)-2)*step
    upper = (round(maxx/step)+2)*step
    ruler = arange(lower,upper,step)
    #ruler = arange(5,20,0.5)
    plot_dianshutu(high,low,ruler)
if __name__=="main":
    print_pnf('002359')


'''
1-5   0.25
5-20   0.5
20-100  1
100-200 2
200-500 4
500-1000 5
1000-25000 50
25000-infi  500  
'''
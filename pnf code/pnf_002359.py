# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:20:46 2019

@author: WeicZhang
"""

import tushare as ts
from dianshutu_v6 import *

df = ts.get_hist_data('002359')
high = df['high'].values.tolist()
low = df['low'].values.tolist()

high.reverse()
low.reverse()
#high = high[308:]
#low = low[308:]
ruler = arange(5,20,0.5)
plot_dianshutu(high[384:],low[384:],ruler)

#plot_dianshutu(high[500:520],low[500:520],ruler)

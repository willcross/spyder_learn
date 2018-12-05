# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:40:05 2018

@author: WeicZhang
"""

import numpy as np
import pandas as pd
import tushare as ts
import h5py
import itertools
import datetime
codes=['002216']
def get_all_code():
    hehe = ts.get_stock_basics()
    hoho = hehe[(hehe.timeToMarket<20170901)&(hehe.timeToMarket>0)]
    codes = hoho.index.tolist()
    return codes


def hdf5_file_init():
    codes = get_all_code()
    f = h5py.File('stocks.h5')
    for i in codes:
        grp = f.create_group(i)
        df  = ts.get_k_data(i)
        times = df[['date']].values.tolist()
        times = list(itertools.chain.from_iterable(times))
        times = [a.encode('unicode-escape').decode('string_escape') for a in times]
        price = df[['open','close','high','low','volume']].values
        #dset1 = grp.create_dataset('timestamp',(len(times),),maxshape=(None,))
        dset1 = grp.create_dataset('timestamp',data=times,maxshape=(None,))
        #dset1[:,] = times
        #dset2 = grp.create_dataset('price',price.shape,maxshape=(None,None))
        dset2 = grp.create_dataset('price',data = price,maxshape=(None,None))
        #dset2[:,:]=price
    f.close()
def hdf5_clear_groups():
    f = h5py.File('stocks.h5')
    for i in f.keys():
        del f[i]
    f.close()
def hdf5_maintain():
    f = h5py.File('stocks.h5')
    for i in f.keys():
        ddd = f[i]['timestamp'].value[-1].split('-')
        oldtime = datetime.datetime(int(ddd[0]),int(ddd[1]),int(ddd[2]))
        todaytime = datetime.datetime.now()
        todaytime_str = todaytime.strftime('%Y-%m-%d')
        oldtime_str = oldtime.strftime('%Y-%m-%d')
        if (todaytime-oldtime).days>0:
            df = ts.get_k_data(i,start = oldtime_str,end =todaytime_str )
            increased_days = list(df.shape)[0]
            dddd = df.date.values[-1].split('-')
            new_start_date = datetime.datetime(int(dddd[0]),int(dddd[1]),int(dddd[2]))
            k_data_returned_increased_days = (new_start_date-oldtime).days
            if increased_days>1 and k_data_returned_increased_days>0:
                shape_time = list(f[i]['timestamp'].shape)
                shape_price = list(f[i]['price'].shape)
                str1 = '('+str(shape_time[0]+increased_days-1)+',)'
                str2 = '('+str(shape_price[0]+increased_days-1)+','+str(shape_price[1])+')'
                tuple1 = eval(str1)
                tuple2 = eval(str2)
                f[i]['timestamp'].resize(tuple1)
                f[i]['price'].resize(tuple2)
                times = df[['date']].values.tolist()
                times = list(itertools.chain.from_iterable(times))
                times = [a.encode('unicode-escape').decode('string_escape') for a in times]
                price = df[['open','close','high','low','volume']].values
                f[i]['timestamp'][-increased_days+1:]=times[1:]
                f[i]['price'][-increased_days+1:,:]=price[1:,:]
    f.close()        
def hdf5_read_data():
    f = h5py.File('stocks.h5')
    for i in f.keys():
        data = f[i]['price'].value


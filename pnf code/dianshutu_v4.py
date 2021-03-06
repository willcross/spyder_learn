
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:02:40 2019
this version, use high low method to plot, consider high bull, low bull, high-low convert conditions
@author: Will
"""
def plot_dianshutu(close,low,ruler):
    import matplotlib.pyplot as plt
    out = dianshutu(close,low,ruler)
    x,y = produce_xyaxis(out)
    plt.figure()   
    plt.grid()
    plt.scatter(x,y,marker='o')
    plt.yticks(ruler)
    plt.xticks(x)
def dianshutu(high,low,rulers):
    closess = high_to_rulers(high,rulers)# return closes is same as highh
    loww = low_to_rulers(low,rulers)
    first_value=closess[0]
    temp=[]
    #temp.append(first_value)
    out=[]
    #column = 0
    bull_former = True
    bull_current = None
    length_c = len(closess)
    for i in range(1,length_c):
        if closess[i]<=closess[i-1] and loww[i]>=loww[i-1]:
            pass
        else:
            if closess[i]>closess[i-1]:
                bull_current = True
            elif loww[i]<loww[i-1]:
                bull_current  =False
            if bull_current==bull_former:
                if bull_current == True:
                    temp.extend(high_low_converse(closess[i-1],closess[i],rulers))
                else:
                    temp.extend(high_low_converse(loww[i-1],loww[i],rulers))
                
            elif len(temp)<2 and bull_current==True: 
                temp.extend(high_low_converse(loww[i-1],closess[i],rulers))
            elif len(temp)<2 and bull_current==False:
                temp.extend(high_low_converse(closess[i-1],loww[i],rulers))
                #temp.append(loww[i])
            else:
                out.append(temp)
                temp=[]
                if bull_current==True:
                    temp.extend(high_low_converse(loww[i-1],closess[i],rulers))
                    #temp.append(closess[i])
                else:
                    temp.extend(high_low_converse(closess[i-1],loww[i],rulers))
                    #temp.append(loww[i])
            bull_former = bull_current
    out.append(temp)
    return out
                
def produce_xyaxis(inn):
    out = []
    index = 0
    
    for i in inn:
        temp = []
        for j in i:
            temp.append(index)
        index+=1
        out.append(temp)                            
    x = []
    y = []
    for _ in out:
        x += _
    for __ in inn:
        y += __
    return x,y
    
    
    
    
    
    
#    length_r = len(rulers)
#    temp=[]
#    qishidian,ii = rulerlocation(closes[0],rulers)
#    temp.append(qishidian)
#    for i in range(1,length_c):
#        if closes[i]>=closes[i-1]:
#            pass
           
           
def highrulerlocation(x,rulers):
    #this function input is close, and ruler list, return is close in the middle of rulers
    length=len(rulers)
    for i in range(1,length):
        if x>rulers[i-1] and x<=rulers[i]:
            #return rulers[i]/2.0+rulers[i-1]/2.0
            return rulers[i-1]
def lowrulerlocation(x,rulers):
    length=len(rulers)
    for i in range(1,length):
        if x>rulers[i-1] and x<=rulers[i]:
            #return rulers[i]/2.0+rulers[i-1]/2.0
            return rulers[i]
def high_low_converse(former,later,rulers):
    out = []
    step = rulers[1]-rulers[0]
    if former>later:
        for j in range(0,int((former-later)/step)):
                out.append(former-step*(j+1))
    else:
        for k in range(0,int((later-former)/step)):
                out.append(former+step*(k+1))
    return out
                
def high_to_rulers(highs,rulers):
    out=[]
    for i in highs:
        out.append(highrulerlocation(i,rulers))  
    # if step offset larger than 0.5, fill them full
    
    return out
def low_to_rulers(lows,rulers):
    out=[]
    for i in lows:
        out.append(lowrulerlocation(i,rulers))  
    # if step offset larger than 0.5, fill them full
    
    return out
def rulerindex(rulers):
    # this function return the 1/2 limits value list
    out=[]
    length=len(rulers)
    for i in range(1,length):
        out.append(rulers[i]/2.0+rulers[i-1]/2.0)
    return out

def arange(start,stop,step):
    out=[]
    out.append(start)
    temp=start
    while True:
        temp = temp +step
        if temp<=stop:
            out.append(temp)
        else:
            break
    return out



        
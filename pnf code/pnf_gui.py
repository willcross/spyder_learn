# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:53:34 2019

@author: WeicZhang
"""
'''
from Tkinter import *

root = Tk()
one = Label(root, text='one', width=30, height=5,bg="white", font=("Arial", 500))
one.pack()



root.mainloop()


#!/usr/bin/python
# -*- coding:utf-8 -*-

from tkinter import *
import time

num=0

tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()
itext=canvas.create_text(30,30,text=str(num))
while num<7:
	num +=1
	canvas.itemconfig(itext,text=str(num))
	canvas.insert(itext,12,'')
	tk.update()
	print('num=%d'%num)
	tk.after(1000)
'''
import Tkinter as tk
from tkinter.filedialog import askopenfilename
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("威科夫点数图工具v1.0    作者微博 【威科夫指标-点数图】 微信 【canbeshine】")
        #self.root.geometry("940x250")
#        ws = self.root.winfo_screenwidth() # width of the screen
#        hs = self.root.winfo_screenheight() # height of the screen
#        
#        # calculate x and y coordinates for the Tk root window
#        x = (ws/2) - (940/2)
#        y = (hs/2) - (250/2)
#        self.root.geometry('%dx%d+%d+%d' % (940, 250, x, y))
#        
#        self.root.resizable(0,0)
#        self.label = tk.Label(self.root,text="作者微信 canbeshine",width=20, height=5,bg="white", font=("Arial", 20,'bold'))
#        self.label.pack(fill="both", expand=True)
##        self.update_clock(time.clock())
#        self.root.mainloop()
        tk.Label(self.root, text = "步骤一 载入数据：").grid(row = 0, column = 0)
        tk.Label(self.root, text = "方式一 输入品种代码：").grid(row = 0, column = 1)
        tk.Label(self.root, text = "或者").grid(row = 0, column = 2)
        tk.Label(self.root, text = "方式二 载入离线数据").grid(row = 0, column = 3)
       
        tk.Label(self.root, text = "步骤二 输入价格间距").grid(row = 2, column = 0) 
        
        
        self.e1 = tk.Entry(self.root)#stock number
        self.e2 = tk.Entry(self.root)#price step
        
        self.e1.grid(row = 1, column = 1, padx = 10, pady = 5)
        self.e2.grid(row = 2, column = 1, padx = 10, pady = 5)
        
        tk.Label(self.root, text = "步骤三  点击 ‘画图’ 按钮").grid(row = 3, column = 0)
        
 

        self.path = ''
        self.code = ''
        tk.Button(self.root, text = "载入数据", width = 10, command = self.load_data)\
                        .grid(row = 1, column = 3, sticky = "w", padx = 10, pady = 5)
        tk.Button(self.root, text = "画图", width = 10, command = self.show)\
                        .grid(row = 3, column = 1, sticky = "e", padx = 10, pady = 5)  #退出就直接调用窗口的 quit() 方法 
        self.root.mainloop()
    def load_data(self):
        try:
            path = self.path.split('/')
            pathnew=[]
            for i in range(len(path)-1):
                pathnew.append(path[i]+'/')
            self.path = askopenfilename(initialdir=pathnew)
        except:
            self.path = askopenfilename()
        print(self.path)
    def show(self):
        self.code = self.e1.get()
        self.step = self.e2.get()
        print(r"code %s" % self.code)
        print(r"step %s" % self.step)
        print(self.path)
        self.e1.delete(0, "end")
        self.e2.delete(0, "end")


if __name__=="__main__":
        app=App()
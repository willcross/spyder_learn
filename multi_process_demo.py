# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 16:01:39 2018

@author: WeicZhang
"""

#from multiprocessing import Process
#import os
# 
## 子进程要执行的代码
#def run_proc(name):
#  print('Run child process %s (%s)...' % (name, os.getpid()))
# 
#if __name__=='__main__':
#  print('Parent process %s.' % os.getpid())
#  p = Process(target=run_proc, args=('test',))
#  print('Child process will start.')
#  p.start()
#  p.terminate()
#  
#  print('Child process end.')

#from multiprocessing import Pool
#import os, time, random
#import h5py
#f=h5py.File('m_process.h5')
# 
#def long_time_task(name):
#    f.create_group(str(name))
#    print('group %s is created' % name)
#    time.sleep(random.random() * 3)
##  print('Run task %s (%s)...' % (name, os.getpid()))
##  start = time.time()
##  time.sleep(random.random() * 3)
##  end = time.time()
##  print('Task %s runs %0.2f seconds.' % (name, (end - start)))
# 
#if __name__=='__main__':
#  print('Parent process %s.' % os.getpid())
#  p = Pool(4)
#  for i in range(5):
#    p.apply_async(long_time_task, args=(i,))
#  print('Waiting for all subprocesses done...')
#  p.close()
#  p.join()
#  f.close()
#  print('All subprocesses done.')
#  time.sleep(10)



#from multiprocessing import Process
#import time
# 
#def fun1(t):
# print 'this is fun1',time.ctime()
# time.sleep(t)
# print 'fun1 finish',time.ctime()
# 
#def fun2(t):
# print 'this is fun2',time.ctime()
# time.sleep(t)
# print 'fun2 finish',time.ctime()
# time.sleep(3)
# 
#if __name__ == '__main__':
# a=time.time()
# p1=Process(target=fun1,args=(4,))
# p2 = Process(target=fun2, args=(6,))
# p1.start()
# p2.start()
# p1.join()
# p2.join()
# b=time.time()
# print 'finish',b-a
# time.sleep(2)

#
#from multiprocessing import Process, Queue
#import os, time, random
# 
## 写数据进程执行的代码:
#def write(q,listt):
#  print('Process to write: %s' % os.getpid())
#  for value in listt:
#    print('Put %s to queue...' % value)
#    q.put(value)
#    time.sleep(random.random())
# 
## 读数据进程执行的代码:
#def read(q):
#  print('Process to read: %s' % os.getpid())
#  while True:
#    value = q.get(True)
#    print('Get %s from queue.' % value)
# 
#if __name__=='__main__':
#  # 父进程创建Queue，并传给各个子进程：
#  q = Queue()
#  pw = Process(target=write, args=(q,['A', 'B', 'C']))
#  pw2 = Process(target=write, args=(q,['d','e','f']))
#  pr = Process(target=read, args=(q,))
#  # 启动子进程pw，写入:
#  pw.start()
#  pw2.start()
#  # 启动子进程pr，读取:
#  pr.start()
#  # 等待pw结束:
#  pw.join()
#  pw2.join()
#  # pr进程里是死循环，无法等待其结束，只能强行终止:
#  time.sleep(10)
#  pr.terminate()


import h5py
from multiprocessing import Pool #导入进程池
import datetime,time

 
def mycallback(x):
    print(x)
    f.create_group(x)  
 
def sayHi(num):
    w = str(num)
    return w
    
if __name__ == '__main__':
    e1 = datetime.datetime.now()
    f = h5py.File('haha.h5')
    for i in range(10):
        f.create_group(str(i))
#    p = Pool(4)
#    
#    for i in range(10):
#        p.apply_async(sayHi, (i,),callback=mycallback)#sayHi是我们进程运行的对象，callback=mycallback这里是当
#    p.close()
#    p.join()
    e2 = datetime.datetime.now()
    print((e2-e1)) 
    time.sleep(10)
    f.close() 
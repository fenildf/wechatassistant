# _*_ coding=utf8
'''
测试多线程效率
'''
import requests
import time
import threading
#from multiprocessing import Process
import os
#import thread

def count(x, y):
    # 使程序完成150万计算
    c = 0
    while c < 500000:
        c += 1
        x += x
        y += y
        
def write(threadname):
    f = open("test.txt", "a")
    for x in range(500):
        f.write(str(threadname))
        f.write(" line:" +str(x) +" :testwrite\n")
    f.close()

def read():
    f = open("test.txt", "r")
    lines = f.readlines()
    f.close()

'''
# CPU密集操作
t = time.time()
for x in range(10):
    count(1, 1)
print("Line cpu", time.time() - t)


# IO密集操作
t = time.time()
for x in range(10):
    write()
    read()
print("Line IO", time.time() - t)

    
#测试多线程并发执行CPU密集操作所需时间
counts = []
t = time.time()
for x in range(10):
    thread = Thread(target=count, args=(1,1))
    counts.append(thread)
    thread.start()

for x in range(10):
    print(counts[x])

e = len(counts)
while True:
    for th in counts:
        if not th.is_alive():
            e -= 1
    if e <= 0:
        break
print(time.time() - t)
'''

#测试多线程并发执行IO密集操作所需时间
def io():
    write()
    read()

t = time.time()
ios = []
for x in range(10):
    threadr = threading.Thread(target=write,args=('threadryan'+str(x),))
    #thread.start_new_thread('threadryan.' +str(x))
    ios.append(threadr)
    threadr.start()

e = ios.__len__()
while True:
    for th in ios:
        if not th.is_alive():
            e -= 1
    if e <= 0:
        break
print(time.time() - t)
# -*- encoding: utf-8 -*-
'''
@File : 8_4.py
@Time : 2020/05/01 01:38:10
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
    编写一个简单的聊天程序；
    其中一个进程发送文字聊天消息（从键盘输入文字消息）；  
    另外一个进程接收并打印消息
'''

# here put the import lib
from multiprocessing import Process, Queue
import os
import time


def write(q):
    print("键入: \eixt 可以退出输入进程")
    message = input('>>')
    try:
        while message != '\exit':
            q.put(message)
            time.sleep(0.5)
            message = input('>>')
        print('您已退出输入进程')
        print("60s后输出进程将自动终结,也可以通过键击 ctrl + c 强行终止")
        exit(0)
    except Exception as e:
        print(type(e), e)


def read(q):
    try:
        while True:
            value = q.get(timeout=60)
            print('-->', value)
            time.sleep(0.5)
    except:
        print("长时间未输入,结束输出进程")
        exit(0)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=read, args=(q,))
    pw.start()
    # 每次把这个写入函数包装成一个子进程
    # 它都不响应,整程序卡死......
    # 调试发现这个进行处于stoped状态
    # 不明所以!!!
    write(q)  # 所以把写函数放到了主进程里

    pr = Process(target=read, args=(q,))
    pr.start()

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 8_1.py
@Time : 2020/4/27 16:16:19 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
有100个同学的分数：数据请用随机函数生成；
A 利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；

B 利用线程池来实现；
"""
import random
import threading
from concurrent.futures import ThreadPoolExecutor
import time


def num():
    for i in range(20):
        x = random.randint(0, 100)
        print(x)


def multithread():
    for i in range(5):
        threading.Thread(target=num).start()


def threadpool():
    executor = ThreadPoolExecutor(max_workers=5)
    # 通过submit函数提交执行的函数到线程池中，submit函数立即返回，不阻塞
    for i in range(5):
        executor.submit(num)


if __name__ == "__main__":
    # 多线程
    multithread()
    time.sleep(10)
    # 线程池
    threadpool()

    time.sleep(5)

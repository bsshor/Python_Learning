# -*- encoding: utf-8 -*-
'''
@File : 8_3.py
@Time : 2020/04/30 08:16:08
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
    多进程练习：
计算1～100000之间所有素数的个数， 要求如下:
- 编写函数判断一个数字是否为素数，然后统计素数的个数；
-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
-对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
'''
# here put the import lib
from multiprocessing import Process, Pool, Queue
import multiprocessing
import time
import math


def is_prime(num):
    """
    判断素数
    """
    if num <= 1:
        return False
    i = 2
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def single_process(start, end):
    size = 0
    for i in range(start, end + 1):
        if is_prime(i):
            size += 1
    # print("%d~%d之间的质数共有%d个"%(a,b,size))

def multi_process(count):
    li = []
    for i in range(1, count + 1):
        li.append(Process(target=single_process, args=(
            ((int(100000/count))*(i-1)), ((int(100000/count)))*i)))
        li[-1].start()
        # li[-1].join()

if __name__ == '__main__':
    s2 = time.time()

    s0 = time.time()
    print("------------------4进程------------------")
    multi_process(4)
    e0 = time.time()
    print('4进程:', e0 - s0)  # 0.06s左右

    s10 = time.time()
    print("------------------10进程------------------")
    multi_process(10)
    e10 = time.time()
    print('10进程:', e10 - s10)  # 0.15~0.21秒间

    print("------------------单进程------------------")
    s1 = time.time()
    single_process(1, 100000)
    e1 = time.time()
    print('单进程(不使用多进程):', e1 - s1)  # 0.2s左右

    e2 = time.time()
    print('全程:', e2 - s2)

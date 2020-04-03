#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 4_1.py
@Time : 2020/3/27 23:38:31 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入
和头部插入并记录程序运行的时间；
用deque来实现，同样记录程序所耗费的时间；
输出这2个时间的差值；
提示：
列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
"""
import datetime
import time
from collections import deque

# 列表
li = [i for i in range(2, 12)]
# 此处进行操作
start = datetime.datetime.now()
# print(start)
li.insert(0, 0)
li.append(11)

end = datetime.datetime.now()
# print(end)
runtime_list = (end - start).total_seconds()

print("列表首尾插入耗时:", runtime_list, 's')
# 队列


# 此处进行操作
q = deque(['颠倒是非', '奥德赛', '的发v收到'])
start = time.time()
# print(start)
q.append('x')
q.appendleft('y')

# end = time.time()
print(end)
runtime_deque = end - start
print("deque首尾插入耗时:", runtime_deque, 's')

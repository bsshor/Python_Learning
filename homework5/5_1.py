# -*- encoding: utf-8 -*-
'''
@File : 5_1.py
@Time : 2020/04/08 00:47:50
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
    编写一个装饰器，能计算其他函数的运行时间
'''

# here put the import lib

# -*- encoding: utf-8 -*-
'''
@File : 5_1.py
@Time : 2020/04/08 00:49:37
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
    
'''

# here put the import lib


import time
def outer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("函数运行时间为%.3fs" % (end - start))

    return wrapper


# 使用示例
# @outer
# def add(a, b):
#     print(a + b)

# add(234560, 362)

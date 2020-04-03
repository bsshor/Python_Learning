"""
使用random模块，生成随机数，来初始化一个列表，元组；
使用了 random 模块的 randint() 函数来生成随机数，
查询一下相关函数的用法；
"""
# -*- encoding: utf-8 -*-
'''
@File : 1_5.py
@Time : 2020/03/04 23:00:23
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''

# here put the import lib
import random

a1 = [random.randint(1, 11), random.randint(1, 11)]
print(a1)

a2 = (random.randint(1, 23), random.randint(4, 44))
print(a2)

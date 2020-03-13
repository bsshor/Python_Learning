"""
打印输出九九乘法表
"""
# -*- encoding: utf-8 -*-
'''
@File : 1_7.py
@Time : 2020/03/04 20:40:02
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''

# here put the import lib
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(j, '*', i, '=', i*j, end='\t\t')
        j += 1
    print('\n')
    i += 1

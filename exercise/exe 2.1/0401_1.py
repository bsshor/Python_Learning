# -*- encoding: utf-8 -*-
'''
@File : 0401_1.py
@Time : 2020/04/01 08:36:31
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''

# here put the import lib
"""
定义一个高阶函数, 实现加,减,乘,除计算器功能
"""


def add(a, b):
    return a+b


def jian(a, b):
    return a - b


def cheng(a, b):
    return a*b


def chu(a, b):
    return a/b


def calculator(a, b):
    print(a, '+', b, '=', add(a, b))
    print(a, '-', b, '=', jian(a, b))
    print(a, '*', b, '=', cheng(a, b))
    print(a, '/', b, '=', chu(a, b))


if __name__ == "__main__":
    calculator(3, 5)

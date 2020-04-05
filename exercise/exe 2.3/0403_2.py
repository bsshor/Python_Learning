# -*- encoding: utf-8 -*-
'''
@File : 0403_2.py
@Time : 2020/04/03 21:59:29
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''

# here put the import lib
"""
练习:  定义一个函数, 做2个数的加法;  
然后我们定义一个装饰器, 对原函数记录运行日志;
日志的内容,随便定义: "加法被执行了"

"""


def outer(func):
    def wrapper(*args):
        print("加法被执行了")
        func(*args)

    return wrapper


@outer
def add(x, z):
    print(x+z)


add(1, 6)


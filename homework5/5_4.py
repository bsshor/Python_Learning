# -*- encoding: utf-8 -*-
'''
@File : 5_4.py
@Time : 2020/04/08 00:48:26
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
    编写装饰器来实现，对目标函数进行装饰，
分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
三个目标函数分别为：
​ A 打印输出20000之内的素数；
​ B 计算整数2-10000之间的素数的个数；
​ C 计算整数2-M之间的素数的个数；
'''

# here put the import lib
import math


def outer(func):
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        return result
    return wrapper


@outer
def A():
    for n in range(2, 20001):
        if n == 2:
            print(n)
        else:
            for i in range(2, n):
                if n % i == 0:
                    break
                if i == n-1:
                    print(n)


A()


@outer
def B():
    num = 0
    for n in range(2, 10001):

        if n == 2:
            num += 1
        else:
            for i in range(2, n):
                if n % i == 0:
                    break
                if i == n-1:
                    num += 1
    return num

# print(B())


@outer
def C(x):
    num = 0
    for n in range(2, x):

        if n == 2:
            num += 1
        else:
            for i in range(2, n):
                if n % i == 0:
                    break
                if i == n-1:
                    num += 1
    return num

# print(C(10000))

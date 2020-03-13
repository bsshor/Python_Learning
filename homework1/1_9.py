"""
设计一个猜数字 游戏；
最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；
"""
# -*- encoding: utf-8 -*-
'''
@File : 1_9.py
@Time : 2020/03/04 23:02:48
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''

# here put the import lib


import random

N = int(input ("请输入猜测次数:"))
num = random.randint(0, 213)
i = 0
result = False
while i < N:
    x = int(input("请输入您猜的数字："))
    i += 1
    if x > num:
        print("您给的数大了")
    elif x < num:
        print("您给的数小了")
    else:
        print("恭喜您猜对了")
        result = True
        break
if not result:
    print("很遗憾，您的挑战机会已用尽，挑战失败")
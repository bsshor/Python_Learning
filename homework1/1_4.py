"""
判断用户输入的年份是否为闰年
"""
# -*- encoding: utf-8 -*-
'''
@File : 1_4.py
@Time : 2020/03/04 21:43:33
@Author :  Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''

# here put the import lib

year = int(input("请您任意输入一个年份："))

# 闰年分为普通闰年和世纪闰年，需要分别处理
if year % 100 == 0:  # 如果能被100整除，则是世纪年，按世纪闰年来判断
    if year % 400 == 0:
        print(year, "是闰年")
    else:
        print(year, "是平年")

elif year % 4 == 0:  # 不能被100整除的是普通年，按普通闰年的方法来判断
    print(year, "是闰年")
else:
    print(year, "是平年")

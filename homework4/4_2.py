#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 4_2.py
@Time : 2020/3/27 23:38:47 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
定义一个函数，判断一个输入的日期，是当年的第几周，周几？
将程序改写一下，
能针对我们学校的校历时间进行计算
（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）
"""
print(
"""本程序仅用于判断2020年上学期校历进程
从第1周至第27周(2020.2.17 --- 2020.8.23)
"""
)
month = input("请输入月份:")
day = input("请输入日子:")
week = ['星期日','星期一','星期二','星期三','星期四','星期五','星期六']
data = {'2': 29,    
        '3': 31,    
        '4': 30,    
        '5': 31,    
        '6': 30,    
        '7': 31,    
        '8': 31,    
}
days = 0
for i in '2345678':
    if i == month[-1]:
        break
    days += data[i]
days = days - 16 + int(day)
# print(days)

b = days % 7
if b != 0 :
    a = days // 7 + 1
else:
    a = days // 7 

print("当前是第{}周{}".format(a,week[b]))


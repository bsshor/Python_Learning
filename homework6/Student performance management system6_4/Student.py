#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : Student.py
@Time : 2020/4/11 00:55:27 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
Python学生成绩管理系统
"""
import pandas as pd
data = pd.read_csv(r'homework6\Student performance management system6_4\Python_Score.csv')
print('---------------------------------------------------')
print(data)
print('---------------------------------------------------')


df2 = data[['班级','学号','姓名','Python分数']][data['姓名']  == '从宾白']
print(df2)
print('---------------------------------------------------')

# 删除含关键字的行
y=data[data['姓名'].str.contains('姓名')]  #显示出标题行
print(y)
print('---------------------------------------------------')
# df.drop(df.index[[2913]],inplace=True)
# df = df.to_csv("/Users/hey/Desktop/楼宇办公自动化_nohead.csv",index=0)

# 删除行
data.drop(data.index[40:],inplace=True)
print(data)
data.to_csv(r'homework6\Student performance management system6_4\Python_Score.csv')

"""
软件1802,20181180216,闻飞星,38
软件1802,20181180217,蒙羽,67
软件1802,20181180218,谷斯玉,79
软件1802,20181180219,池玲琅,78
软件1802,20181180220,叶若芳,100
软件1802,20181180221,武哲,89
软件1802,20181180222,温寄翠,95
"""
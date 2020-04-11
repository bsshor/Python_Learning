#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : Student6_4.py
@Time : 2020/4/10 18:18:04 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
封装方法，求单个学生的总分，平均分，以及打印学生的信息。
"""


class Student:
    def __init__(self):
        self.name = None
        self.age = None
        self.gender = None
        self.English = None
        self.mathematics = None
        self.Chinese = None

    def show(self):
        print('姓名：%s，年龄：%s，性别：%s' % (self.name, self.age, self.gender))
        print('%s的总成绩是：%.2s' % (
            self.name, self.English + self.mathematics + self.Chinese))
        print('%s的平均分是：%.2s' % (
            self.name, (self.English + self.mathematics + self.Chinese) / 3))


stu1 = Student()
# 信息初始化
stu1.name = input('请输入姓名：')
stu1.age = input('请输入年龄：')
stu1.gender = input('请输入性别：')
stu1.English = float(input('请输入英语成绩：'))
stu1.mathematics = float(input('请输入数学成绩：'))
stu1.Chinese = float(input('请输入语文成绩 :'))

stu1.show()

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : Student6_2.py
@Time : 2020/4/10 14:23:06 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
定义一个学生Student类。
有下面的类属性：
    1 姓名 name
    2 年龄 age
    3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
类方法：
    1 获取学生的姓名：get_name() 返回类型:str
    2 获取学生的年龄：get_age() 返回类型:int
    3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下
"""
import random


class Student(object):
    name = None
    age = None
    score = {"语文": None, "数学": None, "英语": None}

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.score.values()
                   )


if __name__ == "__main__":
    stu1 = Student()
    # 初始化
    stu1.name = "学生A"
    stu1.age = random.randint(18, 25)
    stu1.score["语文"] = random.randint(0, 100)
    stu1.score["数学"] = random.randint(0, 100)
    stu1.score["英语"] = random.randint(0, 100)

    # 输出
    print("----------------------------------")
    print("姓名:", stu1.get_name())
    print("三科中的最高分:", stu1.get_course())

    stu2 = Student()
    # 初始化
    stu2.name = "学生B"
    stu2.age = random.randint(18, 25)
    stu2.score["语文"] = random.randint(0, 100)
    stu2.score["数学"] = random.randint(0, 100)
    stu2.score["英语"] = random.randint(0, 100)

    # 输出
    print("----------------------------------")
    print("姓名:", stu2.get_name())
    print("三科中的最高分:", stu2.get_course())

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : dog6_1.py
@Time : 2020/4/10 13:49:22 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
定义一个狗类
里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
"""
import random


class Dog(object):
    dogs = [{"拉布拉多": ["金色", 332, 1000]}, {"藏獒": ["黑色", 34, 3232]}, {"雪纳瑞": ["白色", 48, 566]}]

    def sale(self):
        """
        "自动"卖狗
        :return:
        """
        if self.dogs[0]["拉布拉多"][1] > 0:  # 如果这种犬还有余量,就继续交易
            self.dogs[0]["拉布拉多"][1] -= random.randint(0, self.dogs[0]["拉布拉多"][1])
        if self.dogs[1]["藏獒"][1] > 0:  # 如果这种犬还有余量,就继续交易
            self.dogs[1]["藏獒"][1] -= random.randint(0, self.dogs[1]["藏獒"][1])
        if self.dogs[2]["雪纳瑞"][1] > 0:  # 如果这种犬还有余量,就继续交易
            self.dogs[2]["雪纳瑞"][1] -= random.randint(0, self.dogs[2]["雪纳瑞"][1])

    def show(self):
        """
        输出余量
        :return:
        """
        print('------------------------犬余量------------------------')
        print("%s还有%d只" % ("拉布拉多", self.dogs[0]["拉布拉多"][1]))
        print("%s还有%d只" % ("藏獒", self.dogs[1]["藏獒"][1]))
        print("%s还有%d只" % ("雪纳瑞", self.dogs[2]["雪纳瑞"][1]))


dog = Dog()
dog.show()

dog.sale()
dog.show()

dog.sale()
dog.show()

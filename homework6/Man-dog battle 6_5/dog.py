#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : dog.py
@Time : 2020/4/10 21:24:27 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
狗
"""


class Dog(object):
    def __init__(self, name):
        self.name = name
        self.life = 80  # 初始生命力80
        self.attack = 15  # 初始攻击力15
        self.locked = 3



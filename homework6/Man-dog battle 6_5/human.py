#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : human.py
@Time : 2020/4/10 21:24:46 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
人
"""


class Human(object):
    def __init__(self, name):
        self.name = name
        self.life = 100  # 初始生命力了100
        self.attack = 10  # 初始攻击力10
        self.locked = 2

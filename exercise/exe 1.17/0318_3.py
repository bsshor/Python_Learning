"""
练习3:   一个文件内容的如下,请读取文件的内容, 并输出;
            姓名      学号      分数
            张三      101         78
            李四      102         87
            王五       103        83
"""
# -*- encoding: utf-8 -*-
'''
@File : 0318_3.py
@Time : 2020/03/18 09:29:16
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''
import os

with open("test3.txt", 'r', encoding='utf-8') as f:
    print(f.read())

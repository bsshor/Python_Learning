"""
一个字典中，存放了10个学生的学号（key）和分数（value）；
请筛选输出，大于80分的同学
（按照格式：学号：分数）
"""
# -*- encoding: utf-8 -*-
'''
@File : 1_2.py
@Time : 2020/03/04 22:57:45
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''

# here put the import lib
students = {1001: 89, 1002: 23, 1003: 78, 1004: 88, 1005: 76,
            1006: 99, 1007: 93, 1008: 85.5, 1009: 64.5, 1010: 88.5}
print("分数大于80的学生有：")
for id, score in students.items():
    if score > 80:
        print(id, ':', score)

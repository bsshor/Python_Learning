"""
给定一个字典,保存了5个同学的学号,姓名,年龄;使用pickle模块将数据对象保存到文件中去
"""
# -*- encoding: utf-8 -*-
'''
@File : 0318_4.py
@Time : 2020/03/18 09:45:38
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''
import pickle

dict = {
    '1': (1212, 'sdsd', 12),
    '2': (12, '史蒂芬森', 23),
    '3': (32, '水电费', 24),
    '4': (232, '是发大V', 34),
    '5': (22, "防守打法", 45)
}
with open('tmp.pk', 'wb') as f:
    pickle.dump(dict, f)

with open('tmp.pk', 'rb') as f:
    data = pickle.load(f)
    print(data)

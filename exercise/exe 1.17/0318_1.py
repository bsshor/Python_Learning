"""
练习:  在window平台下练习os.path 相关方法的使用
"""
# -*- encoding: utf-8 -*-
'''
@File : 0318_1.py
@Time : 2020/03/18 08:30:45
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''

# here put the import lib
import os

path = os.getcwd()  # 返回当前工作目录
pwd = os.path.abspath('0304_1.py')
print(pwd)
print('1', path)
print("当前路径是否为绝对路径：", os.path.isabs(path))
print("当前路径是否为文件：", os.path.isfile(path))
print('2', os.path.basename(r'G:\Python_Learning\exercise\exe 1.17\0318_1.py'))  # 返回文件名
print('3', os.path.dirname(r'G:\Python_Learning\exercise\exe 1.17\0318_1.py'))  # 返回目录路径
print('4', os.getcwd())  # 返回当前工作目录
print('5', os.path.split(r'G:\Python_Learning\exercise\exe 1.17\0318_1.py'))  # 分割文件名与路径
print('6', os.path.join('G:', 'Python_Learning', 'exercise', 'exe 1.17', '0318_1.py'))  # 将目录和文件名合成一个路径
print('7', os.path.getsize(r'G:\Python_Learning\exercise\exe 1.17\0318_1.py'))  # 返回目录大小

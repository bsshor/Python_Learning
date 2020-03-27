"""
练习:  构造上述文件结构,分别在指定位置打开文件进行写入操作;
同级文件夹里面打开;
同级目录下的子目录里面打开;
上一级文件目录中的其他文件夹中打开
"""
# -*- encoding: utf-8 -*-
'''
@File : 0318_2.py
@Time : 2020/03/18 09:20:45
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''

# here put the import lib
# !/usr/bin/python3
import os

# 同级文件夹里打开一个文件
f = open("test.txt", "w")

f.write("在同级文件夹里打开一个文件\n做的很好!!\n")

# 关闭打开的文件
f.close()

# 同级目录下的子目录里面打开
os.mkdir('subdir')
with open(r'G:\Python_Learning\exercise\exe 1.17\subdir\readme.md', mode='w', encoding='utf-8') as f:
    f.write("子目录下打开")

# 上级目录的其他文件里打开文件
with open(r'G:\Python_Learning\exercise\exe 1.13\readme.md', mode='r+', encoding='utf-8') as f:
    print(f.readline())
    f.write("测试")

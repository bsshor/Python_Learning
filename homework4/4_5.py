#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 4_5.py
@Time : 2020/3/27 23:39:25 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
通过Python来模拟实现一个txt文件的拷贝过程
"""

import os

"""
在源文件路径上:
    判断是否为先已存在文件
在文件拷贝到指定路径的过程中:
    1.大前提是存到现有目录上,而不是在现有目录的基础上还要由程序新建一或多个子文件夹
    2.给定的只能是文件目录的路径,而不能含有文件    
"""
def copy(source, des):
    if os.path.isdir(source):
        print("当前仅输入目录,未输入文件名!")
    elif os.path.isfile(source):
        with open(source, 'r', encoding='utf-8') as f1:
            text = f1.read()

            if os.path.isdir(des):
                name = os.path.basename(source)  # 获取文件名
                des = os.path.join(des, name)  # 拼接路径和文件名

                with open(des, 'w', encoding='utf-8') as f2:
                    f2.write(text)
                print('拷贝成功')
            else:
                print("存储路径错误!")
    else:
        print("无此文件")


print("Python模拟文件拷贝")
src = input("请输入源文件路径地址:")
des = input("请输入文件拷贝后存放路径:")

copy(src, des)



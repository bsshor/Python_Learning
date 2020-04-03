#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 3_5.py
@Time : 2020/3/26 21:34:32 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
文件编程小项目
"""
import os

# 为避免重复创建，
# 先判断"Blowing in the wind.txt"指定文件夹下这个文件是否存在，如果没有则创建。
if not os.path.exists(r'G:\Python_Learning\homework3\Blowing in the wind.txt'):
    try:
        with open(r'G:\Python_Learning\homework3\Blowing in the wind.txt', 'w', encoding='utf-8') as fw:
            string = '''How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they‘re forever banned
The answer, my friend, is blowing in the wind
The answer is blowing in the wind'''
            fw.write(string)

    except Exception as e:
        print(type(e), e)
else:
    print("已存在")

try:
    with open(r'G:\Python_Learning\homework3\Blowing in the wind.txt', 'r', encoding='utf-8') as fr:

        lines = fr.readlines()

        # 本处用到了嵌套，外层的目的是读取原文本，暂存于lines，内层则是实现对原文本的插入
        with open(r'G:\Python_Learning\homework3\Blowing in the wind.txt', 'w', encoding='utf-8') as fw:
            lines.insert(0, '\tBlowing in the wind   Bob Dylan\n')
            lines.append('\n\t\t\t\t1962 by warner Bros.Inc')
            for line in lines:
                fw.write(line)

        # 回到外层，由于第一次读取后，指针fr指向了EOF,
        # 所以，通过fr.seek(num),j将指针fr调到文件开头，num>0
        # 经测试，num指的是第几个字符，从0开始代表第一个字符，而不是指代行
        fr.seek(0)
        lastest = fr.readlines()
        for line in lastest:
            print(line, end='')


except Exception as e:
    print(type(e), ':', e)

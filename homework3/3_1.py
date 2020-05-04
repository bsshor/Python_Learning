#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 3_1.py
@Time : 2020/3/26 19:01:00
@Author : Bundchen
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：写一个程序，读取键盘输入的任意行文字信息，
当输入空行时结束输入，将读入的字符串存于列表;
然后将列表里面的内容写入到文件input.txt中
"""


def is_allspace(String):
    flag = True
    for i in String:
        if i != ' ':
            flag = False
            break
    return flag


text = input("请输入任意行文字信息，当输入空行时结束输入:\n")
texts = []

"""
判断输入截止的思路：
1.用户直接在新的一行里输入回车(\n)，此时input()读入的是：''————空字符串
2.用户输入了一系列空格。例如"                   "
"""
while text != '' and (not is_allspace(text)):
    texts.append(text)
    text = input()

try:
    with open(r'homework3\input.txt', 'w', encoding='utf-8') as fw:
        fw.write('\n'.join(texts))  # join()拼接字符串，用'\n'拼接是因为input不能
        # 读取换行符，写入文件时需要对输入的换行符进行还原
except Exception as e:
    print(type(e), e)

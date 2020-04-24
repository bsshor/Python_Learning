#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 7.1.py
@Time : 2020/4/21 17:43:23 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
    给定一个文件(webspiderUrl.txt)，请用正则表达式，
    逐行匹配提取其中的URL链接信息，
    并保存到另外一个文件中(Url.txt)
"""
import re

try:
    with open(r'G:\桌面\Python_Learning\homework7\webspiderUrl.txt', 'r', encoding='utf-8') as fr:
        pattern = r'[a-zA-z]+://[^\s$(;|\')]*'  # 匹配所有的网址形式
        line = fr.readline()
        while line:
            url = re.findall(pattern, line)  # 获取每行所有符合该模式的网址
            line = fr.readline()

            if url:  # 如果查得的url不为空,则逐个写入url列表里的网址
                with open(r'G:\桌面\Python_Learning\homework7\Url.txt', 'a', encoding='utf-8') as fw:
                    i = 0
                    while i < len(url):
                        fw.write(url[i] + '\n')
                        i += 1

except Exception as e:
    print(type(e), ':', e)


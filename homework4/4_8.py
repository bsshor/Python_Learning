#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 4_8.py
@Time : 2020/3/27 23:39:53 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
京东二面笔试题
1） 生成一个大文件ip.txt,要求1200行，
每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip
"""
import random

# 纯属练手,此处就是想用列表解析式生成ip地址(/▽＼)
ip = [(lambda x: '172.25.254.' + str(random.randint(1, 254)))(x) for x in range(1200)]
try:
    with open('ip.txt', 'w', encoding='utf-8') as fw:
        for text in ip:
            fw.write(text + '\n')

    with open('ip.txt', 'r', encoding='utf-8') as fr:
        Ip_Frequency = {}
        line = fr.readline().strip()
        while line:
            if line in Ip_Frequency.keys():
                Ip_Frequency[line] += 1
            else:
                Ip_Frequency[line] = 1

            line = fr.readline().strip()

except Exception as e:
    print(type(e), ':', e)

print('{:\0<5}\t\t{:\0<18}\t{}'.format('rank'.title(), 'ip'.capitalize(), 'Frequency'))
# 鼠标拿字符串的首字母大小写函数练练手
for i, t in enumerate(sorted(Ip_Frequency.items(), key=lambda x: x[1], reverse=True)[0:10]):
    print(' {:\0<4,}\t{:\0<18}\t{:>5}'.format(i + 1, t[0], t[1]))  # 格式输出控制, \0是ascII码里的空格
    # {:>5}自起始位起从第五处开始输出

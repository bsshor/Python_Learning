#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 3_3.py
@Time : 2020/3/26 20:42:10 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
编写一个程序，读取文件中保存的10个学生成绩名单信息
(学号,姓名, Python课程分数);
 然后按照分数从高到低进行排序输出
"""
try:
    with open(r'homework3\3_3Scores.txt', 'r', encoding='utf-8') as fr:
        lines = []
        # 去掉每行里的换行符
        for line in fr:
            lines.append(line.strip())
        print("\n".join(sorted(lines, key=lambda x: x.split()[2], reverse=True)))
except Exception as e:
    print(type(e), e)

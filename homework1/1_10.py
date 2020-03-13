"""
给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
   提示：可以用字典来统计：key 是单词，value 是单词出现次数；
    先创建一个字典，然后遍历刚刚取出的单词列表，接着做一个判断： 如果字典中 key 已经出现了这个单词，那么它对应的 value ，也就是出现次数就 +1； 如果这个单词没出现过，就直接 插入这个单词及 value 为 1 到 字典中；
"""
# -*- encoding: utf-8 -*-
'''
@File : 1_10.py
@Time : 2020/03/04 23:03:16
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''

# here put the import lib
import re

demo = input("请输入一段文本:")

print("输出：", demo)

text = re.findall(r"[\w']+|[.,!?;]", demo)  # 正则表达式解析单词和标点
dit = {}
i = 0

# 第一步，判断字典里是否有当前单词
while i < len(text):
    if text[i] not in dit:

        dit[text[i]] = 1
    else:
        dit[text[i]] += 1

    i += 1

dit1 = {}
for key in dit.keys():
    if key not in ".,!?;":
        dit1[key] = dit[key]

# sorted()，按值的大小对键排序
print(sorted(dit1.items(), key=lambda item: item[1], reverse=True))

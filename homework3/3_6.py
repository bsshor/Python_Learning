#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 3_6.py
@Time : 2020/3/26 22:35:23 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章),
请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);
"""
import re


# 第一步，读取文章内容
def readtext(path):
    """
    读取文本内容
    :param path:
    :return: 存储每行文本(字符串)的列表
    """
    li = []  # 存储每行文本
    try:
        with open(path, 'r', encoding='utf-8') as fr:
            for line in fr:
                text = line
                if text == '' or text == '\n':
                    continue
                else:
                    li.append(text.strip())
    except Exception as e:
        print(type(e), ':', e)
    finally:
        return li


# 路径
path1 = r'G:\Python_Learning\homework3\08789108.txt'
path2 = r'G:\Python_Learning\homework3\08845524.txt'
li1 = readtext(path1)
li2 = readtext(path2)


# 第二步，分词，去重
def split_sentence(li):
    """
    分词，将句子过滤掉符号后，生成单词
    :param li: 存储句子的列表
    :return: 单词列表
    """
    tokens = []  # 用于存储分词
    for string in li:
        string = re.findall(r"[\w']+|[.,!?;]", string)  # 正则表达式解析单词和标点

        # 正则表达式用的还是不够熟练。。。有些符号(',' '.' ';')没被成功过滤
        for i in string:
            if i == ',' or i == '.' or i == ';':  # 这个if是用来过滤无关的标点符号
                string.remove(i)
            elif i == 'and' or i == 'or' or i == 'of' or i == 'the' or i == 'to' or i == 'is' or i == 'are' or i == 'in' or i == 'on':
                string.remove(i)  # 此处的i判断是用来模拟去重，
                # 以上介词和连词在文中出现频率均极高，
                # 但对相似度的影响很小
            else:
                tokens.append(i)
    return tokens


tokens1 = split_sentence(li1)
tokens2 = split_sentence(li2)


# 第三步，统计频率
def frequency(tokens):
    """
    统计频率
    :param tokens: 存储字符串的列表
    :return:key：词频字典 key：numbers
    """
    dit = {}
    i = 0
    # 判断字典里是否有当前单词
    for i in tokens:
        if i not in dit:
            dit[i] = 1
        else:
            dit[i] += 1
    return dit


dit1 = frequency(tokens1)
dit2 = frequency(tokens2)

# 第四步，判断相似度
# print(sorted(dit1.items(), key=lambda item: item[1], reverse=True))
sample1 = sorted(dit1.items(), key=lambda item: item[1], reverse=True)
# print(sample1)
sample2 = sorted(dit2.items(), key=lambda item: item[1], reverse=True)
# print(sample2)

# 从两文中取前n个高频单词做相似度计算
# n的计算依据：样本较小的那个的长度的60%
if len(sample1) < len(sample2):
    n = int(len(sample1) * 0.6)
else:
    n = int(len(sample2) * 0.6)
# i 计算相似的单词个数
i = 0
for a in sample1[0:n]:
    # print(a[0])
    for b in sample2[0:n]:
        # print(b[0])
        if b[0] == a[0]:
            i += 1

# 以百分号形式输出
print("两论文的相似度为：%s" % (str(i / n * 100)[:5] + '%'))

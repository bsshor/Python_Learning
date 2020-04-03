"""
练习4
:   一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出到另外一个文件中:
            姓名      学号      分数
            张三      101         78
            李四      102         87
            王五       103        83
并将分数排序后输出
"""
# -*- encoding: utf-8 -*-
'''
@File : 0318_4.py
@Time : 2020/03/18 09:40:08
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
'''
import os

with open("test3.txt", 'r', encoding='utf-8') as f:
    line = f.readline()
    print(line, end='')
    with open("test4.txt", 'w', encoding='utf-8') as fw:
        fw.write(line)
    line = f.readline()
    lines = {}
    while line:
        # line = line.split()
        line = line.strip()
        for i in range(len(line) - 1, -1, -1):
            if line[i] == ' ':
                lines[line[:i + 1]] = line[i + 1:]
                # print(lines)
                break
        line = f.readline()
    texts = sorted(lines.items(), key=lambda d: d[1], reverse=True)
    for text in texts:
        string = text[0] + text[1] + '\n'
        print(string, end='')
        with open("text4.txt", 'a', encoding='utf-8') as fw:
            fw.write(string)

'''
#方法2：

with open(r"G:\Python_Learning\exercise\exe 1.17\test3.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    #lines = [_ for _ in lines if _.strip()]
    for line in lines[:3]:
        lines.append(line.strip())
        print(line.strip())
    str_1 = '\n'
    print("lines:",lines)
    lines = lines[3:]
    print("new",lines)
    #print(str_1.join(sorted(lines, key=lambda s: s.split()[2], reverse=1)))
    print((sorted(lines[3:], key=lambda s: s.split()[2], reverse=1)))
    with open('test4.txt','w',encoding='utf-8') as fw:

        b=str_1.join(sorted(lines,key=lambda s:s.split()[2],reverse=1))
        print('b=str_1.join(sorted(lines,key=lambda s:s.split()[2],reverse=1):',b)
        fw.write('\n'.join(sorted(lines,key=lambda s:s.split()[2],reverse=1)))


    #print(str_1.join(sorted(open('test3.txt', 'r', encoding='utf-8'), key=lambda s: s.split()[2], reverse=1)))

'''

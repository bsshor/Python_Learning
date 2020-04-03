#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 4_6.py
@Time : 2020/3/27 23:39:35
@Author : Bundchen
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，
如果是文件，显示大小; 输出格式效果如下:

​ 名称 日期 类型（文件夹或者 文件） 大小


"""
import datetime
import os

import A4_7 as File_Size  # 导入A4_7.py,作为计算文件大小的工具包


def strB2Q(ustring):
    """半角字符转全角字符"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 32:  # 半角空格直接转化
            inside_code = 12288
        elif 32 <= inside_code <= 126:  # 半角字符（除空格）根据关系转化
            inside_code += 65248

        rstring += chr(inside_code)
    return rstring


# filetype.add_type()
file = input("请输入任意一个文件夹路径:")
path_list = os.listdir(file)

print("{:\u3000<20}\t\t{:\u3000<20}\t\t{:\u3000<10}\t\t{}".format("名称", "日期", "类型", "大小"))
# {}是占位符
# \u3000全角空格(中文符号),中文文章中使用
# \u3000<20 表示改占位符长为20,长度小于20且无内容的位置用\u3000填充

for name in path_list:
    path = os.path.join(file, name)
    time = os.path.getctime(path)  # 本处选择的是输出文件最近修改时间函数,结果:1583948773.0837238
    time = datetime.datetime.fromtimestamp(time)  # 转换成可读格式,输出结果2020-03-12 01:46:13.083724
    time = str(time)[0:-7]  # 去掉后七位小数点
    if os.path.isdir(path):
        type = "文件夹"
    else:
        type = os.path.splitext(path)[1] + "文件"  # 获取文件后缀名
    size = File_Size.file_base_conversion(path)
    name = strB2Q(name)
    time = strB2Q(time)
    type = strB2Q(type)
    size = strB2Q(size)
    print("{:\u3000<20}\t\t{:\u3000<20}\t\t{:\u3000<10}\t\t{}".format(name, time, type, size))

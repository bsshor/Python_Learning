#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : A4_7.py
@Time : 2020/3/27 23:39:43 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
使用python代码统计一个文件夹中所有文件的总大小
"""
"""
测试发现,os模块里的获取文件大小的方法返回值均为字节,
在windows操作系统里,单个文件是以kb为最小文件大小显示的,采取进一法.
例如:346B以1KB显示,
对于windows的文件夹的情况,则是在实际总大小(字节)的基础上,通过进制转换与进一法,显示的
例如:A文件夹下有11个实际大小均是102B的文件(每个文件在windows下显示为1KB),怎A的大小是2KB,而不是11KB
进制:
1TB = 1024GB; 1GB = 1024MB; 1MB = 1024KB; 1KB = 1024B; 1B = 8bit
"""

"""
本题从阅读角度来看,字节形式输出体验度差,需要进行进制转换
"""
import os


def getsize(path):
    """
    计算当前目录或文件的大小
    :param dir:
    :return:
    """
    if os.path.isfile(path):
        size = os.path.getsize(path)  # 文件
    elif os.path.isdir(path):  # 文件夹
        size = 0
        for root, dirs, files in os.walk(path):
            size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    else:
        print("目录错误")
    return size


def file_base_conversion(path):
    """
    对文件大小的进制转换
    :param path:
    :return:
    """
    size_bite = getsize(path)

    units = ['B', 'KB', 'MB', 'GB', 'TB']
    i = 0  # i标志单位级别
    Int = size_bite  # Int标志的是进制转换后的整数位
    while Int // 1024 > 0:
        i += 1
        Int //= 1024
    if i > 0:
        other = str(size_bite)[len(str(Int)):]
        Decimal = int(other) / (1024 ** i)  # Decimal记录小数部分,效果示例:0.6611328125
    else:
        Int = 1
        Decimal = '0.00'
        i = 1
    size = str(Int) + '.' + str(Decimal)[2] + units[i]
    return size


"""
#此处一改往常,采用伪主函数的形式
#原因是因为我要在4_6.py中调用这个文件里的函数
#如果不使用这种形式,
#那么4_6.py在编译本文件时,会把本文件最后两行也一并执行
#同样,为了4_6.py可以调用这个文件里的函数,必须把名字改成非纯数字的文件名,否则报错
"""
if __name__ == '__main__':
    path = input("请输入任意一个文件夹路径:")
    print(file_base_conversion(path))

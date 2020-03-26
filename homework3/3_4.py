#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 3_4.py
@Time : 2020/3/26 21:03:49 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
将当前img目录所有以.png结尾的后缀名改为.jpg.
"""
import os

path = r'G:\Python_Learning\homework3\img'
# 获取当前目录下所有的文件，存于列表files中
files = os.listdir(path)

for filename in files:
    portion = os.path.splitext(filename)  # 将列表中每个文件名分割成一个元组
    # 例如('0f4fc3ec80235880c0f4689f097be46', '.jpg')
    if portion[1] == '.png':
        # 重新组合文件路径、文件名和后缀名
        # 如果是要跨目录的话，必须指明所在路径，不然os.rename(filename,newname)找不到指定位置
        filename = path + '\\' + filename
        newname = path + '\\' + portion[0] + ".jpg"
        os.rename(filename, newname)

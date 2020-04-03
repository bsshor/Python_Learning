#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 4_3.py
@Time : 2020/3/27 23:38:59 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
从键盘输入5个同学的账号和密码,
然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
例如，
​ Tom admin XXXXX
​ Jack root XXXXX
"""
import hashlib

md5 = hashlib.md5()
try:
    with open(r'homework4\Ids.txt', 'w', encoding='utf-8') as fw:
        for i in range(1, 6):
            print("请输入第%d位同学的" % i)
            name = input("姓名:")
            Id = input("账号:")
            password = input("密码:")
            md5.update(password.encode('utf-8'))
            password = md5.hexdigest()
            print('\n')

            fw.write(name + ' ')
            fw.write(Id + ' ')
            fw.write(password + '\n')


except Exception as e:
    print(e)



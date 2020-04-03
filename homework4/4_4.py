##!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 4_4.py
@Time : 2020/3/27 23:39:16 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
(继续上面的练习) 模拟用户登录:5个同学的姓名,账号和密码(加密后的),保存在一个文件上;
系统提示,请输入登录同学姓名,
正确后,请输入账号,
正确后,提示请输入密码（输入明文）;
如果都正确,打印提示, 您登录成功(失败);
"""
import hashlib
md5 = hashlib.md5()
try:
    with open(r'homework4\Ids.txt', 'r', encoding='utf-8') as fr:
        texts = []
        for i in range(5):
            text = fr.readline().split()
            texts.append(text)
        
            

except Exception as e:
    print(e)

dit = {}
for text in texts:
    dit[text[0]] = (text[1], text[2])

choice = 'yes'

while choice == 'yes':
    name = input("请输入姓名:")
    if name in dit:
        Id = input("请输入账号:")
        if Id == dit[name][0]:
            password = input("请输入密码:")
            md5.update(password.encode('utf-8'))
            password = md5.hexdigest()
            if password == dit[name][1]:
                print("登录成功")
            else:
                print("密码错误,登录失败")

        else:
            print("账号错误,登录失败")

    else:
        print("查无此用户,登录失败")

    choice = input("请问还要继续吗(输入yes或no):")
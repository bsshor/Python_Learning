# -*- encoding: utf-8 -*-
'''
@File : 0415_1.py
@Time : 2020/04/15 09:11:50
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
    匹配出163的邮箱地址，且@符号之前有4到20位英文或者数字字符，
例如hello@163.com
'''

# here put the import lib
import re

email = input("请输入邮件地址：")
if re.match('^[0-9a-zA-Z_]{4,20}@163\.com$', email):
    print("right:", email)
else:
    print("wrong")

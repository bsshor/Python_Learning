#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : 7.2.py
@Time : 2020/4/22 00:16:42 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：

"""
# import re
# # pattern = re.compile(r'[a-zA-z]+://[^\s$(;|\')]*')
# # str = "INSERT INTO `temp_icp_web` VALUES ('77', '581', '一汽马自达汽车销售有限公司','http://www.faw-mazda.com; http://www.quyuhuodong.com; http://www.mazda6.com.cn; http://www.rx-8.com.cn; http://www.mazda3.com.cn; http://faw-mazda5.com; http://faw-mx5.com.cn; http://faw-mx5.com; http://www.faw-cx-7.com; http://www.cx-7.com.cn');"
# # rs = pattern.search(str)
# # print(rs.groups())

import re

content = 'Hello 123456789 Word_This is just a test 666 Test'
result = re.search('(\d+).*?(\d+).*', content)

print("result:", result)
print("result.group():", result.group())  # print(result.group(0)) 同样效果字符串
print("result.groups():", result.groups())
print(result.group(1))
print(result.group(0))
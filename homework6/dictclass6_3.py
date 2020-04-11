#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : dictclass6_3.py
@Time : 2020/4/10 14:57:34 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：
定义一个字典类：dictclass
完成下面的功能：
    dict = dictclass({你需要操作的字典对象})
    1 删除某个key
        del_dict(key)
    2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
        get_dict(key)
    3 返回键组成的列表：返回类型;(list)
        get_key()
    4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
        update_dict({要合并的字典})
"""


class dictclass(object):
    def __init__(self, dict={}):
        self.dict = dict

    def del_dict(self, key):
        del self.dict[key]

    def get_dict(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return "not found"

    def get_key(self):
        return self.dict.keys()

    def update_dict(self, alt_dict):
        self.dict.update(alt_dict)
        return self.dict.values()


sample = {"a": 1, "b": 34, 1001: 89, 1002: 23, 1003: 78, 1004: 88, 1005: 76,
          1006: 99, 1007: 93, 1008: 85.5, 1009: 64.5, 1010: 88.5}
alt = {"是多少": 234, "未发生": 2}
dic = dictclass(sample)

print(dic)
print(dic.get_key())
print(dic.get_dict(' rr'))
print(dic.update_dict(alt))
print(dic.get_key())

"""
写函数，检查传入字典的每一个value长度，
如果大于2，那么仅保留前两个长度的内容，
并将新内容返回给调用者写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
"""
import random


def check_length(dit={}):
    for key, value in dit.items():
        if len(value) > 2:
            dit[key] = value[0:2]
    return dit


dit = {}
for i in range(50):
    dit[i] = str(random.randint(1, 434))
print("原字典：", dit)
dit = check_length(dit)
print("新字典：", dit)

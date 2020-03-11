"""
写函数，判断用户传入的对象（字符串、列表、元组）长度,
并返回给调用者
"""


# 失败
# input()读入后的类型都是字符串，需要修改类型
def length(Object):
    return len(Object)


index = input("请任意输入一个对象（字符串、列表、元组）：")
if index[0] == '[' and index[-1] == ']':
    index = [x for x in index[1:-1] if x != ',']
elif index[0] == '(' and index[-1] == ')':
    index = [x for x in index[1:-1] if x != ',']
    index = tuple(index)
print("长度为:", length(index))

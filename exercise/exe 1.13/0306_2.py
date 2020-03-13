"""
定义一个函数,  打印输出列表里面的元素;  
然后增加列表中的元素, 然后再输出新的列表; 
主程序中,打印这个列表的地址(传参之前,传参之后)
"""


def List(mylist):
    print("刚传进来的列表：", mylist)
    print("刚传进来的列表地址：", id(mylist))
    mylist.append('new')
    print("新增后的列表：", mylist)
    print("新增后的列表地址：", id(mylist))


mylist = [1, 2]

print("原列表：", mylist)
print("原列表地址：", id(mylist))
List(mylist)
print("调用后的原列表：", mylist)
print("调用后的列表地址：", id(mylist))

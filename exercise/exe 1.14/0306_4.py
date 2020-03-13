"""
使用不定长参数定义一个函数;
实现对输入数据的封装(封装成一个列表和字典),
然后打印输出
"""


def indefine1(x, *y):
    print(x)
    print(list(y))


def indefine2(x, **y):
    print(x)
    print(y)


indefine1('x', 'dssd', 'asasas', 'dsads', 'asd', 'asdas', 'das')
indefine2('x', dssd='asasas', dsads='asd', asdas='das')

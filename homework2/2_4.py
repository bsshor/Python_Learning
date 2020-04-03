"""
写函数，
统计字符串中有几个字母，几个数字，几个空格，几个其他字符，
并返回结果
"""


def sum_char(str=''):
    letter = 0;
    num = 0;
    space = 0;
    others = 0;

    for i in str:
        if i in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
            letter += 1
        elif i in '1234567890':
            num += 1
        elif i == ' ':
            space += 1
        else:
            others += 1

    print("字母：%d" % letter)
    print("数字：%d" % num)
    print("空格：%d" % space)
    print("其他：%d" % others)


sum_char(input("请输入一个字符串："))

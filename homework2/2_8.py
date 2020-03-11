"""
请用Python定义一个函数，给定一个字符串，
找出该字符串中出现次数最多的那个字符，
并打印出该字符及其出现的次数。
 例如，输入 aaaabbc，输出：a:4
"""


# 需要对字符串进行切片
def string_cut_sum(str=''):
    dit = {}
    for i in str:
        if i not in dit:
            dit[i] = 1
        else:
            dit[i] += 1
    dit = sorted(dit.items(), key=lambda item: item[1], reverse=True)
    print(dit[0][0], ":", dit[0][1])


string_cut_sum(input("请输入一个字符串："))

"""
定义一个函数, 打印输出n以内的斐波那契数列
"""
import random


def fibonacci(max):
    fibonacci = [0, 1]
    while fibonacci[-1] < max:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if fibonacci[-1] >= max:  # 如果最后一个元素大于100，则删除
        del fibonacci[-1]
    for i in fibonacci:
        print(i)


n = random.randint(0, 200)
print('n=%d' % n)
fibonacci(n)

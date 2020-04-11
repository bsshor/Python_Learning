# -*- encoding: utf-8 -*-
'''
@File : 5_3.py
@Time : 2020/04/08 00:48:20
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description :  
    编写一个装饰器，为多个函数加上认证的功能
（必须输入用户的账号密码，才能调用这个函数）
'''

# here put the import lib


def outer(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    status = False
    try:
        with open(r'G:\桌面\Python_Learning\homework5\account.txt', 'r', encoding='utf-8') as fr:
            texts = []
            text = fr.readline().split()
            while text:
                texts.append(text)
                text = fr.readline().split()

    except Exception as e:
        print(e)

    dit = {}
    for i in texts:
        dit[i[0]] = i[1]

    print(dit)
    # 支持验证三次账号,三次都验证失败则退出
    frequency = 3
    while frequency > 0:
        name = input("请输入账号:")
        password = input("请输入密码:")

        if name in dit:
            if password == dit[name]:
                status = True
                frequency = 0
            else:
                print("密码错误!")
                frequency -= 1
        else:
            print("无此账号!")
            frequency -= 1

    if status:
        print("验证成功!")
        return inner
    else :
        return None
    
@outer
def a():
    print(12345)


a()

@outer
def b(x, y):
    return x * y


print(b(12, 3))


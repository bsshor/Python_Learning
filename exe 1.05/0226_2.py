"""
定义一个字符串,分别进行查找某个字符串是否包含在这个字符串里面;
进行某个字符串的替换;
打印字符串的长度;
"""
vars = "My name is Bundchen,I love Python!"
print(vars)

# 查找方法1
if ('is' in vars):
    print('is' + "在变量vars中")
else:
    print("is" + "不在变量vars中")

# 查找方法2
if vars.find('is') < 0:
    print("未查到")
else:
    print("在")

var = vars.replace('is', 'IS')
print(var)  # 输出被替换的字符串

print(len(vars))  # 打印字符串长度

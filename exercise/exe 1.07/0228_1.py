"""
定义元组,进行基本的操作(元组的基本运算,元素的输出,内置函数的使用);
定义一个元组,来保存成绩,输出最高分;
"""

color = (233, 0, 32)
name = ('0', 9)
print(color)
print(sorted(color))
print(len(color))
print(color[2])
print(color.count('x'))
my = name + color
print(my)
print(color * 3)

score = (23, 43, 43, 54, 5443, 32, 543, 23, 43, 5423, 345, 3, 54233)
print(max(score))

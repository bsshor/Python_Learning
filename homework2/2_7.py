"""
随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;
A---成绩>=90;
B-->成绩在 [80,90)
C-->成绩在 [70,80)
D-->成绩<70
"""
import random
def level(score = {}):

    for key,value in score.items():
        if value >= 90:
            print("%d学生的成绩等级为A"% key)
        elif value >= 80:
            print("%d学生的成绩等级为B"% key)
        elif value >= 70:
            print("%d学生的成绩等级为C"% key)
        else:
            print("%d学生的成绩等级为D"% key)

def built_dir( ):
    stu = {}
    for i in range(1,21):
        stu[i] = random.randint(0,100)
#   level(stu)
    return stu

level(built_dir( ))
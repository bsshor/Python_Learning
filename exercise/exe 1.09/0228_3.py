"""
 字典的元素的增加, 修改,删除;
 并观察输出
"""
student = {'id': 120181080701, 'name': "邵博深", 'class': "软件1802", 'age': 21}
student['age'] = 20
students = {"stu1": ('001', '小明'), 'stu2': ('002', '小红'), 'stu3': ('003', '小红'),
            'stu4': ('004', '小强'), 'stu5': ('005', '小华')}
print(students)
print(students.keys())
print(students.values())
print(students['stu5'][0], ',', students['stu5'][1])

students['stu1'] = 'null'
print(students)
del students['stu1']
print(students)
students.__delitem__('stu2')
print(students)
students[1] = 6
students[(1, 'color')] = [43, "uihu", (6566, 989, {1: 6})]
print(students)
print(students.get('567', 1111111))
print(students.get('567'))
print(students.update(student))
print(students)

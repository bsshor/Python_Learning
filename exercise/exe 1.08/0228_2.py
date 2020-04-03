"""
 定义一个字典,存放某个同学的信息(学号,姓名,班级,年龄);
 再定义另外一个字典,存放5个同学的学号,姓名信息;
 通过键来访问相应的数据; 或者整体输出
"""
student = {'id': 120181080701, 'name': "邵博深", 'class': "软件1802", 'age': 21}
print(student)
print(student['name'])

students = {"stu1": ('001', '小明'), 'stu2': ('002', '小红'), 'stu3': ('003', '小红'),
            'stu4': ('004', '小强'), 'stu5': ('005', '小华')}
print(students)
print(students.keys())
print(students.values())
print(students['stu5'][0], ',', students['stu5'][1])

'''
将这4中方式实现的代码分别在vscode上练习一下;
观察输出结果
'''
print('例子1')
username = input('username:')
password = input('password:')
print(username, password)

print('例子2')
name = input("name:")
age = input("age:")
skill = input("skill:")
salary = input("salary:")
info = ''' --- info of ''' + name + ''' name: ''' + name + ''' age: ''' + age + ''' skill: ''' \
       + skill + ''' salary: ''' + salary + ''' ---'''
print(info)

print("例子3")
name = input("username：")
age = input("age：")
skill = input("skill：")
salary = input("salary：")
info = ''' --- info of {_name} Name：{_name} Age：
{_age} Skill：{_skill} Salary：{_salary} '''.format(_name=name, _age=age, _skill=skill, _salary=salary)  # 此处是赋值
print(info)

print("例子4")
name = input("name：")
age = input("age：")
skill = input("skill：")
salary = input("salary：")
info = ''' --- info of {0}--- Name：{0} Age：{1} Skill：{2} Salary：{3} '''.format(name, age, skill, salary)
print(info)

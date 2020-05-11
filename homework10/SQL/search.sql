# 查询所有男生的姓名，年龄，所在班级名称；
select students.name, students.age, classes.name
from students,
     classes
where classes.id = students.cls_id;

# 查询所有查询编号小于4或没被删除的学生；
select *
from students
where students.id < 4
   or students.is_delete = 0;

# 查询姓黄并且“名”是一个字的学生；
select *
from students
where students.name like "黄_";

# 查询编号是1或3或8的学生(方案1)
select *
from students
where students.id = 1
   or students.id = 3
   or students.id = 8;
# 查询编号是1或3或8的学生(方案2)
select *
from students
where students.id in (1, 3, 8);


# 查询编号为3至8的学生(方案1)
select *
from students
where students.id >= 3
  and students.id <= 8;
# 查询编号为3至8的学生(方案2)
select *
from students
where id between 3 and 8;

# 查询未删除男生信息，按年龄降序
select *
from students
where students.gender = '男'
  and students.is_delete = 0
order by students.age desc;

# 查询女生的总数
select count(*) as sum_of_female
from students
where students.gender = '女';

# 查询学生的平均年龄
select avg(students.age) as avg_age
from students;

# 分别统计性别为男/女的人年龄平均值
select students.gender, avg(students.age) as avg_age
from students
group by students.gender;

# 按照性别来进行人员分组如下显示
select gender, group_concat(name) as name
from students
group by gender;
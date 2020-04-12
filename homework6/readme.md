# exe6-Python面向对象编程练习题

[作业地址](https://note.youdao.com/ynoteshare1/index.html?id=66b9264782f8b321bc8b90f3ba763389&type=note)

### 一、定义一个狗类
里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
dog6_1.py
### 二 定义一个学生Student类。
有下面的类属性：

1 姓名 name

2 年龄 age

3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]

类方法：

1 获取学生的姓名：get_name() 返回类型:str

2 获取学生的年龄：get_age() 返回类型:int

3 返回3门科目中最高的分数。get_course() 返回类型:int

写好类以后，可以定义2个同学测试下:
Student6_2.py
### 三、定义一个字典类：dictclass
完成下面的功能：

dict = dictclass({你需要操作的字典对象})

1 删除某个key

del_dict(key)

2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"

get_dict(key)

3 返回键组成的列表：返回类型;(list)

get_key()

4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)

update_dict({要合并的字典})

dictclass6_3.py
### 四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，

​      封装方法，求单个学生的总分，平均分，以及打印学生的信息。
Student6_4.py

### 五  请写一个小游戏，人狗大战
规则:

​    1   2个角色，人和狗，游戏开始后，生成2个人，3条狗，人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 

​        人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;

​    2  人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;

​        人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);

​    3   对战规则: 

​     A  随机决定,谁先开始攻击; 

​     B  一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);

​     C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;

提示：注意组织代码的方式；狗类用一个单独的py文件； 人用一个单独的py文件； 在写一个fight模块（也用类来组织；在这个模块中，导入人和狗模块中编写好的方法）
Man-dog battle 6_5
### 六  用面向对象,实现一个学生Python成绩管理系统

​      学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)

​      实现对学生信息及成绩的增,删,改,查方法;

​       
# 请写一个小游戏，人狗大战
### 规则:

​    1   2个角色，人和狗，游戏开始后，生成2个人，3条狗，人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 

​        人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;

​    2  人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;

​        人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);

​    3   对战规则: 

​     A  随机决定,谁先开始攻击; 

​     B  一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);

​     C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
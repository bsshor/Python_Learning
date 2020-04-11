#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File : Main.py
@Time : 2020/4/10 21:48:16 
@Author : Bundchen 
@Version : 1.0
@Contact : 1476193741@qq.com
@Description ：

"""
import random
import time

from dog import Dog
from human import Human


def game():
    p1 = Human("赫拉克洛斯")
    p2 = Human("亚索")
    d1 = Dog("比卡布")
    d2 = Dog("达斯酱")
    d3 = Dog("撒大莎")
    dog = [d1, d2, d3]
    person = [p1, p2]
    choice = [dog, person]
    # 随机决定谁先发动攻击
    Attacker = random.randint(0, 1)  # 选择进攻方

    # 受攻击方
    Loser = 0
    print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    if Attacker == 0:
        Loser = 1
        print("汪星人悍然挑起战争!")
    else:
        print("人类悍然发动战争!")

    print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')
    # 游戏主循环
    while dog and person:
        time.sleep(1)
        Attack_object = random.randint(0, len(choice[Attacker]) - 1)  # 被攻击方
        Attacked_object = random.randint(0, len(choice[Loser]) - 1)  # 被攻击方
        if choice[Loser][Attacked_object].life > 0:
            choice[Loser][Attacked_object].life -= choice[Attacker][Attack_object].attack
            if choice[Loser][Attacked_object].life < 0:
                choice[Loser][Attacked_object].life = 0
        if choice[Loser][Attacked_object].attack > 0 and choice[Attacker][Attack_object].attack > 0:
            # 如果攻击者仍有攻击力 且 被攻击者也还有攻击力
            choice[Loser][Attacked_object].attack -= choice[Loser][Attacked_object].locked
            if choice[Loser][Attacked_object].attack < 0:
                choice[Loser][Attacked_object].attack = 0

        if Loser == 1:
            print(">>>人族战士%s受到汪星人%s攻击" % (choice[Loser][Attacked_object].name,
                                          choice[Attacker][Attack_object].name))
            print("\t攻击者:%-6s生命力:%-5d攻击力:%-5d" % (
                choice[Attacker][Attack_object].name, choice[Attacker][Attack_object].life,
                choice[Attacker][Attack_object].attack))
            print("\t伤  者:%-6s生命力:%-5d攻击力:%-5d" % (
                choice[Loser][Attacked_object].name, choice[Loser][Attacked_object].life,
                choice[Loser][Attacked_object].attack))
        else:
            print(">>>汪星人%s受到人族战士%s攻击" % (choice[Loser][Attacked_object].name,
                                          choice[Attacker][Attack_object].name))
            print("\t攻击者:%-6s生命力:%-5d攻击力:%-5d" % (
                choice[Attacker][Attack_object].name, choice[Attacker][Attack_object].life,
                choice[Attacker][Attack_object].attack))
            print("\t伤  者:%-6s生命力:%-5d攻击力:%-5d" % (
                choice[Loser][Attacked_object].name, choice[Loser][Attacked_object].life,
                choice[Loser][Attacked_object].attack))

        if choice[Loser][Attacked_object].life <= 0:
            time.sleep(0.5)
            print('\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            if Loser == 1:
                print("!!!人族战士%s阵亡" % (choice[Loser][Attacked_object].name))
            else:
                print("!!!汪星人%s战死" % (choice[Loser][Attack_object]).name)
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n')
            choice[Loser].pop(Attacked_object)  # 战死者出局

        # 由对手出招
        if Loser == 1:
            Loser = 0
            Attacker = 1
        else:
            Loser = 1
            Attacker = 0

    # 判断胜利方
    # time.sleep(1)
    print("\n>>>>>>>>>>>>>>> Game Over <<<<<<<<<<<<<<<")
    if person:
        print('人族胜利（￣︶￣）↗　')
    else:
        print("汪星人胜利(っ´Ι`)っ")
    print(">>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<")


if __name__ == "__main__":
    game()

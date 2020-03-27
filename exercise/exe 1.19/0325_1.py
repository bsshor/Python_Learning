"""
文件复制
"""
import os


def copy(source, des):
    if os.path.exists(source):
        with open(source, 'r', encoding='utf-8') as f1:
            text = f1.read()
            name = os.path.basename(source)
            des = os.path.join(des, name)
            with open(des, 'w', encoding='utf-8') as f2:
                f2.write(text)
            print('成功')
    else:
        print("无此文件")


# 测试


copy(r'G:\Python_Learning\exercise\exe 1.19\0325_1.py', r'G:\Python_Learning\exercise\exe 1.17\subdir')

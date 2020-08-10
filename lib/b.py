# coding=utf-8
# /usr/bin/env python3

'''
Author: swang
Email: 13693554615@163.com

date: 2019-11-01 15:32
'''
import random
from pathlib import Path
path = str(Path('config') / ('txt_final.txt'))

def create_phone():
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    suffix = random.randint(9999999,100000000)
    phone = "1{}{}{}".format(second, third, suffix)

    writetxt(phone)
    return phone

def writetxt(phone):
    print(phone)
    f = open(path, 'a')
    f.write(phone + '\n')
    f.close()

def gettxt():
    try:
        f = open(path, 'r')
        sourceInLines = f.readlines()

        return sourceInLines[0]
    except:
        pass

    f.close()

def gettoken():
    f = open(path, 'r')
    sourceInLines = f.readlines()
    try:
        return sourceInLines[1]
    except:
        print('no foung token')
    f.close()

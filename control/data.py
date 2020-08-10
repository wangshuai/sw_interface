# coding=utf-8
# /usr/bin/env python3

'''
Author: swang
Email: 13693554615@163.com

date: 2019-11-01 15:32
'''
import re
import time
from lib import *
var = []


def replace(data):
    keys = re.findall(r'<(.*?)>', data)
    for r in keys:
        data = data.replace('<' + r + '>', eval(r))

    return data

if __name__ == '__main__':
    parmars = "{'phone': '<b.create_phone()>', 'type': '1'}"
    print(replace(parmars))
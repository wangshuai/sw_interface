# coding=utf-8
# /usr/bin/env python3

'''
Author: swang
Email: 13693554615@163.com

date: 2019-11-07 15:53
'''
# 1、求1-100之间的和
# 1.1
# a = 0
# for i in range(11):
#     a += i
# print(a)
# 1.2
# sum = sum(range(101))
# print(sum)
# 2、冒泡排序
a = [1, 4, 5, 2, 3]
l = len(a)
for i in range(l):
    for j in range(l-1):
        if a[l-j-1] < a[l-j-2]:
            a[l-j-1], a[l-j-2] = a[l-j-2], a[l-j-1]
for i in range(l):
    print(a[i])
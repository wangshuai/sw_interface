# coding=utf-8
# /usr/bin/env python3

'''
Author: swang
Email: 13693554615@163.com

date: 2019-11-26 15:14
'''
# a = [1,2,5,4,3,4,5,3,7,2]
# a.sort()
# last = a[-1]
# for i in range(len(a)-2,-1,-1):
#     if last ==a[i]:
#         del a[i]
#     else:
#         last = a[i]
#
# print(a)

# 随机数字小游戏
# import random
# i = 1
# a = random.randint(1,100)
# print(a)
# b = int(input('请输入： '))
# while a !=b:
#     if a >b:
#         print('第%d次输入小于电脑随机数字'%i)
#         b = int(input('请再次输入： '))
#     else:
#         print('第%d次输入大于电脑随机数字'%i)
#         b = int(input('请再次输入： '))
#     i+=1
# else:
#     print('恭喜，第%d次输入与电脑随机数字%d一样'%(i,b))

# 冒泡排序
# array = [1,2,5,3,6,8,4]
# for i in range(len(array) - 1, 0, -1):
#     print(array[i], end='')
# for i in range(0, len(array), 1):
#     print(i)
#     for j in range(i + 1, len(array), 1):
#         if array[j] < array[i]:
#             array[j], array[i] = array[i], array[j]
#
# print(array)

# json & dict
import json

# coding=utf-8
# /usr/bin/env python3

'''
Author: swang
Email: 13693554615@163.com

date: 2019-11-01 16:47
'''
import requests
from control.log import logger
def http_requests(step, junit, sort='get'):
    data = step['data'].replace('\n', '')
    http_type, parmars = datatating(data)

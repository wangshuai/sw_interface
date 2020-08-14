# coding=utf-8
# /usr/bin/env python3

'''
Author: swang
Email: 13693554615@163.com

date: 2019-11-01 16:47
'''
import logging
import datetime
from pathlib import Path
import sys
from control.utlis import mkdir
# 获取当前时间
def today():
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d')
# 获取logger实例，如果参数为空返回root logger
logger = logging.getLogger("sw_interface")
# 制定logger输出格式
formatter = logging.Formatter(
    '%(asctime)s [%(levelname)s] %(filename)s line:%(lineno)d: %(message)s')
# 创建log文件夹
mkdir('log')
# 文件日志
log_file = str(Path('log') / '{}.log'.format(today()))
file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8', delay=False)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.setLevel(logging.INFO)
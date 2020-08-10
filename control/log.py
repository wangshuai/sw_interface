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

def today():
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d')

logger = logging.getLogger("swang_interface")

formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s line:%(lineno)d: %(message)s')
mkdir('log')
log_file = str(Path('log') / '{}.log'.format(today()))
file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8', delay=False)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.setLevel(logging.INFO)
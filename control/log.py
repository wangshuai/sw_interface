# coding=utf-8
# /usr/bin/env python3

'''
Author: swang
Email: 13693554615@163.com

date: 2019-11-01 16:47
'''
import logging
import datetime
import time
import os
from pathlib import Path
import sys
from control.utlis import mkdir

class Logger:
    def __init__(self):
        file_date = time.strftime("%Y-%m-%d", time.localtime())
        base_path = os.path.dirname(__file__)
        log_dir = base_path + '/log'
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        self.file_name = ''.join((log_dir, os.sep, 'autotest-', file_date, '.log'))
        self.logger = logging.getLogger('sw_interface')
        if not self.logger.handlers:
            self.formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(filename)s line:%(lineno)d: %(message)s')
            self.logger.setLevel(logging.INFO)
            self.fh = logging.FileHandler(self.file_name, encoding='utf-8')
            self.ch = logging.StreamHandler()
            self.fh.setFormatter(self.formatter)
            self.ch.setFormatter(self.formatter)
            self.logger.addHandler(self.fh)
            self.logger.addHandler(self.ch)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

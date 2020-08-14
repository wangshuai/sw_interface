# coding=utf-8
# /usr/bin/env python3

'''
Author: swang
Email: 13693554615@163.com

date: 2020-08-14 10:39
'''

# -*- coding: utf-8 -*-

from pathlib import Path

mali_dict = {'send_user': 'shuai.wang@taurus.ai',  # 发件人
             'password': 'wS0502Sw',  # 2密码
             'receive_users': '13693554615@163.com',  # 3收件人地址
             'receive_lisy': [],  # 4收件人list地址
             'subject': 'python自动化测试报告',  # 5主题
             'email_text': 'hi hello this report',  # 6邮件正文
             'server_address': 'smtp.exmail.qq.com',  # 7服务器地址
             'mail_type': 1}  # 8邮件类型
header = {
    '用例编号': 'id',
    '用例标题': 'title',
    '前置条件': 'condition',
    '测试功能点': 'testdot',
    '测试步骤': 'step',
    '操作': 'keyword',
    '页面': 'page',
    '元素': 'element',
    '测试数据': 'data',
    '预期结果': 'expected',
    '断言': 'assert',
    '设计者': 'designer',
    '步骤结果': 'score',
    '备注': 'remark',
}
report_header = {
    '用例编号': 'id',
    '用例标题': 'title',
    '测试功能点': 'testdot',
    '测试步骤': 'step',
    '操作': 'keyword',
    '页面': 'page',
    '元素': 'element',
    '测试数据': 'data',
    '输出数据': 'output',
    '预期结果': 'expected',
    '断言': 'assert',
    '设计者': 'designer',
    '步骤结果': 'score',
    '备注': 'remark',
}
header_custom = {'id': '用例编号', 'title': '用例标题', 'testdot': '测试功能点', 'step': '测试步骤',
                 'keyword': '操作', 'page': '页面', 'element': '元素', 'data': '测试数据', 'expected': '预期结果', 'assert': '断言',
                 'output': '输出数据',
                 'designer': '设计者', 'score': '步骤结果',
                 'remark': '备注'}

# case的文件的路径
file_case = str(Path('testcase') / ('testcase.xlsx'))
# element的文件的路径
file_element = str(Path('element') / ('elements.xlsx'))
# junit测试报告的路径
file_junit = str(Path('junit') / ('swapi' + '-' + 'junit' + '' + '.xml'))
# excel测试报告的路径
excel_report = str(Path('report') / ('swapi-report.xlsx'))
# 生成xml的测试报告
file_xml = str(Path('control/report') / ('swapi' + '-' + 'report' + '' + '.xlsx'))

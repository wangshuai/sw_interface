# coding=utf-8
from datetime import datetime
from control.data import suite2data, datatodict, suite_format
from control.testcase import TestCase
from control.utlis import Excel, creation_files
from control.log import logger
from email.mime.application import MIMEApplication
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from control.junit import Junit
from control.config import *
import threading
import requests
import time


class Autotest:
    def __init__(self, allocation):
        self.allocation = allocation
        # 用例表 强转为str类型 兼容jenkins运行
        self.file_case = file_case
        # 读取测试用例
        self.excel_case = Excel('r', self.file_case)
        # 转换数据格式为测试套件返回的可执行用例json
        self.test_suit = suite_format(datatodict(self.excel_case.read()))
        # 用于接受用例的结果
        self.result = []
        # 生成junit测试报告
        self.junit_report = file_junit
        # 以下为邮件配置
        self.report = excel_report
        self.junit = Junit()
        # 创建文件
        creation_files()

    def play(self):
        # 传入当前用例
        teastcase = TestCase(self.junit)
        # 读取测试套件执行用例
        for case in self.test_suit:
            # 跳过的用例
            if case['condition'] == 'skip':
                self.junit.case(case['id'], case['title'], datetime.now())
                self.junit.skip_case('This use case is skipped')
                self.junit.settime()
                for skip in case['steps']:
                    skip['score'] = 'skip'
                self.result.append(case)
                continue

            # 写入xml测试报告
            self.junit.case(case['id'], case['title'], datetime.now())
            # 使用线程增加运行速度
            thread = threading.Thread(target=self.result.append(teastcase.run(case)), name=case['title'])
            # 启动线程
            thread.start()
            # 收到测试的结果，进行生成测试报告

            # 参数1：出错的步骤数，参数2：未通过的步骤，参数3：用例总数，参数4：跳过的用例 用例总数-去执行的数
        self.junit.suite(teastcase.step_error, teastcase.step_fail, len(self.test_suit), '')
        self.junit.write_toxml()
        # 创建Excel测试报告
        self.crate_port()

    def crate_port(self):
        report_file = file_xml
        report_workbook = Excel('w', report_file)
        data = suite2data(self.result)
        report_workbook.write(data, 'API_report')
        # 写一次就关一次
        report_workbook.close()

    # 发送邮箱到测试报告
    def sendmail(self):
        msg = MIMEMultipart()
        msg['Subject'] = mali_dict['subject']  # 主题
        msg['From'] = mali_dict['send_user']  # 发件人
        msg['To'] = mali_dict['receive_users']  # 收件人

        # 构建正文
        part_text = MIMEText(mali_dict['email_text'])
        msg.attach(part_text)  # 把正文加到邮件体里面去

        # 构建邮件附件
        part_attach1 = MIMEApplication(open(self.report, 'rb').read())  # 打开附件
        part_attach1.add_header('Content-Disposition', 'attachment', filename='api-report.xlsx')  # 为附件命名
        msg.attach(part_attach1)  # 添加附件

        # 发送邮件 SMTP
        smtp = smtplib.SMTP(mali_dict['server_address'], 25)  # 连接服务器，SMTP_SSL是安全传输
        # smtp.set_debuglevel(1)
        smtp.login(mali_dict['send_user'], mali_dict['password'])
        smtp.sendmail(mali_dict['send_user'], mali_dict['receive_users'], msg.as_string())  # 发送邮件
        logger.info('邮件发送成功~~~~~~~~~~~~')

    def alarm(self):
        """
        1.首先获取未通过的用例进行发送
        2.获取到未通过的用例进行发送标题和步骤的数据
                1.步骤标题
                2.接口名称
                3.输出的数据
                4.不通过的原因
                5.参数
        """
        for r in self.result:
            for s in r['steps']:
                if s['score'] != 'Pass':
                    report = "标题：%s,用例总数：%s,url:%s,原因：%s,输出结果：%s" % (
                        s['testdot'], str(len(self.result)), s['element']['url'], str(s.get('_resultinfo')),
                        s['output'])
                    # 自己存放url，然后直接把拼接好的report 放进去发送钉钉消息即可，钉钉的链接自己写哦
                    url = '&text={ "msgtype": "text", "text": { "content": "%s" } }' % report




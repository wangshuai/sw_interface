# coding=utf-8
# /usr/bin/env python3

'''
Author: swang
Email: 13693554615@163.com

date: 2019-10-14 18:07
'''

# 操作Excel的工具类
from pathlib import Path

import xlrd
import xlsxwriter


class Excel():
    # 初始化方法 参数type：为r是读取excel，为w是写入excel获取不同的实例，参数file_name是将要读取的文件
    def __init__(self, type, file_name):
        # 读取excel
        if type == 'r':
            # 打开文件
            self.workbook = xlrd.open_workbook(file_name)
            # 获取到所有的sheet_names，sheet1,sheet2获取到所有，获取到的是一个list
            self.sheet_names = self.workbook.sheet_names()
            # 装载所有数据的list
            self.list_data = []
        # 写入Excel
        elif type == 'w':
            # 获取写入Excel的实例
            self.workbook = xlsxwriter.Workbook(file_name)

    def read(self):
        # 根据sheet_name读取用例，互殴去文件的总行数和每行的内容
        for sheet_name in self.sheet_names:
            # 通过每个sheet_name获取到每个页的内容
            sheet = self.workbook.sheet_by_name(sheet_name)
            # 获取总行数
            rosw = sheet.nrows
            # 根据总行数进行读取
            for i in range(0, rosw):
                rowvalues = sheet.row_values(i)
                # 将每一行的内容添加进去
                self.list_data.append(rowvalues)

        # 将得到的Excel数据返回进行处理
        return self.list_data

# 将元素和链接表处理为json格式方便查询
def element_tojson(element):
    elements = {}
    for e in element:
        elements[e[0]] = {'type': e[1], 'url': e[2]}
    return elements

'''
1.将Excel头部替换成英文的
2.处理成json格式
'''
def datatodict(data):
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
        '设计者': 'designer',
        '步骤结果': 'score',
        '备注': 'remark',
    }
    head = []
    list_dict_data = []
    for d in data[1]:
        # 获取到英文的头部内容，如果为中文，替换为英文，改为key
        # 传入两个参数的作用：查到则返回查到的数据，查不到则返回传入的原数据
        d = header.get(d, d)
        # 将去除的头部英文装进list中
        head.append(d)

    # 获取到数据进行切片处理，0坐标为标题，1坐标为头部
    for b in data[2:]:
        # 头部和内容拼接为json串
        dict_data = {}
        for i in range(len(head)):
            # 判断类型是为了防止出线str的错误，strip去除空格也有转str的用法
            if isinstance(b[i], str):
                dict_data[head[i]] = b[i].strip()
            else:
                dict_data[head[i]] = b[i]
        # list里面是字典格式
        list_dict_data.append(dict_data)
    return list_dict_data

def suite_format(data):
    # 用例套件list
    testsuite = []
    # 每个用例的testcase
    testcase = {}
    # 得到用例的所有数据
    # 循环遍历，判断里面是不是一组用例，生成用例集
    for d in data:
        # 判断用例有没有标题，没有标题则认为是统一用例，有标题则认为是第二条第三条用例，依次类推
        if d['id'].strip():
            # 判断是否为空 true false
            if testcase:
                # 不为空则只认为用例直接添加到list里面
                testsuite.append(testcase)
                # 将testcase置空
                testcase = {}
            # 生成用例的标题行，里面没有step
            for key in ('id', 'title', 'condition', 'testdot', 'designer', 'remark'):
                # test[key] 为id等值，d[key]为内容值
                testcase[key] = d[key]
            # 添加steps字段，并设置为list
            testcase['steps'] = []

        step = {}
        # 步骤里面添加control字段
        step['control'] = ''
        step['no'] = str(d['step'])
        for key in ('testdot', 'keyword', 'element', 'data', 'expected', 'output', 'score', 'remark'):
            step[key] = d.get(key, '')

        step['_keyword'] = d['keyword']
        step['_element'] = d['element']
        step['_data'] = d['data']
        step['_expected'] = d.get('expected', '')
        step['_output'] = ''
        step['_resultinfo'] = ''

    testcase['steps'].append(step)
    testsuite.append(testcase)

    return testsuite

def mkdir(p):
    path = Path(p)
    if not path.is_dir():
        path.mkdir()


if __name__ == "__main__":
    # file = '../element/elements.xlsx'
    # e = Excel('r', file)
    # list_read = e.read()
    # for i in list_read:
    #     print(i)
    # ele = element_tojson(list_read)
    # print(ele['获取短信验证码'])
    test_case = '../testcase/testcase.xlsx'
    e_case = Excel('r', test_case)
    # 打印输出结果
    # for case in e_case.read():
    #     print(case)
    re = e_case.read()
    # for c in datatodict(re):
    #     print(c)
    data = datatodict(re)
    testsuite = suite_format(data)
    print(testsuite)
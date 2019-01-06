# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: conf.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2018/12/10 下午4:52

import os
from unit.unit_time import time_test

"""
    不可修改目录
"""
DIRE_NAME = (os.path.dirname(os.path.dirname(__file__))+"/case/")
REPORT_DIRE_NAME = (os.path.dirname(os.path.dirname(__file__))+"/report/")
LOG_NAME = (os.path.dirname(os.path.dirname(__file__))+"/logs/")

"""
    文件类
"""
FILE_EXCEL = "case1.xls"  # case用例
SHEET_ID = 0  # sheet页
SAVE_FILE = time_test()+".xls"  # 测试之后文件存放名
FILE_JSON = "shuju.json"  # json数据

"""
    邮件类
"""
SEND_HOST = "smtp.qq.com"  # 发送地址的域名
SEND_USERNAME = ""  # 发件人
PASS_WORD = ""  # 发件人授权码
RECE_NAME = [""]  # 收件人邮箱

"""
    excel 文件类封装，可根据自己的进行修改
"""
EX_ID = "0"  # 目录id
EX_CASENAME = "1"  # 用例名
EX_URL = "2"  # url
EX_RUN = "3"  # 是否执行
EX_REQTYPE = "4"  # 请求类型
EX_HEADER = "5"  # 是否携带head
EX_CASEDEPEND = "6"  # 用例依赖
EX_CASEDEPENDDATA = "7"  # 依赖的返回数据
EX_CASEDEPENDFIELD = "8"  # 数据依赖字段
EX_DATA = "9"  # 请求数据，在json内查找，或者直接定义
EX_EXPECT = "10"  # 预期结果
EX_RESULT = "11"  # 实际结果
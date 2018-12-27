# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 定义常量，把 excel 的数据重新定义

from config import conf as cf


def get_id():
    # id
    return cf.EX_ID


def get_case_name():
    # 用例名
    return cf.EX_CASENAME


def get_url():
    # 用例url
    return cf.EX_URL


def get_is_run():
    # 用例是否执行
    return cf.EX_RUN


def get_request_type():
    # 用例请求类型
    return cf.EX_REQTYPE


def get_header():
    # header
    return cf.EX_HEADER

def get_header2():
    # 测试数据，假定写死header数据
    header = {
        "header":111,
        "cookie":"Yhzhuizhi",
        "id":12315,
    }
    return header

def get_case_depend():
    # 用例依赖
    return cf.EX_CASEDEPEND # G


def get_date_depend():
    # 依赖返回数据
    return cf.EX_CASEDEPENDDATA


def get_field_depend():
    # 数据依赖字段
    return cf.EX_CASEDEPENDFIELD


def get_data():
    # data数据
    return cf.EX_DATA


def get_expect():
    # 预期结果
    return cf.EX_EXPECT # K

def get_result():
    # 实际结果
    return cf.EX_RESULT # L


if __name__ == '__main__':
    print("id：", get_id())
    print("用例名：", get_case_name())
    print("用例url：", get_url())
    print("用例是否执行：", get_is_run())
    print("用例请求类型：", get_request_type())
    print("header：", get_header())
    print("用例依赖：", get_case_depend())
    print("依赖返回数据：", get_date_depend())
    print("数据依赖字段：", get_field_depend())
    print("data数据：", get_data())
    print("预期结果：", get_expect())
    print("实际结果：", get_result())
    print("测试数据",get_header2())

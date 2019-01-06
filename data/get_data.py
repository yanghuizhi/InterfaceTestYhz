# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 获取数据，整理数据集合

from unit.unit_json import ReadJson
from unit.unit_excel import ReadExcel
from config import data_config


class GetData:

    def __init__(self):
        self.readexcel = ReadExcel()

    # 获取excel行数，即 case 个数
    def get_case_lines(self):
        return self.readexcel.get_lines()

    # 获取用例id
    def get_id(self, row):
        col = int(data_config.get_id())
        id = self.readexcel.get_cell_value(row, col)
        return id

    # 获取用例名
    def get_name(self, row):
        col = int(data_config.get_case_name())
        name = self.readexcel.get_cell_value(row, col)
        return name

    # 获取是否执行
    def get_is_run(self, row):
        col = int(data_config.get_is_run())
        run_model = self.readexcel.get_cell_value(row, col)
        if run_model == "YES":
            flag = True
        else:
            flag = False
        return flag

    # 是否携带 header
    def is_header(self, row):
        col = int(data_config.get_header())
        header = self.readexcel.get_cell_value(row, col)
        # 方案一：写死数据，从方法里获取
        # if header == "yes":
        #     return data_config.get_header()
        # else:
        #     return None

        # 方案二：重新定义数据，不为空则使用，为空则不实用
        if header != "":
            return data_config.get_header()
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = int(data_config.get_request_type())
        request_method = self.readexcel.get_cell_value(row, col)
        return request_method

    # 获取url
    def get_request_url(self, row):
        col = int(data_config.get_url())
        url = self.readexcel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = int(data_config.get_data())
        data = self.readexcel.get_cell_value(row, col)
        if data == "":
            return None
        return data

    # 通过获取关键字拿到data数据
    def get_data_for_json(self, row):
        opera_json = ReadJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    # 获取预期结果
    def get_expect_data(self, row):
        col = int(data_config.get_expect())
        expect = self.readexcel.get_cell_value(row, col)
        if expect == "":
            return None
        return expect

    # 写入数据
    def write_result(self, row, value):
        col = int(data_config.get_result())
        self.readexcel.write_value(row, col, value)

    """
###############################################
            以下为依赖模块
###############################################    
    """

    # 获取依赖数据的key
    def get_depend_key(self, row):
        col = int(data_config.get_date_depend())
        depent_key = self.readexcel.get_cell_value(row, col)
        if depent_key == "":
            return None
        else:
            return depent_key

    # 判断是否有case依赖
    def is_depend(self, row):
        col = int(data_config.get_case_depend())    # 修改了这里
        depend_case_id = self.readexcel.get_cell_value(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    # 获取数据依赖字段
    def get_depend_field(self, row):
        col = int(data_config.get_field_depend())
        data = self.readexcel.get_cell_value(row, col)
        if data == "":
            return None
        else:
            return data


if __name__ == '__main__':
    run = GetData()
    for i in range(0,run.get_case_lines()):
        print(run.get_name(i))
        print(run.is_depend(i))
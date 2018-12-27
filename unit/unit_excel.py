# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    读取Excel

须知：
    1、目前只能使用 copy 来操作写入新的 excel
    2、copy 保存实质上是通过 xlwt 进行保存的
    2、通过 xlwt 只能写入 xls 文件,不能写入 xlsx 文件
"""

import xlrd
from config import conf as cf
from xlutils.copy import copy
import xlwt
class ReadExcel(object):

    def __init__(self):
        # 初始化文件和sheet页
        self.file_name = cf.DIRE_NAME + cf.FILE_EXCEL
        self.sheet_id = cf.SHEET_ID
        self.data = self.get_data()

    # 获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)  # 只能读取内容
        write_data = copy(read_data)  # 复制
        sheet_data = write_data.get_sheet(cf.SHEET_ID)
        sheet_data.write(row, col, value)
        # 有一个已知bug，
        # 当将数据写入新文件时，在判断是否运行里面则无法运行下去，只能写入源文件，失败
        # write_data.save(cf.REPORT_DIRE_NAME + cf.SAVE_FILE)
        write_data.save(self.file_name)

    """
###############################################
            以下为依赖模块
###############################################    
    """

    # 根据对应的case_id 找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    # 根据对应的case_id找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        clogs_data = self.get_cols_data()
        for col_data in clogs_data:
            if case_id in col_data:
                return num
            num += 1

    # 根据行号，找到该行的内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列的内容(单元格内容)，整个一列的内容
    def get_cols_data(self, col_id=None):
        if col_id is not None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    ee = ReadExcel()
    # print(ee.get_data())
    # print(ee.get_lines())

    case_id = "yhz-3"
    row = 3
    # 根据对应的 case_id 找到对应行的内容
    print(ee.get_rows_data(case_id))
    # 根据对应的case_id找到对应的行号
    print(ee.get_row_num(case_id))
    # 根据行号，找到该行的内容，
    print(ee.get_row_values(row))
    # 获取某一列的内容(单元格内容)，整个一列的内容
    print(ee.get_cols_data())

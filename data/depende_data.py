# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    处理数据依赖的所有问题
"""
import json
from unit.unit_excel import ReadExcel
from unit.unit_method import RequestMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse  # 第三方库


class DependdentData(object):

    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = ReadExcel()
        self.data = GetData()

    # 通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    # 执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RequestMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = run_method.run_main(method, url, request_data, header)
        return json.loads(res)

    # 根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self, row):
        depend_data = self.data.get_depend_key(row) # 实际上是"yhz-1"
        # print("depend_data", depend_data)
        response_data = self.run_dependent()    # 返回data数据
        # print("数据：", response_data)
        json_exe = parse(depend_data)
        # print(json_exe)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]

if __name__ == '__main__':
    order={
          "data": [],
          "errorCode": 1006,
          "errorDesc": "token error",
          "status": 1,
          "timestamp": 1122334455
            }
    res = "timestamp"
    json_exe=parse(res)
    madle=json_exe.find(order)
    print([math.value for math in madle][0])

    ee = DependdentData("yhz-1")
    print(ee.get_data_for_key(2))
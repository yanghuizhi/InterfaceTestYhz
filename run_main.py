# !/usr/bin/env python
# -*- coding: utf-8 -*-

from unit.unit_method import RequestMethod  # 请求方法
from data.get_data import GetData           # data数据
from common.comparison import Comparison    # 结果比对
from data.depende_data import DependdentData    # 依赖问题
from unit.unit_email import SendEmail           # 邮件发送


class RunMain:
    def __init__(self):
        self.run_method = RequestMethod()
        self.data = GetData()
        self.compar_unil = Comparison()  # 引入并实例化
        self.send_mai = SendEmail()

    # 程序执行的
    def go_on_run(self):

        pass_count, fail_count = [], [] # 统计
        rows_count = self.data.get_case_lines() # case 行数

        for i in range(1, rows_count):  # 排除第一行标题 0
            is_run = self.data.get_is_run(i)

            if is_run:  # 判断是否运行
                id = self.data.get_id(i)    # 用例名：暂时没用
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                expect = self.data.get_expect_data(i)  # 获得预期结果
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)  # 判断是否有依赖
                # res = self.run_method.run_main(
                #     method,
                #     url,
                #     data,
                #     header
                # )

                if depend_case is not None:  # 获取依赖
                    self.depend_data = DependdentData(depend_case)
                    # 获取依赖的key
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_response_data

                res = self.run_method.run_main(
                    method,
                    url,
                    request_data,
                    header
                )
                # print(id,res)
                if self.compar_unil.is_contain(expect, res):  # 结果判断
                    self.data.write_result(i, "pass")  # 回写数据
                    pass_count.append(i)    # 统计成功个数
                    # print(i,"测试通过")
                else:
                    self.data.write_result(i, res)  # 回写数据
                    fail_count.append(i)    # 统计失败个数
                    # print(i,"测试失败")

        # 发送邮件
        # self.send_mai.send_main(pass_count, fail_count)

        # print("通过用例为：", pass_count, " 总计： ", len(pass_count))
        # print("失败个数为：", fail_count, " 总计： ", len(fail_count))
        print("测试结束！")

if __name__ == '__main__':
    run = RunMain()
    print(run.go_on_run())

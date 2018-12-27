# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from config import conf as cf


class ReadJson:

    def __init__(self):
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(file=cf.DIRE_NAME+cf.FILE_JSON, encoding="utf-8") as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self, ID):
        return self.data[ID]

if __name__ == '__main__':
    opjson = ReadJson()
    print(opjson.get_data("login")["os"])

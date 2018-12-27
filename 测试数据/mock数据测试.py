# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: mock数据测试.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2018/12/22 下午3:51


import json
import requests
from 测试数据.unit_mock import mock_test

class RequestMethod(object):

    def __init__(self):
        pass

    def post_main(self, url, data, header=None):
        if header is not None:
            res = requests.post(url=url, data=data, header=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def get_main(self, url, data=None, header=None):
        if header is not None:
            res = requests.get(url=url, data=data, headers=header)
        else:
            res = requests.get(url=url, data=data, )
        return res.text

    def run_main(self, method, url, data=None, header=None):
        if method == "POST":
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)


if __name__ == '__main__':
    import time
    url = "http://coding.imooc.com/api/cate"
    data = {
        "timestamp": str(int(time.time()*1000)),
        "secrect": "078474b41dd37ddd5efeb04aa591ec12",
        "tocken": "0b4c502ba647664be04dfedb32ad4f3d",
        "id": 123,
    }

    mock_test(RequestMethod.run_main, data,url,'POST',data)
    res=RequestMethod()
    ress=res.run_main('POST',url,data)
    if data['id'] == 123:
        print("测试通过")
        print(ress)
        print(ress[3])
        # if ress['status'] == 1:
        #     print("1")
    else:
        print("测试失败")
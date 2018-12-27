# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json


class RequestMethod(object):

    def __init__(self):
        pass

    def post_main(self, url, data, header=None):

        # 老方法作废
        # res = requests.post(url=url, data=data).json()
        # return json.dumps(res, indent=2, sort_keys=True)

        if header is not None:
            res = requests.post(url=url, data=data, header=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def get_main(self, url, data=None, header=None):

        # 老方法作废
        # res = requests.get(url=url, data=data).json()
        # return json.dumps(res, indent=2, sort_keys=True)

        if header is not None:
            res = requests.get(url=url, data=data, headers=header)
        else:
            res = requests.get(url=url, data=data, )

        return res.json()
        # return res.text   # 如果返回json报错，则更改成text

    def run_main(self, method, url, data=None, header=None):

        # 老方法作废
        # if method == "GET":
        #     res = self.send_get(url, data)
        # else:
        #     res = self.send_get(url, data)
        # return res

        if method == "POST":
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)


if __name__ == '__main__':
    url1 = "http://coding.imooc.com/api/cate"
    url2 = "http://t.weather.sojson.com/api/weather/city/101181101"
    data1 = {
        "timestamp": "1507006626132",
        "uid": "5249191",
        "uuid": "5ae7d1a22c82fb89c78f603420870ad7",
        "secrect": "078474b41dd37ddd5efeb04aa591ec12",
        "tocken": "0b4c502ba647664be04dfedb32ad4f3d",
        "cid": "0",
    }

    req = RequestMethod()
    # re11 = req.post_main(url=url1, data=data1)  # 非json模式
    re1 = req.run_main("POST",url=url1, data=data1)

    re2 = req.run_main("GET",url=url2)
    # print("post 数据：", re1)
    # print("get 数据：", re2)


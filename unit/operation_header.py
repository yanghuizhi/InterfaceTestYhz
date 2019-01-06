# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: operation_header.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/1/5 3:14 PM

import requests

url = "http://m.imooc.com/passport/user/login"
data = {
    "username":"18271670195",
    "password":"www2932097",
    "verify":"",
    "referer": "https://m.imooc.com",
}
res = requests.post(url,data).json()
# print(res)
"""
{'status': 10001, 'msg': '成功', 'data': {'userInfo': {'uid': '6680857'}, 'url': ['http://www.imooc.com/user/ssologin?token=ovI4t3ttncgy4x7mwL7pOYYJ7b_UfQAgWnOcleLo0N5VW5SNgt0RXHb9Yuy3qUNYyI4Re89hshf9RlI-35QHe7O741u7wY53u06d9mRZ57PO9bVPYLK9kir0NKLp6refhf3qfEpQDYkumBL87qh8NzFlyOgfqg1LCww7IVV9tp54ZaOEBgKfhanIKAxOgWK-sCaDc4pGT0onoGcAjP3mU3NPDZwIl3KgfUxix4Jhc423A8TQ0-JsHFd7bkKp_QD1-50O3YQZiC7o', 'http://coding.imooc.com/user/ssologin?token=vXLTLZnvUGD9F8QAYC1NPXvyRBURDecoPvUXMhzrgYPrVGvqDxdIoeHG3sr54DOShJAYl8UTGMnAp-o3YKYNKoNrqjyfU2b3k7Nl3jJdJdk9B4j0xWCKQU50j5VxvVNC4vJN6_PmrKs3E8ypxQtNHJXl20SkahmtyxC4GefUFvw-Gb1XxAzXtEiGCLDGvzzohPUcvW-x4DV5o9iozB0Jxa2oxXM4y554g9k9vgZNIDDIVo0cKb5oZvq2hSqYPkBv-pfVNUvnO8']}}
"""
response_url = res['data']['url'][0]
request_url = response_url+""
cookie = requests.get(request_url).cookies

# requests.utils.dict_from_cookiejar(cookie)
# print(cookie["apsid"])
url1 = "新的地址"
# print(requests.get(url=url1,cookie=cookie).text)
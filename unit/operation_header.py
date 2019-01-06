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

response_url = res['data']['url'][0]
# http://www.imooc.com/user/ssologin?token=Es3TjyT2xj3On3AjdlTHF5qB9L-SbkWCMBZulXd7DSyYwr9zCEnnRNVG9EKHU2h08o1f8CaEgpfDYKE4wMExxCLF9PStUvsH-bNpiwqdZCyDg_4DwKVBcU11tUIKNgSxTnH3RmbwVoWKmzrY0i1LN6zwEGzgM9D7S-2OQR4v1FcCEZlDpz8I3uQc7fhtGOxGGM973P5BIT5JQsq1uHf7g3qtg8-smSk5gUfIczW27uzTl9CuFRBdInrcGpKmzvPz-qmgy43bkf

request_url = response_url+"&callback=jQuery191004342300488107509_1546761851114"
cookie = requests.get(request_url).cookies

# <RequestsCookieJar[<Cookie apsid=NlNzZkMThmNWJmNTc4MmEzNjY5YzdjNmQ0OWRjMmIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANjY4MDg1NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADgzYjlhN2FjMDJjODYyZmQ2Mjc4ZTk0ZTQxNzZiMjhir7gxXK%2B4MVw%3DMG for .imooc.com/>, <Cookie cvde=5c31b8af4649b-1 for .imooc.com/>, <Cookie imooc_isnew=1 for .imooc.com/>, <Cookie imooc_isnew_ct=1546762415 for .imooc.com/>, <Cookie imooc_uuid=11947d05-875e-49cf-90f2-f59b2f7681d8 for .imooc.com/>, <Cookie loginstate=1 for .imooc.com/>]>

# cookie = requests.utils.dict_from_cookiejar(cookie)
# print(cookie["apsid"])

url1 = "https://order.imooc.com/pay/cartorder?jsonpcallback=jQuery1113023891953999072268_1546762895967&_=1546762895968"
print(requests.get(url=url1,cookies=cookie).text)
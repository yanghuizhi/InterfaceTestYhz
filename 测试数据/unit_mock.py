# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: unit_mock.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2018/12/22 下午3:33

# 模拟mock方法

from mock import mock

def mock_test(mock_method,request_data,url,method,response_data):
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url,method,request_data)
    return res
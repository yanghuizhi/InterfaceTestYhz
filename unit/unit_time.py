# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: unit_time.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2018/12/23 上午10:53

import time
import locale

locale.setlocale(locale.LC_CTYPE, "")

def date_time_chinese():
    """
    :return: 当前北京时间
    """
    return time.strftime("%Y年%m月%d日 %H时 %M分 %S秒", time.localtime())

def date_time_timestamp():
    """
    :return: 当前时间戳
    """
    return str(int(time.time()*1000))

def time_test():
    """
    :return: 当前北京时间
    """
    return time.strftime("%Y年%m月%d日%H%M%S", time.localtime())

if __name__ == '__main__':
    print(date_time_timestamp())
    print(date_time_chinese())
    print(time_test())
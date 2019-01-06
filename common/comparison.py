# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    将放回的文件和原文件对比
"""
import json
from filecmp import cmp


class Comparison(object):

    def is_contain(self, str_one, str_two):
        """
        判断一个字符串是否在另一个字符串中
        :param str_one: 查找的字符串
        :param str_two: 被查找的字符串
        :return:
        """
        flag = None
        if isinstance(str_one, str):
            str_one = str_one.encode("utf-8").decode("utf-8")
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag


    # 字典对比,判断两个字典是否想等
    def is_equal_dict(self,dict_one,dict_two):

        if isinstance(dict_one,str):
            dict_one=json.loads(dict_one)
        if isinstance(dict_one,str):
            dict_two=json.loads(dict_two)
        return cmp(dict_one,dict_two)
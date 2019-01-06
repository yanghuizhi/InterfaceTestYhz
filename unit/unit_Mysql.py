# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: unit_Mysql.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/1/6 11:08 AM

import pymysql
import json


class OperationMysql(object):

    def __init__(self):
        self.con = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="123456",
            db="yhz_study",
            charset="utf8",
            cursorclass = pymysql.cursors.DictCursor    # 字典模式
        )
        self.cur = self.con.cursor()

    # 查询一条数据
    def search_one(self,sql):
        self.cur.execute(sql)
        resu = self.cur.fetchall()
        result = json.dumps(resu)
        return result

    def closeDB(self):
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.con.close()

if __name__ == '__main__':
    op_mysql = OperationMysql()

    sql1 = "select * from web_user where Name='mushishi'"
    sql2 = "select * from web_user"
    ss = op_mysql.search_one(sql1)
    print(ss)


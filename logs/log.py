# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: log.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2018/12/22 下午3:51

import logging
import time
import config.conf as cf

filename = time.strftime('%Y-%m-%d-%H%M%S', time.localtime(time.time()))

def initLogging(message):

    logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s',
        # datefmt  = '%a, %d %b %Y %H:%M:%S',
        filename =  cf.LOG_NAME + filename + ".log",
        filemode = 'w')

    logger = logging.getLogger(__name__)

    logger.info(message)

initLogging('123')
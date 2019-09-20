#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 22:02
# @Author  : rain
# @File    : logger.py
# @Software: PyCharm

import logging

FORMAT_STR = "%(asctime) %(levelname)s (model) ::%(message)s"

class ConsoleLogger(object):


    def __new__(cls, name = '%(module)s'):
        __format = "%(asctime) %(levelname)s (model) {model}::%(message)s".format(model=name)
        __logger = logging.getLogger(name)
        __logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(__format)
        handler.setFormatter(handler)
        __logger.addHandler(handler)
        return __logger
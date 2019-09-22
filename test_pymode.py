#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2018/9/22

import time

'''
演示：
1.可直接运行
2.用命令行执行
    在文件目录下;
    pytest  test_XX.py   
'''


def add(x, y):
    return x + y


def test_add():
    assert add(1, 2) == 3


def test_add2():
    print("I am 2")
    time.sleep(3)
    assert add(1.2, 3.1) == 5.3
    assert add(1, 2) == 3

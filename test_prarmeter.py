#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/22

import pytest
import random

'''
Pytest-参数化:
'''


# 单个参数化，前面1个变量，后面是对应的数据；
@pytest.mark.parametrize("x", [(1), (2), (6)])
def test_add(x):
    print(x)
    assert x == random.randrange(1, 7)


# 2个参数化，前面两个变量，后面是对应的数据；
@pytest.mark.parametrize("x,y", [
    (9, 9),
    (2, 2),
    (42, 42),
    ("testerhome", "testerhome"),
])
def test_add2(x, y):
    assert x == y


# 可以运算符
@pytest.mark.parametrize("x,y", [
    (3 + 5, 9),
    (2 + 4, 6),
    (6 * 9, 42),
    ("testerhome", "testerhome"),
])
def test_add(x, y):
    assert x == y


# 多个参数化，前面两个变量，后面是对应的数据；
@pytest.mark.parametrize("x,y,z", [
    (3 + 5, 9, 8),
    (2 + 4, 6, 9),
    (6 * 9, 42, 9),
    ("testerhome", "testerhome", "new"),
])
def test_multiple_add(x, y, z):
    assert x == y + z

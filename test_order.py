#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/30

import pytest


def test_01():
    print('test01')


# last:最后一个执行
@pytest.mark.last
def test_02():
    print('test02')


# skip:跳过
@pytest.mark.skip
def test_03():
    print('test03')


# run(order=1):第一个执行
@pytest.mark.run(order=1)
def test_04():
    print('test04')


if __name__ == '__main__':
    pytest.main(['-v'], ['test_order.py'])
    """
    执行顺序：
    test04
    test01
    test02
    """

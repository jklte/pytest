#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/30

import pytest


@pytest.fixture(params=[1, 2, 3])
def test_data(request):
    return request.param


def test_one(test_data):
    print('\ntest data: %s' % test_data)
    '''
    运行此函数：
    返回结果：
    test data: 1
    .
    test data: 2
    .
    test data: 3
    '''

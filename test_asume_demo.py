#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/22

import pytest

'''
演示assume功能；报错后，继续往下执行
'''


def test_multiple_assert():
    pytest.assume(1 == 2)
    pytest.assume(2 == 2)
    pytest.assume(3 == 2)

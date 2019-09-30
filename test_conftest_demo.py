#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/30

import pytest


def test_s1(login):
    print('用例1，登陆后执行其它功能操作')


if __name__ == '__main__':
    pytest.main(['-v'], ['test_conftest_demo.py'])

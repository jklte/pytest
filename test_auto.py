#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/30

import pytest

"""
start设置scope为module级别，在当前.py用例模块只执行一次，autouse=True自动使用
open_home设置scope为function级别，每个用例前都调用一次，自动使用
"""


@pytest.fixture(scope="module", autouse=True)
def start(request):
    print('\n-----开始执行moule----')
    print('module      : %s' % request.module.__name__)
    print('----------启动浏览器---------')
    yield
    print("------------结束测试 end!-----------")


class TestIndex(object):
    @pytest.fixture(scope="function", autouse=True)
    def open_home(self, request):
        print("function：%s \n--------回到首页--------" % request.function.__name__)

    def test_01(self):
        print('-----------用例01--------------')

    def test_02(self):
        print('-----------用例02------------')


if __name__ == "__main__":
    pytest.main(["-s", "test_auto.py"])

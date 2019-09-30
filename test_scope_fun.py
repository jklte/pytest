#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/30

import pytest

'''
scope为 function级别
 每一个函数或方法都会调用
'''


class TestIndex(object):
    @pytest.fixture(scope="function")
    def open_home(self, request):
        print("function：%s \n--------回到首页--------" % request.function.__name__)

    def test_01(self, open_home):
        print('-----------用例01--------------')

    def test_02(self, open_home):
        print('-----------用例02------------')


if __name__ == "__main__":
    pytest.main(["-s", "test_scope_fun.py"])

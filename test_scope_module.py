#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/30

import pytest

"""
scope=module
fixture为module级别时在当前.py脚本里面所有用例开始前只执行一次
"""


@pytest.fixture(scope="module")
def first():
    print("\n获取用户名，scope为module级别当前.py模块只运行一次")
    a = "yoyo"
    return a


def test_1(first):
    '''用例传fixture'''
    print("测试账号：%s" % first)
    assert first == "Haul"


class TestCase(object):
    def test_2(self, first):
        '''用例传fixture'''
        print("测试账号：%s" % first)
        assert first == "Haul"


if __name__ == '__main__':
    pytest.main(["-s", "test_scope_module.py"])
    """
    返回结果：
    test_scope_module.py 
    获取用户名，scope为module级别当前.py模块只运行一次
    .测试账号：Haul
    .测试账号：Haul
    """

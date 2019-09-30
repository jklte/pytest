#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/30

import pytest

'''
scope为class
fixture为class级别的时候，如果一个class里面有多个用例，都调用了此fixture，
那么此fixture只在该class里所有用例开始前执行一次
'''


@pytest.fixture(scope="class")
def first():
    print("\n获取用户名，scope为class级别只运行一次")
    a = "nuo"
    return a


class TestCase(object):
    def test_1(self, first):
        '用例传fixture'
        print("测试账号：%s" % first)
        assert first == "nuo"

    def test_2(self, first):
        '用例传fixture'
        print("测试账号：%s" % first)
        assert first == "nuo"


if __name__ == '__main__':
    pytest.main(["-s", "test_scope_class.py"])
    '''
    class级别 只在类里面运行一次，不管调用多少次
    
    返回结果：
    获取用户名，scope为class级别只运行一次
    .测试账号：nuo
    .测试账号：nuo
    '''

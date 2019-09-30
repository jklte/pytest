#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/30

import pytest


@pytest.fixture()
def open_browser():
    print("\n打开浏览器，打开百度首页")

    yield

    print('执行teardown')
    print('最后关闭浏览器')


@pytest.mark.usefixtures('open_browser')
def test_soso():
    print('case1: 登际后执行搜索')


def test_cakan():
    print('case2:不登陆就看')


@pytest.mark.usefixtures('open_browser')
def test_cart():
    print('case3,登陆，加购物车')


if __name__ == '__main__':
    pytest.main(['-s', 'test_fixture.py'])
    '''
    结果返回：
    test_yield.py 
    打开浏览器，打开百度首页
    .case1: 登际后执行搜索
    执行teardown
    最后关闭浏览器
    .case2:不登陆就看

    打开浏览器，打开百度首页
    .case3,登陆，加购物车
    执行teardown
    最后关闭浏览器
    '''

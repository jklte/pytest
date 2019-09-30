#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/30

import pytest
import sys


# scope=function

def f():
    return 3


@pytest.mark.skip   # 跳过
def test_cakan():
    print('case2:不登陆就看')
    assert f() == 4
    '''
    运行此函数：返回结果：
    Skipped: unconditional skip
    '''


environment = 'android'


@pytest.mark.skipif('environment=="android"', reason='android平台没有这个功能')
def test_cart_3(login):
    print('case3,登陆，点击苹果图标')
    '''
    运行此函数：返回结果：
    Skipped: android平台没有这个功能
    '''


@pytest.mark.skipif(sys.platform == 'win32', reason='不在windows下运行')
@pytest.mark.skipif(sys.version_info < (3, 6), reason='3.6版本以下不执行，您需要更高版本')
def test_cart(login):
    print('case3,登陆，点击苹果图标，3.6以下版本无法执行')
    '''
    运行此函数：返回结果：
    Skipped: 不在windows下运行
    '''


@pytest.mark.xfail  # 标记预计是失败的
def test_xfail():
    print(broken_fixture())
    '''
    运行此函数：返回结果：
    "Sorry, it's 中断异常."
    '''


def broken_fixture():
    raise Exception("Sorry, it's 中断异常.")

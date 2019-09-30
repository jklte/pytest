#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/30

import pytest  # 1.导入pytest


@pytest.fixture()  # 2.添加pytest.fixture()装饰圈
def login():  # 登录的函数名
    print('登录了')


class TestMode(object):
    @pytest.mark.usefixtures('login')  # 3.在想使用的函数上，传入函数名login
    def test_shopping(self):
        print('购物车，需要登录')

    def test_cat(self):  # 4.不需要使用就不用传
        print('查看，不需要登录')

    def test_info(self):
        print('个人信息，需要登录')


if __name__ == '__main__':
    '''
    可以用pycharm自带运行，也可以用main方式运行；注意文件名
    '''
    pytest.main(["-v"], ['test_fixtures_02.py'])

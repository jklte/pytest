#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/30

import pytest


@pytest.mark.webtest
def test_send_http():
    print('01')


@pytest.mark.apptest
def test_devide():
    print('02')


@pytest.mark.android
def test_search():
    print('03')


@pytest.mark.ios
def test_add():
    print('04')


def test_plus():
    print('05')


if __name__ == '__main__':
    pytest.main()

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/30

import pytest


@pytest.fixture()
def login():
    print('"\n输入用户名密码登陆！"')


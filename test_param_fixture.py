#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/30

# import pytest

# test_user_data = ["jklte", "zhanghao"]
#
#
# @pytest.fixture(scope="module")
# def login_r(request):
#     # 这是接收传入的参数，接收一个参数
#     user = request.param
#     print("\n打开首页准备登陆，登陆用户:%s" % user)
#     return user
#
#
# # 这是pytest的参数化数据驱动，indeirect=True 是把login_r当作函数去执行
# @pytest.mark.parametrize("login_r", test_user_data, indirect=True)
# def test_login(login_r):
#     # 登陆用例
#     a = login_r
#     print("测试用例中login的返回值：%s" % a)
#     assert a != ""
#     """
#     运行次函数：返回结果：
#     打开首页准备登陆，登陆用户:jklte
#     .测试用例中login的返回值：jklte
#
#     打开首页准备登陆，登陆用户:zhanghao
#     .测试用例中login的返回值：zhanghao
#     """

import pytest

test_user_data = [{"user": "Haul", "password": "1234"},
                  {"user": "jklte", "password": "123456"},
                  {"user": "test01", "password": ""}]


@pytest.fixture(scope="module")
def login_r(request):
    # 可以通过dict形式，虽然传递一个参数，但通过key的方式可以达到类似传入多个参数的效果
    user = request.param['user']
    pwd = request.param['password']

    print("\n打开首页准备登陆，登陆用户:%s，密码:%s" % (user, pwd))
    if pwd:
        return True
    else:
        return False


# 这是pytest的参数化数据驱动，indeirect=True 是把login_r当作函数去执行
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    # 登陆用例
    a = login_r
    print("测试用例中login的返回值：%s" % a)
    assert a  # 失败的原因，密码为空
    '''
    运行此函数，返回结果：
    打开首页准备登陆，登陆用户:Haul，密码:1234
    .测试用例中login的返回值：True
    
    打开首页准备登陆，登陆用户:jklte，密码:123456
    .测试用例中login的返回值：True
    
    打开首页准备登陆，登陆用户:test01，密码:
    F测试用例中login的返回值：False
    '''

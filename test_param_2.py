#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2019/9/30

import pytest

test_user_data1 = [{"user": "zhang", "password": "888888"},
                   {"user": "jklte", "password": "123456"},
                   {"user": "test01", "password": ""}]

test_user_data2 = [{"q": "中国平安", "count": 3, "page": 1},
                   {"q": "阿里巴巴", "count": 2, "page": 2},
                   {"q": "pdd", "count": 3, "page": 1}]


@pytest.fixture(scope="module")
def login_r(request):
    # 这是接收传入的参数，接收一个参数
    user = request.param['user']
    password = request.param['password']

    print("\n用户名:%s，密码:%s" % (user, password))


@pytest.fixture(scope="module")
def query_param(request):
    q = request.param['q']
    count = request.param['count']
    page = request.param['page']
    print("查询的搜索词：%s" % q)
    return request.param


# 这是pytest的参数化数据驱动，indeirect=True 是把login_r当作函数去执行
# 从下往上执行
# 两个数据进行组合测试有3*3个测试用例执行（test_user_data1的个数*test_user_data2的个数）
@pytest.mark.parametrize("query_param", test_user_data2, indirect=True)
@pytest.mark.parametrize("login_r", test_user_data1, indirect=True)
def test_login(login_r, query_param):
    # 登陆用例
    print(login_r)
    print(query_param)
    """
    运行此函数，返回结果：
    用户名:zhang，密码:888888
    查询的搜索词：中国平安
    .None
    {'q': '中国平安', 'count': 3, 'page': 1}
    查询的搜索词：阿里巴巴
    .None
    {'q': '阿里巴巴', 'count': 2, 'page': 2}
    
    用户名:jklte，密码:123456
    .None
    {'q': '阿里巴巴', 'count': 2, 'page': 2}
    查询的搜索词：中国平安
    .None
    {'q': '中国平安', 'count': 3, 'page': 1}
    查询的搜索词：pdd
    .None
    {'q': 'pdd', 'count': 3, 'page': 1}
    
    用户名:zhang，密码:888888
    .None
    {'q': 'pdd', 'count': 3, 'page': 1}
    
    用户名:test01，密码:
    .None
    {'q': 'pdd', 'count': 3, 'page': 1}
    查询的搜索词：阿里巴巴
    .None
    {'q': '阿里巴巴', 'count': 2, 'page': 2}
    查询的搜索词：中国平安
    .None
    {'q': '中国平安', 'count': 3, 'page': 1}
    """

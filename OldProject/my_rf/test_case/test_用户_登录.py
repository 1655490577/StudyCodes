#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 22:59
# @Blog    : http://www.cnblogs.com/uncleyong
# @Gitee   : https://gitee.com/uncleyong
# @QQ交流群 : 652122175
# @公众号   : 全栈测试笔记


import os, sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
import unittest
import requests
from lib import HTMLTestRunner
from lib import logger
from lib.tools import p
from conf.settings import PROJECT_IP
from conf.settings import PROJECT_PORT


class UserLogin(unittest.TestCase):
    def setUp(self):
        print('测试用例开始执行...self的id是：', str(id(self)))
        self.url = 'http://' + PROJECT_IP + ':' + PROJECT_PORT + '/login'

    def tearDown(self):
        print('测试用例执行完成...')

    def test_user_login_ok(self):
        """登录成功"""
        print('test_user_login_ok: ', str(id(self)))
        logger.logger.logger.debug('当前方法: %s' % p.get_current_function_name())
        params = {"username": 'qzcsbj', "password": '123456'}  # get请求，参数也可以写为字典格式
        try:
            # 传表单
            res = requests.post(url=self.url, params=params, verify=False, timeout=10).json()
        except Exception as e:
            res = {'code': '999', 'msg': '连接错误。'}
        logger.logger.logger.debug('是测试点【%s】下的用例【%s: %s】,返回的结果【%s】' % (
        self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__, p.get_current_function_name(), res))

        self.assertEqual(res['code'], 9420)

    def test_user_login_fail(self):
        """用户名或密码不正确"""
        print('test_user_login_fail: ', str(id(self)))
        params = {"username": 'qzcsbj', "password": '0123456'}
        try:
            res = requests.post(url=self.url, params=params, verify=False, timeout=10).json()
        except Exception as e:
            res = {'code': '999', 'msg': '连接错误。'}
        logger.logger.logger.debug('是测试点【%s】下的用例【%s: %s】,返回的结果【%s】' % (
        self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__, p.get_current_function_name(), res))

        self.assertEqual(res['code'], 9410)

    def test_user_login_no_phone(self):
        """未填写用户名"""
        print('test_user_login_no_phone: ',str(id(self)))
        params = {"username": '', "password": '123456'}
        try:
            res = requests.post(url=self.url, params=params, verify=False, timeout=10).json()
        except Exception as e:
            res = {'code': '999', 'msg': '连接错误。'}
        logger.logger.logger.debug('是测试点【%s】下的用例【%s: %s】,返回的结果【%s】' % (
        self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__, p.get_current_function_name(), res))

        self.assertEqual(res['code'], 9400)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(UserLogin("test_user_login_ok"))
    suit.addTest(UserLogin("test_user_login_fail"))
    suit.addTest(UserLogin("test_user_login_no_phone"))
    fp = open("./report_debug.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'**项目接口自动化测试报告', description=u'**项目接口自动化测试报告')
    runner.run(suit)
    fp.close()

# if __name__ == '__main__':
#     unittest.main()
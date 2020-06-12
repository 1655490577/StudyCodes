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


class UserAdd(unittest.TestCase):
    def setUp(self):
        print('测试用例开始执行...')
        self.url = 'http://' + PROJECT_IP + ':' + PROJECT_PORT + '/add_user4'
        # 获取token
        from lib import login_token
        self.token = login_token.get_token('qzcsbj', '123456')
        print(self.token)
        self.headers = {'content-type': 'application/json'}

    def tearDown(self):
        print('测试用例执行完成...')

    def test_user_add_ok(self):
        """添加成功"""
        logger.logger.logger.debug('当前方法: %s' % p.get_current_function_name())
        payload = {"token":self.token,"username":"test133","realname":"test133","sex":"1","phone":"13800000133","adduser":"qzcsbj"}
        try:
            res = requests.post(url=self.url, json=payload,headers=self.headers).json()
        except Exception as e:
            res = {'code': '999', 'msg': '连接错误。'}
        logger.logger.logger.debug('是测试点【%s】下的用例【%s: %s】,返回的结果【%s】' % (
        self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__, p.get_current_function_name(), res))

        self.assertEqual(res['code'], 9550)

    def test_user_add_exist(self):
        """手机号已经存在"""
        payload = {"token": self.token, "username": "test13", "realname": "test130", "sex": "1",
                   "phone": "13800000130", "adduser": "qzcsbj"}
        try:
            res = requests.post(url=self.url, json=payload, headers=self.headers).json()
        except Exception as e:
            res = {'code': '999', 'msg': '连接错误。'}
        logger.logger.logger.debug('是测试点【%s】下的用例【%s: %s】,返回的结果【%s】' % (
        self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__, p.get_current_function_name(), res))

        self.assertEqual(res['code'], 9360)

    def test_user_add_no_phone(self):
        """未填写手机号"""
        payload = {"token": self.token, "username": "test131", "realname": "test131", "sex": "1",
                   "phone": "", "adduser": "qzcsbj"}
        try:
            res = requests.post(url=self.url, json=payload, headers=self.headers).json()
        except Exception as e:
            res = {'code': '999', 'msg': '连接错误。'}
        logger.logger.logger.debug('是测试点【%s】下的用例【%s: %s】,返回的结果【%s】' % (
        self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__, p.get_current_function_name(), res))

        self.assertEqual(res['code'], 9500)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(UserAdd("test_user_add_ok"))
    suit.addTest(UserAdd("test_user_add_exist"))
    suit.addTest(UserAdd("test_user_add_no_phone"))
    fp = open("./report_debug.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'**项目接口自动化测试报告', description=u'**项目接口自动化测试报告')
    runner.run(suit)
    fp.close()

    # if __name__ == '__main__':
    #     unittest.main()
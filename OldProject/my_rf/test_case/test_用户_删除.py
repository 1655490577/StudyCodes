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


class UserDel(unittest.TestCase):
    def setUp(self):
        print('测试用例开始执行...')
        self.url = 'http://' + PROJECT_IP + ':' + PROJECT_PORT + '/del_user'
        # 获取token
        from lib import login_token
        self.token = login_token.get_token('qzcsbj', '123456')
        print(self.token)
        self.headers = {'content-type': 'application/json'}

    def tearDown(self):
        print('测试用例执行完成...')

    def test_user_del_ok(self):
        """删除成功"""
        logger.logger.logger.debug('当前方法: %s' % p.get_current_function_name())
        payload = {"token":self.token,"username":"test133","adduser":"qzcsbj"}
        try:
            res = requests.post(url=self.url, json=payload,headers=self.headers).json()
            print(res,type(res))
        except Exception as e:
            res = {'code': '999', 'msg': '连接错误。'}

        # res = requests.post(url=self.url, json=payload,headers=self.headers).json()
        # print(res,type(res))


        logger.logger.logger.debug('是测试点【%s】下的用例【%s: %s】,返回的结果【%s】' % (
        self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__, p.get_current_function_name(), res))

        self.assertEqual(res['code'], 9600)

    def test_user_del_not_exist(self):
        """用户不存在"""
        payload = {"token":self.token,"username":"test1333","adduser":"qzcsbj"}
        try:
            res = requests.post(url=self.url, json=payload, headers=self.headers).json()
        except Exception as e:
            res = {'code': '999', 'msg': '连接错误。'}
        logger.logger.logger.debug('是测试点【%s】下的用例【%s: %s】,返回的结果【%s】' % (
        self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__, p.get_current_function_name(), res))

        self.assertEqual(res['code'], 9601)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(UserDel("test_user_del_ok"))
    suit.addTest(UserDel("test_user_del_not_exist"))
    fp = open("./report_debug.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'**项目接口自动化测试报告', description=u'**项目接口自动化测试报告')
    runner.run(suit)
    fp.close()

    # if __name__ == '__main__':
    #     unittest.main()
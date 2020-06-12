#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 22:59
# @Blog    : http://www.cnblogs.com/uncleyong
# @Gitee   : https://gitee.com/uncleyong
# @QQ交流群 : 652122175
# @公众号   : 全栈测试笔记


import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
import unittest
import requests
from lib import HTMLTestRunner
from lib import logger
from lib.tools import p
from conf.settings import PROJECT_IP
from conf.settings import PROJECT_PORT


class UserReg(unittest.TestCase):
    def setUp(self):
        print('测试用例开始执行...')

    def tearDown(self):
        print('测试用例执行完成...')

    def test_user_reg_ok(self):
        """注册成功"""
        pass

    def test_user_reg_exist(self):
        """注册用户名已经存在"""
        pass

    def test_user_reg_no_phone(self):
        """未填写手机号"""
        pass


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(UserReg("test_user_reg_ok"))
    suit.addTest(UserReg("test_user_reg_exist"))
    suit.addTest(UserReg("test_user_reg_no_phone"))
    fp = open("./report_debug.html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'**项目接口自动化测试报告',description=u'**项目接口自动化测试报告')
    runner.run(suit)
    fp.close()

# if __name__ == '__main__':
#     unittest.main()
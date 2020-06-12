#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 22:59
# @Blog    : http://www.cnblogs.com/uncleyong
# @Gitee   : https://gitee.com/uncleyong
# @QQ交流群 : 652122175
# @公众号   : 全栈测试笔记

import os
import sys

# 获取项目的根目录
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(path)

# 把path加入环境变量，0表示放在最前面，因为python解释器会按照列表顺序去依次到每个目录下去匹配你要导入的模块名，
# 只要在一个目录下匹配到了该模块名，就立刻导入，不再继续往后找
sys.path.insert(0, path)
# 导入配置文件中定义的测试用例的路径
from conf.settings import TESTCASE_PATH
# 导入配置文件中定义的测试报告的路径
from conf.settings import REPORT_PATH
import unittest
# 导入报告模板
from lib.HTMLTestRunner import HTMLTestRunner as hr1
from lib.HTMLTestReportCN import HTMLTestRunner as hr2

import time
# 自动根据测试用例的路径匹配查找测试用例文件（*.py）,并将查找到的测试用例组装到测试套件中
suit = unittest.defaultTestLoader.discover(TESTCASE_PATH, pattern='test_*.py')
print(suit)

if __name__ == '__main__':
	# 获取当前时间并指定时间格式
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    # 创建报告文件
    # fp = open(REPORT_PATH + now + "_report.html", 'wb')
    # 调试阶段，不生成太多报告文件，先去掉时间戳
    fp = open(REPORT_PATH + "_report_all.html", 'wb')
    # 使用HTMLTestRunner
    # runner = hr1(
    #     stream=fp,
    #     title=u'vip测试提升圈项目实战接口自动化测试报告',
    #     description=u'测试报告也可访问测试服务器查看，地址：http://<测试服务器IP>:8081/')

    # 使用HTMLTestReportCN
    runner = hr2(
        stream=fp,
        title=u'vip测试提升圈项目实战接口自动化测试报告',
        description=u'测试报告也可访问测试服务器查看，地址：http://<测试服务器IP>:8081/',
        tester="全栈测试笔记")

    runner.run(suit)
    fp.close()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 22:59
# @Blog    : http://www.cnblogs.com/uncleyong
# @Gitee   : https://gitee.com/uncleyong
# @QQ交流群 : 652122175
# @公众号   : 全栈测试笔记

import os


# 获取项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 定义测试用例的目录路径
TESTCASE_PATH =  os.path.join(BASE_PATH,'test_case')
# 定义测报告的目录路径
REPORT_PATH =  os.path.join(BASE_PATH,'report/')
# 定义日志文件的路径
LOG_PATH = os.path.join(BASE_PATH,'log/log.txt')
# 定义测试数据的目录路径
DATA_PATH = os.path.join(BASE_PATH,'data')


# project
PROJECT_IP = '127.0.0.1'
PROJECT_PORT = '9999'


# print(BASE_PATH)
# print(TESTCASE_PATH)
# print(REPORT_PATH)
# print(LOG_PATH)



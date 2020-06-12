#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from selenium import webdriver
import time
open = webdriver.Chrome()
#隐式等待
open.implicitly_wait(3)
open.get('https://www.baidu.com/')
#   浏览器全屏方法
open.maximize_window()
open.find_element_by_class_name('s_ipt').send_keys('北京')
# time.sleep(3)
open.find_element_by_class_name('s_btn').click()
# time.sleep(1)
open.find_element_by_link_text('北京_百度百科').click()
open.switch_to.window(open.window_handles[1])
open.find_element_by_css_selector("body > div.body-wrapper > div.before-content > div.polysemant-list.polysemant-list-normal > ul > li:nth-child(5) > a").click()
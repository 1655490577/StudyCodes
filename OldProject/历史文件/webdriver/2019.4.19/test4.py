#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://test-admin.skjiadao.com/skjd-admin/')
value = driver.find_element_by_xpath("//*[@id='loginname']")
value.send_keys('admin')
print(value.get_attribute('value'))

time.sleep(3)
driver.close()
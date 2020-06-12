#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('http://www.python3.vip/doc/tutorial/selenium/code/sample3.html')
mainWindow = driver.current_window_handle
driver.find_element_by_xpath('/html/body/a').click()
print(driver.window_handles)
for i in driver.window_handles:
    driver.switch_to.window(i)
    if '必应' in driver.title:
        break
    else:
        pass
driver.close()
driver.switch_to.window(mainWindow)
driver.close()
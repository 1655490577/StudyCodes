#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from Aoneone import TestOne
import time
# desired_caps = {'platformName': 'Android',
#                 'deviceName': 'emulator-5554',
#                 'platformVersion': '5.1.1',
#                 'appPackage': 'com.hbskjd.driver',
#                 'appActivity': 'com.hbskjd.driver.ui.login.LoginActivity',
#                 'unicodeKeyboard': True,
#                 'resetKeyboard': True}
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

TestOne = TestOne('Android', 'emulator-5554', '5.1.1', 'com.hbskjd.driver',
                    'com.hbskjd.driver.ui.login.LoginActivity', True, True)
driver = TestOne.return_driver()

driver.implicitly_wait(8)
# driver.find_element_by_id('android:id/button2').click()
driver.find_element_by_id("com.hbskjd.driver:id/login_phone").send_keys('13168775547')
driver.find_element_by_id('com.hbskjd.driver:id/login_psw').send_keys('123456')
driver.find_element_by_id('com.hbskjd.driver:id/login_finish').click()
print(driver.get_window_size())
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
print(x, y)
time.sleep(2)
driver.swipe(9/100*x, 94/100*y, 92/100*x, 94/100*y, 500)
time.sleep(2)
# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.'
#                              'FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.'
#                              'LinearLayout[3]/android.widget.RelativeLayout').click()
TestOne.target_click(542,1525,driver)
time.sleep(2)
driver.find_element_by_id('com.hbskjd.driver:id/online_status').click()
time.sleep(2)
driver.find_element_by_id('com.hbskjd.driver:id/saomaxiadan').click()
time.sleep(2)
driver.find_element_by_id('com.hbskjd.driver:id/toolbar_leftImgBtn').click()
time.sleep(2)
driver.find_element_by_id('com.hbskjd.driver:id/toolbar_leftImgBtn').click()



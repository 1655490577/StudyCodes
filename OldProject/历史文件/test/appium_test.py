from appium import webdriver
from time import sleep

desired_caps = {'platformName': 'Android', 'platformVersion': '4.4.2', 'deviceName': '127.0.0.1:62001 device',
                'appPackage': 'com.skjd.bus', 'appActivity': 'ui.activity.WelcomeActivity'}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_id("android:id/button1").click()
driver.find_element_by_id('com.skjd.bus:id/login_phone').send_keys('13168775547')
driver.find_element_by_id('com.skjd.bus:id/login_psw').send_keys('a123456789')
driver.find_element_by_id('com.skjd.bus:id/login_finish').click()
driver.reset()

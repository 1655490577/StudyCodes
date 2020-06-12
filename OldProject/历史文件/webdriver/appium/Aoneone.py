#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from appium import webdriver


class TestOne(object):

    def __init__(self, platformname, devicename, platformversion, apppackage,
                 appactivity, unicodekeyboard, resetkeyboard):
        self.platformName = platformname
        self.deviceName = devicename
        self.platformVersion = platformversion
        self.appPackage = apppackage
        self.appActivity = appactivity
        self.unicodeKeyboard = unicodekeyboard
        self.resetKeyboard = resetkeyboard
        self.desired_caps = {
                    'platformName': self.platformName,
                    'deviceName': self.deviceName,
                    'platformVersion': self.platformVersion,
                    'appPackage': self.appPackage,
                    'appActivity': self.appActivity,
                    'resetKeyboard': self.resetKeyboard,
                    'unicodeKeyboard': self.unicodeKeyboard
        }

    def return_driver(self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
        return driver

    @staticmethod
    def target_click(x1, y1, driver):      # x1,y1为你编写脚本时适用设备的实际坐标
        wd = driver
        x_1 = x1/1080     # 计算坐标在横坐标上的比例，其中375为iphone6s的宽
        y_1 = y1/1980     # 计算坐标在纵坐标667为iphone6s的高
        x = wd.get_window_size()['width']       # 获取设备的屏幕宽度
        y = wd.get_window_size()['height']      # 获取设备屏幕的高度
        print(x_1*x, y_1*y)      # 打印出点击的坐标点
        wd.tap([(x_1*x, y_1*y)], 500)       # 模拟单手点击操作


if __name__ == '__main__':
    test_one = TestOne('Android', 'emulator-5554', '5.1.1', 'com.hbskjd.driver',
                        'com.hbskjd.driver.ui.login.LoginActivity', True, True)
    adriver = test_one.return_driver()
    print(type(adriver))
    adriver.implicitly_wait(8)
    # driver.find_element_by_id('android:id/button2').click()
    adriver.find_element_by_id("com.hbskjd.driver:id/login_phone").send_keys('13168775547')
    adriver.find_element_by_id('com.hbskjd.driver:id/login_psw').send_keys('123456')
    adriver.find_element_by_id('com.hbskjd.driver:id/login_finish').click()

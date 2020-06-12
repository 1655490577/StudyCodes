#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://localhost:63342/Python_codes/webdriver/2019.4.19/testhtml.html?_ijt=sg8lo3o9d5beuoe23emfakb0j')
eleObjList = driver.find_elements_by_xpath("//div//p")

for eleObj in eleObjList:
    print(eleObj.text)

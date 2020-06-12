from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('http://www.python3.vip/doc/tutorial/selenium/code/sample2.html')
driver.switch_to.frame('frame1')
lists = driver.find_elements_by_class_name('animal')
for i in lists:
    print(i.text)
driver.switch_to.default_content()
driver.close()
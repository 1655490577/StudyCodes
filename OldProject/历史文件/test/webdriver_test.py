from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# assert "Python" in driver.title
list1 = ['王涛', '涂许平', '汪文']
for i in list1:
    elem = driver.find_element_by_id("kw")
    elem.clear()
    elem.send_keys(i)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
# assert "No results found." not in driver.page_source
# driver.close()
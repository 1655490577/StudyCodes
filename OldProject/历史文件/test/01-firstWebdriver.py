from selenium import webdriver
from multiprocessing import Pool
import time
import unittest


class TestWeb(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_run(self):
        driver = self.driver
        driver.get("http://39.104.54.182:8012/skjd-admin/main/index")
        driver.maximize_window()
        time.sleep(2)
        elem1 = driver.find_element_by_id("loginname")
        elem2 = driver.find_element_by_id("password")
        elem3 = driver.find_element_by_id("to-recover")
        elem1.clear()
        elem1.send_keys("admin")
        time.sleep(2)
        elem2.clear()
        elem2.send_keys("admin")
        time.sleep(5)
        elem3.click()


if __name__ == '__main__':
#     unittest.main()
    pool = Pool(2)
    for i in range(2):
        pool.apply_async(unittest.main)
    pool.close()
    pool.join()
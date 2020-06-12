from selenium import webdriver
import time


# 1.登录
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://39.104.54.182:8080/skjd-admin/main/index")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='loginname']").send_keys('admin')
driver.find_element_by_xpath("//*[@id='password']").send_keys('admin')
time.sleep(5)       # 留出输入验证码的时间
driver.find_element_by_xpath("//*[@id='to-recover']").click()

# 2.进入首页,定位进入优惠劵界面
time.sleep(3)
driver.find_element_by_xpath("//*[@id='lm132']/a[@class='dropdown-toggle']").click()
driver.find_element_by_xpath("//*[@id='z133']").click()

a = ['满13减12.99', '满50减49.99', '满50减49.99', '满50减49.99',
     '满168减167.99', '满168减167.99', '满60减59.99', '满300减299.99']
b = 'ABCDEFGH'
c = ['1300', '5000', '5000', '5000', '16800', '16800', '6000', '30000']
d = ['1299', '4999', '4999', '4999', '16799', '16799', '5999', '29999']
# 添加优惠劵
for i in range(1, 9):
    driver.switch_to.frame('mainFrame')
    driver.switch_to.frame('page_z133')
    driver.find_element_by_xpath("//*[@id='Form']/div/table/tbody/tr/td[1]/a").click()
    time.sleep(0.1)
    driver.switch_to.default_content()
    driver.switch_to.frame('_DialogFrame_0')
    time.sleep(0.1)
    driver.find_element_by_id('name').send_keys(a[i-1])
    driver.find_element_by_id('code').send_keys(b[i-1])
    driver.find_element_by_id('lineID').click()
    driver.find_element_by_xpath("//*[@id='lineID']/option[8]").click()
    time.sleep(0.1)
    driver.find_element_by_id('type').click()
    time.sleep(0.1)
    driver.find_element_by_xpath(f"//*[@id='type']/option[{i+1}]").click()
    time.sleep(0.1)
    driver.find_element_by_id('count').send_keys('5')
    driver.find_element_by_id('tomoney').send_keys(c[i-1])
    driver.find_element_by_id('money').send_keys(d[i-1])
    driver.find_element_by_id('starttime').click()
    time.sleep(0.1)
    driver.find_element_by_xpath("//*[@id='layui-laydate1']/div[2]/div/span[2]").click()
    time.sleep(0.1)
    driver.find_element_by_id('explain').send_keys(a[i-1])
    driver.find_element_by_xpath("/html/body/div/div/input[1]").click()
    time.sleep(0.1)
time.sleep(1)
# 生成优惠劵
for i in range(2):
    for j in range(1, 9):
        driver.switch_to.frame('mainFrame')
        driver.switch_to.frame('page_z133')
        time.sleep(0.1)
        driver.find_element_by_xpath(f"//*[@id='table_report']/tbody/tr[{j}]/td[9]/a[1]").click()
        time.sleep(0.1)
        driver.switch_to.default_content()
        driver.switch_to.frame('_DialogFrame_0')
        time.sleep(0.1)
        driver.find_element_by_id('sum').send_keys('20')
        driver.find_element_by_xpath("/html/body/div/div[2]/input[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/a[2]").click()
        time.sleep(1)

time.sleep(5)
driver.close()

'''
通过switch_to.frame()方法切换表单
'''
from time import sleep

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.126.com")
sleep(2)
login_frame=driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
driver.switch_to.frame(login_frame)
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()

#重新回到主页面上操作元素，这时候，就可以用switch_to_default_content()方法返回到主页面
driver.switch_to.default_content()

driver.quit()
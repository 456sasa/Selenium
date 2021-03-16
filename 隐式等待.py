"""
WebDriver提供的implicitly_wait()方法可用来实现隐式等待
参数是时间，单位为秒
它会等待页面上的所有元素
如果元素存在则继续执行，如果定位不到元素，则它将已轮询的方式不断地判断元素是否存在
直到超出社而至的时间还没定位到元素，则抛出异常
"""
from time import ctime

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver=webdriver.Chrome()
#设置隐式等待时间为10s
driver.implicitly_wait(10)


driver.get("http://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("ssss").send_keys("ssss")
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()
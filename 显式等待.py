
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

element=WebDriverWait(driver, 5,0.5).until(
    EC.visibility_of_element_located((By.ID,"kw"))
)

element.send_keys("selenium")


driver.quit()

"""
在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间仍检测不到，则抛出异常
WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
   driver:浏览器驱动
   timeout:最长超时时间，默认以秒为单位
   oll_frequency:检测的间隔（步长）时间，默认为0.5s
   ignored_exceptions:超时后的异常信息，默认情况下抛出NoSuchElementException异常

WebDriverWait()一般与until()或until_not()方法配合使用
   until(method,message="")   调用该方法提供的驱动程序作为一个参数，直到返回值为True
   until_not(method,message="")   调用该方法提供的驱动程序作为一个参数，直到返回值为flase
"""
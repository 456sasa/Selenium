from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")

# driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element(By.ID,"kw").send_keys("test")

driver.find_element_by_id("su").click()



time.sleep(3)

driver.quit()
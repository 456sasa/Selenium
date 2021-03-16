from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

input=driver.find_element_by_id("kw")

#在输入框输入内容
input.send_keys("seleniummmmmmmm")

time.sleep(3)

#删除最后一位
input.send_keys(Keys.BACKSPACE)

#输入空格键
input.send_keys(Keys.SPACE)

input.send_keys("测试")


#Ctral+a全选
input.send_keys(Keys.CONTROL,"a")

#Ctral+x剪切
input.send_keys(Keys.CONTROL,"x")
time.sleep(3)
#Ctral+v粘贴
input.send_keys(Keys.CONTROL,"v")

#回车代替单击操作
input.send_keys(Keys.ENTER)

driver.quit()
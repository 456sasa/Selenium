'''
switch_to.alert()方法定位
text  返回alert、confirm、prompt中的文字信息
accept() 接受现有的警告框
dismiss() 解散现有警告框
send_keys() 在警告框中输入文本(如果可以输入的话)
'''
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
#设置浏览器大小全屏
driver.maximize_window()

#打开搜索设置
driver.find_element_by_id("s-usersetting-top").click()
driver.find_element_by_link_text("搜索设置").click()

#保存设置
driver.find_element_by_class_name("prefpanelgo").click()

#获取警告框
alert=driver.switch_to.alert

#获取警告框信息
text=alert.text
print(text)

#接取警告框 效果确定接受关闭警告框
alert.accept()

time.sleep(3)
driver.quit()
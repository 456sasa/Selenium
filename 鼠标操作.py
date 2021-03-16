"""
在WebDriver中，与鼠标操作相关的方法都封装在ActionChains类中
ActionChains类提供了鼠标操作的常用方法：
  perform():执行ActionChains类中存储的所有行为
  context_click():右击
  double_click():双击
  drag_and_drop():拖动
  move_to_element():鼠标悬停
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

#定位要悬停的元素
above=driver.find_element_by_link_text("新闻")
#鼠标悬停
ActionChains(driver).move_to_element(above).perform()

ActionChains(driver).double_click(above).perform()


time.sleep(3)
driver.quit()
"""
ActionChains(driver)   
调用ActionChains类，把浏览器驱动driver作为参数传入

move_to_element(above)
move_to_element()方法用于模拟鼠标移动到元素上，在调用时需要指定元素

perform（）
提交所有ActionChains类中存储的行为
"""
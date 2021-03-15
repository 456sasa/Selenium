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

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

#定位要悬停的元素
above=driver.fin

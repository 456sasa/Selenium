from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")

"""
控制浏览器大小
"""

def changesize():
    # 参数数字为像素
    driver.set_window_size(480, 800)
    time.sleep(3)
    driver.quit()


"""
控制浏览器前进后退
"""

def forward():
    #访问百度首页
    first_url="https://www.baidu.com/"
    print("now access %s" %(first_url))
    driver.get(first_url)

    #访问新闻页
    second_url="https://news.baidu.com"
    print("now access %s" %(second_url))
    driver.get(second_url)
    time.sleep(3)

    #返回到百度首页
    print("back to %s" %(first_url))
    driver.back()
    time.sleep(3)

    #前进到新闻夜
    print("forward to %s" %(second_url))
    driver.forward()
    time.sleep(3)

    driver.quit()

"""
模拟浏览器刷新
"""
def refresh():
    driver.get("https://news.baidu.com")
    driver.refresh()
    print("refresh")
    time.sleep(3)
    driver.quit()


"""
Webdriver中的常用方法
"""
def Webdriver_commom_methond():
    driver.get("http://www.baidu.com")
    #clear()清除文本
    driver.find_element_by_id("kw").clear()
    #send_keys(value)模拟按键输入
    driver.find_element_by_id("kw").send_keys("Selenium")

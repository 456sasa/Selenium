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
def Webdriver_commom_methond1():
    driver.get("http://www.baidu.com")
    time.sleep(3)
    #clear()清除文本
    driver.find_element_by_id("kw").clear()
    #send_keys(value)模拟按键输入
    driver.find_element_by_id("kw").send_keys("Selenium")
    time.sleep(3)
    #click():单击元素
    driver.find_element_by_id("su").click()

    driver.find_element_by_id("kw").clear()

    #submit():提交表单
    search_text=driver.find_element_by_id("kw")
    search_text.send_keys("test_submit")
    search_text.submit()

    time.sleep(3)

    driver.quit()

def Webdriver_commom_methond2():
    driver.get("http://www.baidu.com")
    #获取输入框尺寸
    size=driver.find_element_by_id("kw").size
    print(size)

    #返回百度热榜信息
    hot_chart=driver.find_elements_by_class_name("title-content-title")
    # for hot in hot_chart:
    #     print(hot.text)
    for i in range(len(hot_chart)):
        print(str(i+1)+"."+hot_chart[i].text)

    #返回元素的属性值，可以使id、name、type或其他任意属性
    attribute=driver.find_element_by_id("kw").get_attribute("type")
    print(attribute)

    #返回元素的结果是否可见，返回结果未True或False
    result=driver.find_element_by_id("kw").is_displayed()
    print(result)

    driver.quit()

Webdriver_commom_methond2()
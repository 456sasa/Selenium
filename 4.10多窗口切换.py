from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

#获取百度搜索窗口句柄
search_windows=driver.current_window_handle

driver.find_element_by_link_text("登录").click()
driver.find_element_by_link_text("立即注册").click()

#获得当前所有打开的窗口句柄
all_handles=driver.window_handles

#进入注册窗口

for handle in all_handles:
    if handle!=search_windows:
        driver.switch_to.window(handle)
        print(driver.title)
        driver.find_element_by_name("userName").send_keys("username")
        driver.find_element_by_name("phone").send_keys("13xxxxxxxxx")
        driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("password")

        time.sleep(2)
        #关闭当前窗口
        driver.close()

#回到搜索窗口
driver.switch_to.window(search_windows)
print(driver.title)

driver.quit()
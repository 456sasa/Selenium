from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.implicitly_wait(3)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("kw").send_keys(Keys.ENTER)

#定位一组元素
texts=driver.find_elements_by_xpath("//div[@tpl='se_com_default']/h3/a")

print(len(texts))

for t in range(len(texts)):
    print(str(t+1)+"."+texts[t].text)

driver.quit()
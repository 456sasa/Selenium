'''
Select类   用于定位<select>标签
select_by_value()  通过value值定位下拉选项
select_by_visible_text()  通过text值定位下拉选项
select_by_index()  根据下拉选项的索引进行选择。第一个选项为0

deselect_by_index(index)  取消选择，用于多选
deselect_by_value(value)  取消选择，用于多选
deselect_by_visible_text(text)  取消选择，用于多选
deselect_all()  全部取消，用于多选
options 所有选项
first_selected_option  第一个选择的选项（多选情况下）或者当前选择的选项（单选）
all_selected_options  所有已经选择的选项
'''

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://sahitest.com/demo/selectTest.htm")
#设置浏览器大小全屏
driver.maximize_window()

ele=driver.find_element_by_id("s3Id")

#实例化Select
selected_element=Select(ele)
selected_element.select_by_index(1)

print(selected_element.first_selected_option.text)
time.sleep(1)

selected_element.select_by_value("o2val")
print(selected_element.first_selected_option.text)

selected_element.select_by_visible_text("o3")
print(selected_element.first_selected_option.text)


ele2=driver.find_element_by_id("s4Id")
selected_element2=Select(ele2)
selected_element2.select_by_index(1)
selected_element2.select_by_index(2)
selected_element2.select_by_index(3)

print("######")
for select in selected_element2.all_selected_options:
    print(select.text)

print("######")
selected_element2.deselect_by_index(1)
for select in selected_element2.all_selected_options:
    print(select.text)

print("######")
selected_element2.deselect_by_value("o2val")
for select in selected_element2.all_selected_options:
    print(select.text)

print("######")
selected_element2.deselect_by_visible_text("o3")
for select in selected_element2.all_selected_options:
    print(select.text)
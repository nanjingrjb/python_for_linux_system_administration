'''*************************************************************************
File Name: op_sel_chosefromlist.py
Author: nanjingrjb
Mail: nanjingrjbgmail.com/g 
Created Time: Thu Jul 20 07:59:36 2023
 *******************************************************************
'''


from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://tieba.baidu.com/index.html")

selectWebElement = driver.find_element(By.NAME, "rn");
Select(selectWebElement).select_by_visible_text("每页显示30条")
time.sleep(30)  #等待3s，以便看到选择效果

Select(selectWebElement).select_by_value("20")
time.sleep(30)

Select(selectWebElement).select_by_index(0)


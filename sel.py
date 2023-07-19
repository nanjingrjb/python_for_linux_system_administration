import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#建立浏览器信息
driver = webdriver.Edge()
#输入网址
driver.get("http://www.baidu.com")

#得到百度输入框
element = WebDriverWait(driver, 5, 0.5).until(
                      EC.presence_of_element_located((By.ID, "kw"))
                      )
element.send_keys('selenium')

#得到百度一下的按钮
element = WebDriverWait(driver, 5, 0.5).until(
                      EC.presence_of_element_located((By.ID, "su"))
                      )
element.send_keys(Keys.ENTER)

#延时等待100s
time.sleep(1000)
driver.quit()
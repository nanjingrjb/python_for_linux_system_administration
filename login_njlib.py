from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#模拟鼠标操作
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Edge()

driver.get('http://ntszzy.org:8070/ermsLogin/view.do')
time.sleep(2)
# 定位搜索输入框
#采用输入加属性的办法来实现，其中
text_label =driver.find_element(By.XPATH,'//input[@name="userName"]')
text_label.send_keys('13776603610')
#ac=ActionChains(driver)
#ac.click(text_label).perform()
text_label =driver.find_element(By.XPATH,'//input[@name="password"]')
text_label.send_keys('Scusky111111')
text_label =driver.find_element(By.XPATH,'//input[@name="cwcode"]')
text_label.send_keys('3')

#捕捉登录按钮
login_butt =driver.find_element(By.XPATH,'//input[@type="button"]')
ac=ActionChains(driver)
#点击登录按钮
ac.click(login_butt).perform()
time.sleep(10)


# 在搜索框中输入 Dream丶Killer



time.sleep(200)
# 清除搜索框中的内容
text_label.clear()

# 输出搜索框元素是否可见
print(text_label.is_displayed())
# 输出placeholder的值
print(text_label.get_attribute('placeholder'))

# 定位搜索按钮
button = driver.find_element_by_xpath('//*[@id="toolbar-search-button"]/span')
# 输出按钮的大小
print(button.size)
# 输出按钮上的文本
print(button.text)

'''输出内容
True
python面试100问
{'height': 32, 'width': 28}
搜索
'''
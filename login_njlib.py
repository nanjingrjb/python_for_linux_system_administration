from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#模拟鼠标操作
from selenium.webdriver.common.action_chains import ActionChains

def login_sj():
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
    val=input("input digit res")
    text_label.send_keys(str(val))

    #捕捉登录按钮
    login_butt =driver.find_element(By.XPATH,'//input[@type="button"]')
    ac=ActionChains(driver)
    #点击登录按钮
    ac.click(login_butt).perform()
    time.sleep(100)

#手机验证码登录
def login_yzm():
    driver = webdriver.Edge()

    driver.get('http://ntszzy.org:8070/ermsLogin/view.do')
    time.sleep(2)
    # 定位搜索输入框
    #采用输入加属性的办法来实现，其中
    text_label =driver.find_element(By.XPATH,'//a[@href="#tabs-2"]')
    #选择点击
    text_label.click()

     #采用输入加属性的办法来实现，其中
    text_label =driver.find_element(By.XPATH,'//input[@name="phone"]')
    text_label.send_keys('13776603610')

    #获取验证码
    #text_label =driver.find_element(By.XPATH,'//a[@href="javascript:void(0);"]')
    text_label=driver.find_element(By.CLASS_NAME,'send-btn-link')
    #选择点击
    text_label.click()
    time.sleep(2)
    val=input("input digit res")
    #根据路径来寻找，从父标签开始
    text_label =driver.find_element(By.XPATH,'//div/div/form/dl/dd/input')
    text_label.send_keys(str(val))
    time.sleep(2)
    #点击验证
    text_label = driver.find_element(By.XPATH, '//div/div/form/div/input[@value="验 证"]')
    text_label.click()


     #捕捉登录按钮
    login_butt =driver.find_element(By.XPATH,'//input[@type="button"]')
    ac=ActionChains(driver)
    #点击登录按钮
    ac.click(login_butt).perform()

    time.sleep(20)

if __name__=='__main__':
    #login_sj()
    login_yzm()






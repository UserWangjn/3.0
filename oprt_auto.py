#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YIMAO'
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#打开页面

url="http://10.128.1.42:8088/passport/login"
browser=webdriver.Firefox()
browser.get(url)

time.sleep(10)
button1=browser.find_elements_by_xpath("/html/body/app-root/app-login/div/div[2]/div/div[1]/div/input")
button2=browser.find_elements_by_xpath("/html/body/app-root/app-login/div/div[2]/div/div[2]/div/input")
# button1 = browser.find_elements_by_name('userName')
# button2 = browser.find_elements_by_name('password')
#print(len(button1))
button1[0].send_keys('alarmx')
# button1[0].send_keys('alarmx')
#time.sleep(10)
# button1.send_keys("Eastmount CSDN")
button2[0].send_keys('123456a&')
# button2[0].send_keys('123456a&')
loginBtn = browser.find_element_by_id('login')
loginBtn.click()

time.sleep(20)


# from selenium import webdriver
# import time
# browser = webdriver.Firefox()
# browser.get('https://www.taobao.com')
# input = browser.find_elements_by_id('q') # 找到搜索框的id为q
# input.send_keys('IPhone') # 作用是在搜索框中输入 此处代码有问题，暂时未解决
# time.sleep(1)
# input.clear() # 清楚搜索框中的内容
# input.send_keys('ipad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()
# browser.close()






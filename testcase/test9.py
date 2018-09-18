#-*-coding:utf-8-*- 
__author__ = 'Administrator'

import uiautomator2 as u2
from atx.ext.chromedriver import ChromeDriver
from public import cofig

d = u2.connect_usb(cofig.ID)  #手机的ip 为10.10.23.15
d.app_start('com.github.android_app_bootstrap',stop='True')
d(text='Login').click()
d(text='Baidu').click()
driver = ChromeDriver(d).driver(cofig.ip2)  #这里也一样填手机的ip,端口5555即可
print("执行通过")
driver.find_element_by_id('index-kw').click()
driver.find_element_by_id('index-kw').send_keys('Python')
driver.find_element_by_id('index-bn').click()
print(driver.title)
driver.quit()
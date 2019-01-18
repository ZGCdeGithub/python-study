from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time


driver = webdriver.PhantomJS(executable_path=r'D:\ProgramData\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('http://www.baidu.com')

# 通过函数查找title标签
print('Title: {0}'.format(driver.title))


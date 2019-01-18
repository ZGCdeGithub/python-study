from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


url = 'http://www.baidu.com'
driver = webdriver.Chrome(executable_path=r'D:\ProgramData\chromedriver\chromedriver.exe')

# 打开网址
driver.get(url)

# 打印出网页titlt

web_title = driver.find_element_by_id('wrapper')
print(web_title)
print(web_title.text)

# 在搜索框中输入python，并搜索
time.sleep(2)
driver.find_element_by_id('kw').send_keys('python')
# 点击搜索框
driver.find_element_by_id('su').click()

# 将搜索内容截屏，（sleep2秒是防止网页没有加载完）
time.sleep(3)
driver.save_screenshot('python.png')

# 打印出页面的cookie
print(driver.get_cookies())

# 全选当前页面
web_body = driver.find_elements_by_tag_name('body')
print(web_body)
web_body[0].send_keys(Keys.CONTROL, 'a')

# 剪切输入框的内容
input_id_kw = driver.find_element_by_id('kw')
input_id_kw.send_keys(Keys.CONTROL, 'a')
input_id_kw.send_keys(Keys.CONTROL, 'x')

input_id_kw.send_keys(u'航空母舰')
time.sleep(2)
driver.save_screenshot('search1.png')

# 清空输入框
time.sleep(1)
input_id_kw.clear()
time.sleep(1)

# 关闭浏览器
driver.quit()



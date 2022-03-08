from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get("https://instagram.com/accounts/login/")
username = "neelmehta08"
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
driver.find_element_by_name("username").send_keys(username)
# for i in range(50,-1,-1):
driver.find_element_by_name("password").send_keys('//')
# time.sleep(500) 
driver.find_element_by_name("password").send_keys(u'\ue007')
# driver.find_element_by_name("password").send_keys(Keys.CONTROL,'a',Keys.DELETE) 
    # time.sleep(500)
time.sleep(6)
# url="http://instagram.com/{}"
# driver.get(url.format(username))
# post = driver.find_elements_by_class_name('_9AhH0')
# post[0].click()
# curr_img = driver.find_elements_by_class_name('PdwC2')
# time.sleep(1)
# if len(curr_img)>0:
#     like = driver.find_elements_by_css_selector('[aria-label="Like"]')
#     print(like)
#     like[0].click()

mssg = driver.find_element_by_css_selector('[aria-label="Messenger"]')
mssg.click()
time.sleep(2)
not_now = driver.find_elements_by_class_name('HoLwm')
not_now[0].click()
time.sleep(2)
user = driver.find_elements_by_xpath("// div[contains(text(),\'manavshah.25')]")
user[0].click()
time.sleep(2)

mssg = driver.find_element_by_xpath("//textarea[@placeholder='Message...']")
for i in range(15):
    mssg.send_keys("hello")
    driver.find_element_by_xpath("// button[contains(text(),\'Send')]").click()
time.sleep(1)

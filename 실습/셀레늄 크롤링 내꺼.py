<<<<<<< HEAD
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chromedriver = 'C:/Users/701/kdigital/lecture/K_digital_lecture/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.jungle.co.kr/')
a = driver.find_elements_by_class_name('title')
title=[]
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    login_btn2 = driver.find_element_by_css_selector('#more')
    login_btn2.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    login_btn2.click()
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        for i in a:
            title.append(i.text)
        break
=======
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chromedriver = 'C:/Users/701/kdigital/lecture/K_digital_lecture/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.jungle.co.kr/')
a = driver.find_elements_by_class_name('title')
title=[]
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    login_btn2 = driver.find_element_by_css_selector('#more')
    login_btn2.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    login_btn2.click()
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        for i in a:
            title.append(i.text)
        break
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
print(title)
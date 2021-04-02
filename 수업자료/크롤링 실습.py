<<<<<<< HEAD
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver= webdriver.Chrome('C:/Users/701/kdigital/lecture/K_digital_lecture/chromedriver.exe') 
# driver.get('https://www.rocketpunch.com/jobs')
# driver.implicitly_wait(2)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# a = driver.find_elements_by_css_selector('div.company-name strong')
# name=[]
# login_btn2 = driver.find_element_by_css_selector('.more-jobs')
# login_btn2.click()
# for i in a:
#     name.append(i.text)
# b= driver.find_elements_by_css_selector('div.description')
# description=[]
# for i in b:
#     description.append(i.text)
# c= driver.find_elements_by_css_selector('a.nowrap.job-title.primary.link')
# human=[]
# for i in c:
#     if i.text :
#         human.append(i.text)    
#     else:
#         pass
# print(name)
# print(description)
# print(human)

import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.rocketpunch.com/jobs'

#def print_url():
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
li_list = soup.select('.company item')
for li in li_list:
    brand = li.select_one('div.company-name strong').text
    name = li.select_one('div.description')
    price = li.select_one('a.nowrap.job-title.primary.link')
    print('브랜드:', brand,'\n''제품명:',name,'\n''가격:',price,'\n')
#print_url()
# for page in range(1,11):
#     URL = URL+'?device=&d_cat_cd=001&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page='+str(page)+'&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&size=&tags=&sale_campaign_yn=&timesale_yn=&q='
=======
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver= webdriver.Chrome('C:/Users/701/kdigital/lecture/K_digital_lecture/chromedriver.exe') 
# driver.get('https://www.rocketpunch.com/jobs')
# driver.implicitly_wait(2)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# a = driver.find_elements_by_css_selector('div.company-name strong')
# name=[]
# login_btn2 = driver.find_element_by_css_selector('.more-jobs')
# login_btn2.click()
# for i in a:
#     name.append(i.text)
# b= driver.find_elements_by_css_selector('div.description')
# description=[]
# for i in b:
#     description.append(i.text)
# c= driver.find_elements_by_css_selector('a.nowrap.job-title.primary.link')
# human=[]
# for i in c:
#     if i.text :
#         human.append(i.text)    
#     else:
#         pass
# print(name)
# print(description)
# print(human)

import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.rocketpunch.com/jobs'

#def print_url():
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
li_list = soup.select('.company item')
for li in li_list:
    brand = li.select_one('div.company-name strong').text
    name = li.select_one('div.description')
    price = li.select_one('a.nowrap.job-title.primary.link')
    print('브랜드:', brand,'\n''제품명:',name,'\n''가격:',price,'\n')
#print_url()
# for page in range(1,11):
#     URL = URL+'?device=&d_cat_cd=001&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page='+str(page)+'&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&size=&tags=&sale_campaign_yn=&timesale_yn=&q='
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
#     print_url()
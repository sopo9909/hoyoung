from urllib.request import urlretrieve
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time 

search = input('어떤 사진을 원하니?')
url =f"https://www.google.com/search?q={quote_plus(search)}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiR2K-hvvruAhUL7WEKHeU1D68Q_AUoAXoECAYQAw&biw=1054&bih=898"

chromedriver = 'C:/Users/701/kdigital/lecture/K_digital_lecture/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html)
for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
img = soup.select('.rg_i.Q4LuWd')
n =1 
imguri =[]
for i in img:
    try:
        imguri.append(i.attrs["src"])
    except KeyError:
        imguri.append(i.attrs["data-src"])
for i in imguri:
    urlretrieve(i,"C:/Users/701/kdigital/lecture/K_digital_lecture/내가만든재미난것/크롤링/"+search+str(n)+".jpg")
    n +=1
driver.close()
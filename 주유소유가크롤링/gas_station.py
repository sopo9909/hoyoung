import requests
from requests.models import Response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromedriver = 'C:/Users/701/Downloads/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(chromedriver)
URL = 'https://www.opinet.co.kr/searRgSelect.do'
driver.get(URL)
def setSeoul():
    Seoul = driver.find_element_by_xpath('//*[@id="SIDO_NM0"]/option[2]')
    Seoul.click()
def setGu(Guname):
    Gu = driver.find_element_by_xpath("//option[@value='"+str(Guname)+"']")
    Gu.click()
gugu=['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구','도봉구','동대문구','동작구','마포구','서대문구','서초구','성동구','성북구','송파구','양천구','영등포구','용산구','은평구','종로구','중구','중랑구']
headers = {"Content-Type":"application/x-www-form-urlencoded"}
data = {"name": "홍길동"}
requests.post("URL",data=data,headers=headers)
setSeoul()
for i in gugu: #구선택
    setGu(i)
    search_btn = driver.find_element_by_css_selector('#searRgSelect')
    search_btn.click()
    oilprice = driver.find_element_by_css_selector('#body1 > tr:nth-child(1) > td:nth-child(2)')
    nameofgasstation = driver.find_element_by_css_selector('#body1 > tr:nth-child(1) > td.rlist > a')


#클라이언트에 저장
session = requests.session()
response = session.get("URL")

#csv 저장
#.to_csv(C:/Users/701/Desktop/gas_station.csv)
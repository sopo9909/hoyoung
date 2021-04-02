<<<<<<< HEAD
import re

import requests
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
print(datetime.today().day)
yesterday = datetime.today() - timedelta(1)
urls ='https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=003&date='+str(yesterday.strftime("%Y%m%d"))
print(urls)
response = requests.get(urls,headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select(".type06_headline a")
for v in range(1,len(result),2):
    print(result[v].text.strip())
result2 = soup.select(".lede")
for v in range(len(result2)):
=======
import re

import requests
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
print(datetime.today().day)
yesterday = datetime.today() - timedelta(1)
urls ='https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=003&date='+str(yesterday.strftime("%Y%m%d"))
print(urls)
response = requests.get(urls,headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select(".type06_headline a")
for v in range(1,len(result),2):
    print(result[v].text.strip())
result2 = soup.select(".lede")
for v in range(len(result2)):
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
    print(result2[v].text)
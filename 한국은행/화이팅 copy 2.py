from time import *
from datetime import *
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import pandas as pd
import datetime
import requests
news_url ='https://www.yna.co.kr/view/AKR20201231123300530?input=1195m'
new_link = requests.get(news_url,headers={'User-Agent':'Mozilla/5.0'})
news_html = BeautifulSoup(new_link.text,'html.parser')
title = news_html.find('h1',{'class':'tit'}).get_text()
datetime = news_html.find('p',{'class':'update-time'})
print(datetime.get_text().strip('송고시간'))
article= news_html.find('div',{'class':'story-news article'}).get_text().strip()
#print(title,article)

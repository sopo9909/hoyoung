import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as bsp
import matplotlib
import matplotlib.pyplot as plt
import sqlite3
import re
import sqlite3
url='http://biz.khan.co.kr/khan_art_view.html?artid=202103162149005&code=920501'
res=requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
src=res.content.strip()
html =bsp(src,'html.parser')
title=html.find(attrs={'class':'headline'}).text
author=html.find(attrs={'class':'name'}).text
author=re.sub('[^가-힣]','',author)
time=html.find(attrs={'class':'byline'}).text.replace('\n','')
time=re.sub('수정.*','',time).replace('입력 :','').replace('\xa0','').strip()
content=html.find(attrs={'class':'art_body'}).text
author=re.sub('[^가-힣]','',author)
content=content.replace('\n',"").replace('\t',"").replace('\r',"")
content=re.sub('createIframe.*;','',content)
print(' 제목 : '+title+' 기자 : '+author+' 게시시간 : '+time+' 본문 : '+content)
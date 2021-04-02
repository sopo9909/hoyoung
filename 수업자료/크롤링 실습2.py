<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
#--------------------------문제 1번~
URL1 = 'https://finance.naver.com/sise/sise_quant.nhn'
response = requests.get(URL1)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select(".tltle")
index=[]
name=[]
for i, v in enumerate(result):
    index.append(i+1)
    name.append(v.text)
result3 = soup.select(".number")
preprice=[]
for v in range(0,len(result3),10):
    preprice.append(result3[v].text)
histprice=[]
for v in range(1,len(result3),10):
    rm = result3[v].text.strip()
    histprice.append(rm)
j=0
pm=[]
re = 0
result4 = soup.select(".number span")
for v in range(1,len(result4),2):
    am = result4[v].text.strip().strip('%')
    pm.append(float(am))
print(pm)
for a in range(len(name)):
    if pm[a] <= 0:
        print(index[a],name[a],preprice[a],histprice[a])
#--------------------------문제 2번~
for i in range(1,11):
    URL1 = 'https://search.musinsa.com/category/001?device=&d_cat_cd=001&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page='+str(i)+'&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&size=&tags=&sale_campaign_yn=&timesale_yn=&q='
    response = requests.get(URL1)
    soup = BeautifulSoup(response.text, "html.parser")
    result5 = soup.select(".boxed-list-wrapper .item_title a")
    brand=[]
    for v in range(len(result5)):
        tm = result5[v].text
        brand.append(tm)

    result6 = soup.select(".boxed-list-wrapper .list_info a")
    item=[]
    for v in result6:
        item.append(v.get('title'))
    price=[]
    priceset=[]
    result7 = soup.select(".boxed-list-wrapper .price")
    for r in range(len(result7)):
        am=result7[r].text
        priceset.append(am)
    for i in range(len(priceset)):
        astl =priceset[i].split()
        if len(astl) == 2:
            price.append(astl[1])
        else:
            price.append(astl[0])

    for ro in range(len(brand)):
        print('브랜드 : ',brand[ro],'이름 : ',item[ro],'가격 : ',price[ro])
#-------------네이버 뉴스시스 어제날짜------------------------
import requests
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
yesterday = datetime.today() - timedelta(1)
url='https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=003'
response = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select(".type06_headline a")
a=[]
for link in result:
    a.append(link.get('href'))
x=str(a[0])
a=int(x[-8:])
for i in range(10261000,a):
    urls ='https://news.naver.com/main/read.nhn?mode=LPOD&mid=sec&oid=003&aid=00'+str(i)
    response = requests.get(urls,headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.select(".t11")
    a=""
    for v in range(len(result)):
        a=result[v].text
        a=a[:10].replace(".","")
    if a==yesterday.strftime("%Y%m%d"):
        result2 = soup.select("#articleTitle")
        for v in range(len(result2)):
            x=result2[v].text
        print(x)
        result3 = soup.select("#articleBodyContents")
        for v in range(len(result3)):
            y = result3[v].text.strip()
=======
import requests
from bs4 import BeautifulSoup
#--------------------------문제 1번~
URL1 = 'https://finance.naver.com/sise/sise_quant.nhn'
response = requests.get(URL1)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select(".tltle")
index=[]
name=[]
for i, v in enumerate(result):
    index.append(i+1)
    name.append(v.text)
result3 = soup.select(".number")
preprice=[]
for v in range(0,len(result3),10):
    preprice.append(result3[v].text)
histprice=[]
for v in range(1,len(result3),10):
    rm = result3[v].text.strip()
    histprice.append(rm)
j=0
pm=[]
re = 0
result4 = soup.select(".number span")
for v in range(1,len(result4),2):
    am = result4[v].text.strip().strip('%')
    pm.append(float(am))
print(pm)
for a in range(len(name)):
    if pm[a] <= 0:
        print(index[a],name[a],preprice[a],histprice[a])
#--------------------------문제 2번~
for i in range(1,11):
    URL1 = 'https://search.musinsa.com/category/001?device=&d_cat_cd=001&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page='+str(i)+'&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&size=&tags=&sale_campaign_yn=&timesale_yn=&q='
    response = requests.get(URL1)
    soup = BeautifulSoup(response.text, "html.parser")
    result5 = soup.select(".boxed-list-wrapper .item_title a")
    brand=[]
    for v in range(len(result5)):
        tm = result5[v].text
        brand.append(tm)

    result6 = soup.select(".boxed-list-wrapper .list_info a")
    item=[]
    for v in result6:
        item.append(v.get('title'))
    price=[]
    priceset=[]
    result7 = soup.select(".boxed-list-wrapper .price")
    for r in range(len(result7)):
        am=result7[r].text
        priceset.append(am)
    for i in range(len(priceset)):
        astl =priceset[i].split()
        if len(astl) == 2:
            price.append(astl[1])
        else:
            price.append(astl[0])

    for ro in range(len(brand)):
        print('브랜드 : ',brand[ro],'이름 : ',item[ro],'가격 : ',price[ro])
#-------------네이버 뉴스시스 어제날짜------------------------
import requests
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
yesterday = datetime.today() - timedelta(1)
url='https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=003'
response = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select(".type06_headline a")
a=[]
for link in result:
    a.append(link.get('href'))
x=str(a[0])
a=int(x[-8:])
for i in range(10261000,a):
    urls ='https://news.naver.com/main/read.nhn?mode=LPOD&mid=sec&oid=003&aid=00'+str(i)
    response = requests.get(urls,headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.select(".t11")
    a=""
    for v in range(len(result)):
        a=result[v].text
        a=a[:10].replace(".","")
    if a==yesterday.strftime("%Y%m%d"):
        result2 = soup.select("#articleTitle")
        for v in range(len(result2)):
            x=result2[v].text
        print(x)
        result3 = soup.select("#articleBodyContents")
        for v in range(len(result3)):
            y = result3[v].text.strip()
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
        print(y)
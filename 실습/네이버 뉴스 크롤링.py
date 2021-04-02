<<<<<<< HEAD
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
print(x)
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
print(x)
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
import csv
from bs4 import BeautifulSoup
import requests
file=open("stock.csv",mode="w",encoding="utf-8",newline="")
writer=csv.writer(file)
def print_stock_price(page_num):
    result = [[], [], []]
    for n in range(16,page_num):
        url = 'https://finance.naver.com/item/sise_day.nhn?code=005930&page='+str(n+1)
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"}
        r = requests.get(url,headers=headers)
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        tr = soup.select('table >tr')
        for i in range(1, len(tr)-1):
            if tr[i].select('td')[0].text.strip():
                a=tr[i].select('td')[0].text.strip()
                b=tr[i].select('td')[1].text.strip()
                c=tr[i].select('td')[6].text.strip()
                writer.writerow([a,b,c])
                print(a,b,c)
print_stock_price(18)#5월 1일 까지 4월도 포함됨

# #-----------기사 크롤링 부분-----------------
for i in range(426566,426567):#431050
    urls ='https://news.naver.com/main/read.nhn?mode=LPOD&mid=sec&oid=422&aid=0000'+str(i)
    response = requests.get(urls,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.select(".t11")#날짜
    day=""
    print(urls)
    for v in range(len(result)):
        day=result[v].text
        day=day[:10]#날짜 추출 완료
        print(day)
    result2 = soup.select("#articleTitle")
    for v in range(len(result2)):
        x=result2[v].text
        print(x)#제목
    result3 = soup.select("#articleBodyContents")
    for v in range(len(result3)):
        y = result3[v].text.strip().strip('\n').strip('\r').replace("\t", "").replace("\n", "").replace("\v", "").replace("\f", "").replace("<br>", "")
        print(y)#본문
    result4 = soup.select(".guide_categorization_item")
    for v in range(len(result4)):
        z = result4[v].text.strip()
        print(z)
        #섹터
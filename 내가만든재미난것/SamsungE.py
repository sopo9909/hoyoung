import csv
from bs4 import BeautifulSoup
import requests
import pandas as pd
file=open("stock.csv",mode="w",encoding="utf-8",newline="")
writer=csv.writer(file)
writer.writerow(['date','price','flow'])
def print_stock_price(page_num):
    result = [[], [], []]
    for n in range(page_num):
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
                #print(a,b,c)
print_stock_price(80)
file.close()
file=open("new.csv",mode="w",encoding="utf-8",newline="")
writer=csv.writer(file)
writer.writerow(["day","title","content","sector"])
# #-----------기사 크롤링 부분-----------------
for i in range(426566,431050):#431050
    urls ='https://news.naver.com/main/read.nhn?mode=LPOD&mid=sec&oid=422&aid=0000'+str(i)
    response = requests.get(urls,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.select(".t11")#날짜
    day=""
    title=""
    content=""
    sector=""
    print(urls)
    for v in range(len(result)):
        day=result[v].text
        day=day[:10]#날짜 추출 완료
        #print(day)
    result2 = soup.select("#articleTitle")
    for v in range(len(result2)):
        title=result2[v].text
        #print(x)#제목
    result3 = soup.select("#articleBodyContents")
    for v in range(len(result3)):
        content = result3[v].text.strip().strip('\n').strip('\r').replace("\t", "").replace("\n", "").replace("\v", "").replace("\f", "").replace("<br>", "")
        #print(y)#본문
    result4 = soup.select(".guide_categorization_item")
    for v in range(len(result4)):
        sector = result4[v].text.strip()
        #print(z)
        #섹터
    writer.writerow([day,title,content,sector])
    # ul_list = soup.select('.u_likeit_list_count _count')
    # print(ul_list)
    # for li in ul_list:
    #     good = li.select_one('.u_likeit_list_count _count').text
    #     hunhun = li.select_one('.u_likeit_list_count _count').text
    #     sad = li.select_one('.u_likeit_list_count _count').text
    #     angry = li.select_one('.u_likeit_list_count _count').text
    #     wantnext = li.select_one('.u_likeit_list_button _button off').text
        #print(good)
    # result5 = soup.select(".u_likeit_list_count _count")
    # for v in range(len(result5)):
    #     e = result5[v].text.strip()
    #     print(e)
file.close()
##----------데이터 정리 ------##
stock_data = pd.read_csv('stock.csv',header=0,sep=',')
new_data = pd.read_csv('new.csv',header=0,sep=',')
stock_data = pd.DataFrame(stock_data)
stock_data['new_date'] = pd.to_datetime(stock_data['date'])
new_data = pd.DataFrame(new_data)
new_data['new_date'] = pd.to_datetime(new_data['date'])
import datetime
from datetime import date,timedelta
time = datetime.datetime.strptime('2020-05-01','%Y-%m-%d')
new_data2 = new_data[(new_data["new_date"]>"2020-04-30")&(new_data["new_date"]<"2020-06-01")]
stock_data2 = stock_data[(stock_data["new_date"]>"2020-04-30")&(stock_data["new_date"]<"2020-06-01")]
stock_data2=stock_data2.drop(['date'], axis='columns', inplace=True)
new_data2=new_data2.drop(['date'], axis='columns', inplace=True)
count_news_total=new_data2.groupby('new_date').count()#날짜별 총 기사수
news_samsung = new_data2.loc[new_data2['content'].str.contains('삼성전자',na=False)]
count_news_samsung=news_samsung.groupby('new_date').count()
data_all = pd.merge(stock_data2,count_news_samsung,left_on='new_date',right_on='new_date',how='inner')
#data_all2 = pd.merge(data_all,count_news_samsung,left_on='new_date',right_on='new_date',how='inner')

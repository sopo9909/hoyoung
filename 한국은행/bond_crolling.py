#desigend by Hoyoung
#요곳이 재미짐


from bs4 import BeautifulSoup
import pandas as pd
import requests
import wget

def con(urls):
    headers = {"authority": "finance.naver.com"
,"method": "GET"
,"path": "/research/debenture_list.nhn?keyword=&brokerCode=&searchType=writeDate&writeFromDate=2005-01-01&writeToDate=2021-01-04&x=29&y=27"
,"scheme": "https",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "ko,en;q=0.9,en-US;q=0.8",
"cookie": "NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=V5Q3OA3RX7JF6; nx_ssl=2; naver_stock_codeList=005930%7C252670%7C; page_uid=U/7UZwp0Jy0sslZflkZssssssWs-475281; summary_item_type=recent; recent_board_read=4475; JSESSIONID=91E4EE43EDE52CD2D77C43E56FDC0252",
"referer": "https://finance.naver.com/research/debenture_list.nhn?keyword=&brokerCode=&searchType=writeDate&writeFromDate=2005-01-01&writeToDate=2021-01-04&x=23&y=26",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "same-origin",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"}
    response = requests.get(urls,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all('td',{'class':'file'})
    for link in links:
        news_urlbefore =link.find('a').get('href')
        wget.download(news_urlbefore)
for i in range(1,131):
    urls='https://finance.naver.com/research/debenture_list.nhn?keyword=&brokerCode=&searchType=writeDate&writeFromDate=2005-01-01&writeToDate=2021-01-04&x=23&y=26&page='+str(i)
    con(urls)

#desigend by Hoyoung
#요곳이 재미짐


from time import *
from datetime import *
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import pandas as pd
import datetime
import requests
title_set=[]
datetime_set=[]
article_set=[]
def cond(url):
    headers = {"authority": "search.naver.com",
    "method": "GET",
    "path": "/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2021.01.04&de=2021.01.04&docid=&nso=so%3Ar%2Cp%3Afrom20210104to20210104%2Ca%3Aall&mynews=1&refresh_start=0&related=0",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ko,en-US;q=0.9,en;q=0.8",
    "cookie": "NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=7J5EOJKNQDZF6; nid_inf=809684172; NID_AUT=lPpROqf85py4ARSAzT7KkM82jnuLvdfEmRI1bbOBfp1GKeFuaHWKwvdBE3se8dIj; NID_JKL=kzTdoQevAP+DR3DkqmBUB8Aib16ZU7KuHKixZXDyPnE=; nx_ssl=2; nso_open=1; NID_SES=AAABtDbP95xW4CrZCztiC2Xj+C2uMYgoQ46Mc0D3d+kMn/kGhvRveKtcvGrmdERshAD2Rq0lyBXcuKz6LbuhB0cOWp7cVZXgdKJtXz/j6ZLhlLdPHDg/2xvkxs/Qj7rSIRkPxB+J1/nf5UQ+Gvt1VxNNxYeD7YUpeRNpnyVgNCAaECojvpA7kRpCQ4u4RK8jmMUV0sXqvIVNrUHhcJJhV0pRKs83l7c9kfe5oZ3PzxJmUjdOxdR6Nk6VHfmE/njgRT73DL3Vae4eyRq7ZeoGteyZBw7CVnfOcs6/RVgy6iNWPY+21hlaQDdDFjEG0jWDLE/7L4bHLMZ+h9/ejg9dKZjo4Lr88LMstCX5KtiOANnJSebllewGwl9LfGOy3MPzdh0o1/U4hGSrNG800phEi7KK8Npxg7u3MXDQ2Iz//SEvUUOVafwidGNlZhIonPR7A+5hTgReiGxkft2bysKapmR1nbnglwAkClFOmYPm/mpDx2Kzz5bEj2273vg/R2cF3+1zhZUrPdE1fz9Dk8JYZQeKPmzDXoxGny47uNT8V3c4Z6mZ5IOKsO6FOrbp+CvA2OxQi6fUpJ8MaAZ2rqyu6qoFqIY=; page_uid=U/7fudp0J14ssRKXfYVssssstmo-144945; news_office_checked=1001,1018,2227; news_my_status=1",
    "referer": "https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2021.01.04&de=2021.01.04&docid=&nso=so%3Ar%2Cp%3Afrom20210104to20210104%2Ca%3Aall&mynews=1&refresh_start=0&related=0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all('div',{'class':'news_area'})
    for link in links:
            #press = link.find('span',{'class':'_sp_each_source'}).get_text()
        news_urlbefore =link.find_all('a')#.get('href')
        news_url=news_urlbefore[1].attrs["href"]
        if ('einfomax.co.kr' in news_url):
            new_link = requests.get(news_url,headers={'User-Agent':'Mozilla/5.0'})
            news_html = BeautifulSoup(new_link.text,'html.parser')
            try:
                title = news_html.find('div',{'class':'article-head-title'}).get_text()
            except:
                title=""
            datetime = news_html.find('ul',{'class':'no-bullet auto-marbtm-0 line-height-6'})
        
            try:
                datetime2 = datetime.find_all('li')
                if '승인'in datetime2[1].get_text().strip():
                    datetime2 = datetime2[1].get_text().strip().strip('승인').strip()
            except:
                datetime2=""
            try:
                article= news_html.find('div',{'id':'article-view-content-div'}).get_text().strip().replace("\t", "").replace("\n", "").replace("\v", "").replace("\f", "").replace("<br>", "")
            except:
                article=""
            title_set.append(title)
            datetime_set.append(datetime2[:10])
            article_set.append(article)

        elif ('edaily.co.kr' in news_url):
            new_link = requests.get(news_url,headers={'User-Agent':'Mozilla/5.0'})
            news_html = BeautifulSoup(new_link.text,'html.parser')
            try:
                title = news_html.find('h2').get_text().strip("\t")
            except:
                title=""
            datetime = news_html.find('div',{'class':'dates'})
            datetime2 = datetime.find_all('p')
            try:
                datetime2=datetime2[0].get_text().strip()
            except:
                datetime2=""
            try:
                article= news_html.find('div',{'class':'news_body'}).get_text().strip().replace("\t", "").replace("\n", "")
            except:
                article=""
            title_set.append(title)
            datetime_set.append(datetime2[:10])
            article_set.append(article)
        elif ('yna.co.kr' in news_url):
            new_link = requests.get(news_url,headers={'User-Agent':'Mozilla/5.0'})
            news_html = BeautifulSoup(new_link.text,'html.parser')
            try:
                title = news_html.find('h1',{'class':'tit'}).get_text().strip("\t")
            except:
                title=""
            try:
                datetime = news_html.find('p',{'class':'update-time'})
            except:
                datetime=""
            try:
                datetime = datetime.get_text().strip('송고시간')
            except:
                datetime=""
            article=""
            try:
                article= news_html.find('div',{'class':'story-news article'}).get_text().strip().replace("\t", "").replace("\n", "")
            except:
                article=""
            title_set.append(title)
            datetime_set.append(datetime[:10])
            article_set.append(article)
        elif ('news.naver.com' in news_url):
            new_link = requests.get(news_url,headers={'User-Agent':'Mozilla/5.0'})
            news_html = BeautifulSoup(new_link.text,'html.parser')
            try:
                title = news_html.find('h3',{'id':'articleTitle'}).get_text()
            except:
                title=""
            try:
                datetime = news_html.find('span',{'class':'t11'}).get_text()
            except:
                datetime=""
            try:
                article= news_html.find('div',{'id':'articleBodyContents'}).get_text().strip().replace("\t", "").replace("\n", "")
            except:
                article=""
            title_set.append(title)
            datetime_set.append(datetime[:10])
            article_set.append(article)
        else:
            new_link = requests.get(news_url,headers={'User-Agent':'Mozilla/5.0'})
            news_html = BeautifulSoup(new_link.text,'html.parser')
            title = news_html.find('h3',{'id':'articleTitle'}).get_text()
            datetime = news_html.find('span',{'class':'t11'}).get_text()
            article= news_html.find('div',{'id':'articleBodyContents'}).replace("\t", "").replace("\n", "")
            title_set.append(title)
            datetime_set.append(datetime[:10])
            article_set.append(article)

url_query =quote('금리')
thirty=5100
now = datetime.datetime.now()
for i in range(5101,5401):#5848-일 반복
    now_minus= now - datetime.timedelta(days=i)
    x=now_minus.strftime('%Y.%m.%d')
    y=now_minus.strftime('%Y%m%d')
    url ='https://search.naver.com/search.naver?where=news&query='+url_query+'&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds={}&de={}&docid=&nso=so%3Ar%2Cp%3Afrom{}to{}%2Ca%3Aall&mynews=1&refresh_start=0&related=0'.format(x,x,y,y)
    cond(url)
    print("여기까지"+str(i))
    try:
        headers = {"authority": "search.naver.com",
        "method": "GET",
        "path": "/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2021.01.04&de=2021.01.04&docid=&nso=so%3Ar%2Cp%3Afrom20210104to20210104%2Ca%3Aall&mynews=1&refresh_start=0&related=0",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ko,en-US;q=0.9,en;q=0.8",
        "cookie": "NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=7J5EOJKNQDZF6; nid_inf=809684172; NID_AUT=lPpROqf85py4ARSAzT7KkM82jnuLvdfEmRI1bbOBfp1GKeFuaHWKwvdBE3se8dIj; NID_JKL=kzTdoQevAP+DR3DkqmBUB8Aib16ZU7KuHKixZXDyPnE=; nx_ssl=2; nso_open=1; NID_SES=AAABtDbP95xW4CrZCztiC2Xj+C2uMYgoQ46Mc0D3d+kMn/kGhvRveKtcvGrmdERshAD2Rq0lyBXcuKz6LbuhB0cOWp7cVZXgdKJtXz/j6ZLhlLdPHDg/2xvkxs/Qj7rSIRkPxB+J1/nf5UQ+Gvt1VxNNxYeD7YUpeRNpnyVgNCAaECojvpA7kRpCQ4u4RK8jmMUV0sXqvIVNrUHhcJJhV0pRKs83l7c9kfe5oZ3PzxJmUjdOxdR6Nk6VHfmE/njgRT73DL3Vae4eyRq7ZeoGteyZBw7CVnfOcs6/RVgy6iNWPY+21hlaQDdDFjEG0jWDLE/7L4bHLMZ+h9/ejg9dKZjo4Lr88LMstCX5KtiOANnJSebllewGwl9LfGOy3MPzdh0o1/U4hGSrNG800phEi7KK8Npxg7u3MXDQ2Iz//SEvUUOVafwidGNlZhIonPR7A+5hTgReiGxkft2bysKapmR1nbnglwAkClFOmYPm/mpDx2Kzz5bEj2273vg/R2cF3+1zhZUrPdE1fz9Dk8JYZQeKPmzDXoxGny47uNT8V3c4Z6mZ5IOKsO6FOrbp+CvA2OxQi6fUpJ8MaAZ2rqyu6qoFqIY=; page_uid=U/7fudp0J14ssRKXfYVssssstmo-144945; news_office_checked=1001,1018,2227; news_my_status=1",
        "referer": "https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2021.01.04&de=2021.01.04&docid=&nso=so%3Ar%2Cp%3Afrom20210104to20210104%2Ca%3Aall&mynews=1&refresh_start=0&related=0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        next =soup.find('a',{'class':'btn_next'}).get('href')
        url2 = 'https://search.naver.com/search.naver' + next
        cond(url2)
    except:
        pass
    if i%30==0:
        newsdata_set={'date':datetime_set,'title':title_set,'content':article_set}
        newsdata_set=pd.DataFrame(newsdata_set)
        newsdata_set.to_csv('newsdata_set'+str(thirty)+'.csv',encoding='utf-8')
        thirty+=1

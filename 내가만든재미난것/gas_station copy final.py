from pandas.io.stata import value_label_mismatch_doc
import csv
import re
import requests
from requests.models import Response
from requests.sessions import session
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
URL = 'https://www.opinet.co.kr/searRgSelect.do'
session = requests.session()
gugu=['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구','도봉구','동대문구','동작구','마포구','서대문구','서초구','성동구','성북구','송파구','양천구','영등포구','용산구','은평구','종로구','중구','중랑구']
sector_list=[]
price_list=[]
name_lst=[]
brand_list=[]
adress_list=[]
selfgasY_list=[]
for i in gugu:
    data = {"BTN_DIV": "os_btn",
            "BTN_DIV_STR": None,
            "POLL_ALL": "all",
            "SIDO_NM": "서울특별시",
            "SIGUNGU_NM": i,
            "SIDO_CD": "01",
            "SIGUN_CD": "0101",
            "MAP_CENTER_X": None, 
            "MAP_CENTER_Y": None, 
            "MAP_ZOOM": None,
            "MAP_FIRST_X": None, 
            "MAP_FIRST_Y": None, 
            "LPG_YN": None,
            "SESSION_USER_ID": None,
            "SIDO_NM0": "서울특별시",
            "SIGUNGU_NM0": i,
            "DONG_NM": None, 
            "GIS_X_COOR": None, 
            "GIS_Y_COOR": None,
            "GIS_X_COOR_S": None, 
            "GIS_X_COOR_E": None,
            "GIS_Y_COOR_S": None,
            "GIS_Y_COOR_E": None,
            "SEARCH_MOD": "addr",
            "OS_NM": None,
            "OS_ADDR": None,
            "NORM_YN": "on",
            "SELF_DIV_CD": "on",
            "VLT_YN": "on",
            "KPETRO_YN": "on",
            "KPETRO_DP_YN": "on",
            "POLL_DIV_CD": "SKE",
            "POLL_DIV_CD": "GSC",
            "POLL_DIV_CD": "HDO",
            "POLL_DIV_CD": "SOL",
            "POLL_DIV_CD": "RTO",
            "POLL_DIV_CD": "ETC"}
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ko,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "588",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "WMONID=sZViNtz61vJ; JSESSIONID=azzAwqA4v7da7ZMpTUZnakIKXdDPn29laeGqE1vQbqNm6y21VEyVYZmAFVUXaumC.b3BpbmV0X2RvbWFpbi9vcGluZXQxLTE=; NetFunnel_ID=5002%3A200%3Akey%3DCD1FA963BDBA67F749822E2E1FD568A12B59DE7CB9456AA675AEC1FBDA3CE9F3591E3E543E076439F9E9A56E2B079EE39512A42EF93688E05898BEAEA5132364D81C7703A9CB6C9C3EC52EC3E7349681C05C4FB4A117B63488D854A91AD6BDF1AD0F18A36EF9F31178B8EEAEA42BD451%26nwait%3D0%26nnext%3D0%26tps%3D0%26ttl%3D0%26ip%3Dnfl.opinet.co.kr%26port%3D443",
    "Host": "www.opinet.co.kr",
    "Origin": "https://www.opinet.co.kr",
    "Referer": "https://www.opinet.co.kr/searRgSelect.do",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    response=session.post(URL,data=data,headers=headers)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    li_list = soup.select('tbody tr')
    for li in li_list:
        #dateq =li.find("a")["href"]
        try:
            dateq =li.select_one("a").attrs["href"]
            dateqset=re.findall(r"'.*?'",dateq)
            sector = i
            price = int(dateqset[2].strip("''"))
            if dateqset[22] == "'SKE'":
                name = dateqset[23].strip("''")
                brand = dateqset[22].strip("''")
            else:
                name = dateqset[22].strip("''")
                brand = dateqset[23].strip("''")
            adress = dateqset[25].strip("''")
            try:
                self_gas=li.select_one('span').text
                if self_gas == '셀프':
                    selfgasY ='Y'
                else:
                    selfgasY='N'
            except AttributeError as e:
                selfgasY='N'
            sector_list.append(sector)
            price_list.append(price)
            name_lst.append(name)
            brand_list.append(brand)
            adress_list.append(adress)
            selfgasY_list.append(selfgasY)
        except AttributeError as e:
            pass
oilstation_data={
    '지역':sector_list,
    '유가':price_list,
    '주유소명':name_lst,
    '브랜드':brand_list,
    '주소':adress_list,
    '셀프주유소여부':selfgasY_list
}
oilstation_data=pd.DataFrame(oilstation_data)
oilstation_data2=oilstation_data.drop_duplicates('주유소명',keep='first')
oilstation_data2.to_csv('gas_station.csv',encoding='utf-8')
open_data = pd.read_csv('gas_station.csv',engine='python',encoding='utf-8')
print(open_data.sort_values(by=['유가']).head(5))
print(open_data.sort_values(by=['유가'],ascending=[False]).head(5))
print(open_data.sort_values(by=['유가']).groupby('셀프주유소여부').head(1))
print(open_data.sort_values(by=['유가']).groupby('지역').head(1))
resulut_min=open_data.groupby('지역').min()
print(resulut_min)

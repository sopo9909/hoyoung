<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
import re

URL = 'https://store.musinsa.com/app/items/lists/001'

def print_url():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    li_list = soup.select('#searchList li[class="li_box"] div[class="article_info"]')
    for li in li_list:
        brand = li.select_one('p[class="item_title"]>a').text
        name = li.select_one('p[class="list_info"]>a').attrs['title']
        price = li.select_one('p[class="price"]').text
        li_price = price.split()
        if len(li_price)==2 :
            price_discount = li_price[1]
        else: price_discount = li_price[0]
        print('브랜드:', brand,'\n''제품명:',name,'\n''가격:',price_discount,'\n')
        
for page in range(1,11):
    URL = URL+'?device=&d_cat_cd=001&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page='+str(page)+'&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&size=&tags=&sale_campaign_yn=&timesale_yn=&q='
=======
import requests
from bs4 import BeautifulSoup
import re

URL = 'https://store.musinsa.com/app/items/lists/001'

def print_url():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    li_list = soup.select('#searchList li[class="li_box"] div[class="article_info"]')
    for li in li_list:
        brand = li.select_one('p[class="item_title"]>a').text
        name = li.select_one('p[class="list_info"]>a').attrs['title']
        price = li.select_one('p[class="price"]').text
        li_price = price.split()
        if len(li_price)==2 :
            price_discount = li_price[1]
        else: price_discount = li_price[0]
        print('브랜드:', brand,'\n''제품명:',name,'\n''가격:',price_discount,'\n')
        
for page in range(1,11):
    URL = URL+'?device=&d_cat_cd=001&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page='+str(page)+'&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&size=&tags=&sale_campaign_yn=&timesale_yn=&q='
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
    print_url()
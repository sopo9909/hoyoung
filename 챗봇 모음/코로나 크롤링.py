from bs4 import BeautifulSoup
import requests
html = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98',headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(html.text, 'html.parser')
data1 = soup.find('div', {'class':'status_info'})
#print(data1)
total_corona = data1.find('p', {'class':'info_num'}).text
print(total_corona)
corona = data1.find('em', {'class':'info_variation'}).text
print(corona)
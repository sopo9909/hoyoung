from bs4 import BeautifulSoup
import requests
import pandas as pd
pos_text=[]
man=[]
for i in range(1,5):
    html = requests.get('https://sqlplus.tistory.com/entry/%EA%B8%8D%EC%A0%95%EC%97%90-%EA%B4%80%ED%95%9C-100%EB%8C%80-%EB%AA%85%EC%96%B8-'+str(i)+'4?category=621818',headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(html.text, 'html.parser')
    data1 = soup.find('div', {'class':'tt_article_useless_p_margin'})
    #print(data1)
    total_corona = data1.find_all('div', {'class':'txc-textbox'})#.text
    for j in total_corona:
        s=j.text
        s=s.replace('\xa0',"")
        s=s.replace('\r\n',"")
        s=s.split('-')
        pos_text.append(s[0])
        man.append(s[1])
all_pos={'긍정말':pos_text,'사람':man}
all_pos=pd.DataFrame(all_pos)
all_pos.to_csv('all_pos.csv',encoding='utf-8')
print(pos_text)
print('#############')
print(man)
# corona = data1.find('em', {'class':'info_variation'}).text
# print(corona)
#desigend by Hoyoung
#요곳이 재미짐


import pandas as pd
import numpy as np
news_all=pd.read_csv('result1.csv')
def sort(n):
    try:
        a=n.replace('\n',"").replace('\r',"")
    except:
        a=n
    return a
news_all['new_content'] = news_all['content'].apply(sort)
news_all.dropna(axis=0)
del news_all['content']
news_all=news_all.replace(r'^\s*$', np.nan, regex=True)
news_all.dropna(axis=0)
news_all.dropna()

a=[]
for i in range(105447,105847):
    a.append(i)
news_all.drop(a,inplace=True)
news_all.to_csv('result_news.csv',encoding='utf-8')
#desinged by 호영

down_ngram_list = []
for i in range(len(df_down)):
    df_down['ngrams'][i]=str(df_down['ngrams'][i])
    down_ngram_list += df_down['ngrams'][i].split(',')
temp_df = pd.DataFrame({'down_count': down_ngram_list})
down_count_df = pd.DataFrame(temp_df['down_count'].value_counts()).reset_index(drop=False)
up_Total = df_newdata['up_count'].sum()
down_Total = df_newdata['down_count'].sum()

for i in range(len(df_newdata)):
    polarity.append((df_newdata['up_count'][i]/up_Total)/(df_newdata['down_count'][i]/down_Total))
df_newdata['polar_score']=polarity
def Polari(n):
    if n > 1.3:
        a='Hawkish'
    elif n <0.76:
        a='Dovish'
    else:
        a='nothing'
    return a
df_newdata['polarity'] = df_newdata['polar_score'].apply(Polari)
df_dicpos = df_newdata[df_newdata['polarity']=='Hawkish'].reset_index(drop=True)
df_dicneg = df_newdata[df_newdata['polarity']=='Dovish'].reset_index(drop=True)

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import re
pos=""
neg=""
for i in range(len(df_dicpos)):
    a=df_dicpos['index'][i].strip('/')
    a=a.replace('/','')
    a=a.replace('N','')
    a=a.replace('G','')
    a=a.replace('V','')
    a=a.replace(';','')
    pos = pos + a*int(df_dicpos['up_count'][i]) + " "
for i in range(len(df_dicneg)):
    b=df_dicneg['index'][i].strip('/')
    b=b.replace('/','')
    b=b.replace('N','')
    b=b.replace('G','')
    b=b.replace('V','')
    b=b.replace(';','')
    neg = neg + b*int(df_dicneg['down_count'][i]) + " "
wordcloud = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',max_font_size=300,stopwords=STOPWORDS,background_color='#FFFFFF',width=1800,height=1200).generate(' '.join(pos))
plt.figure(figsize=(5,5))
plt.imshow(wordcloud)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()
wordcloud = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',max_font_size=300,stopwords=STOPWORDS,background_color='#FFFFFF',width=1800,height=1200).generate(' '.join(neg))
plt.figure(figsize=(5,5))
plt.imshow(wordcloud)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()
<<<<<<< HEAD
#word는 한 문장 넣는 거
#designed by 호영
# def make_freqlist(ngrams):
#     freqlist={}
#     for ngram in ngrams:
#         if (ngram in freqlist):
#             freqlist[ngram]+=1
#         else:
#             freqlist=1
#     return freqlist
# df_newdata = pd.merge(A, B, left_on='', right_on='key', how='outer')
# df_newdata['up_count'].fillna(0)
# df_newdata['down_count'].fillna(0)
# df_newdata['total_count'] = df_newdata['up_count']+df_newdata['down_count']
# indexNames =df_newdata[df_newdata['total_count']<=15].index
# df_newdata.drop(indexNames,inplace=True)
# polarity=[]

# # #up_count의 총합
# # ################################################################################################################
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
pos=""
neg=""

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

text='안녕하세요 저는 황호영 입니다 오늘은 우리의 마지막 날이예요 여러분 고생하셨구요 사랑은 아니지만 좋아합니다'
alice_mask=np.array(Image.open('alice_mask.png'))
stopword = set(STOPWORDS)
stopword.add("said")
wc = WordCloud(background_color="white",max_words=200,mask=alice_mask,stopwords=stopword)
wc = wc.generate(text)
plt.figure(figsize=(8,8))
plt.imshow(alice_mask,cmap=plt.cm.gray,interpolation='bilinear')
plt.axis("off")
plt.show

for i in range(len(df_dicpos)):
    pos = pos + df_dicpos['index'][i]*df_dicpos['up_count'][i] + " "
for i in range(len(df_dicneg)):
    neg = neg + df_dicneg['index'][i]*df_dicneg['down_count'][i] + " "
wordcloud = WordCloud(max_font_size=200,font_path='./NanumGothic.ttf',stopwords=STOPWORDS,background_color='#FFFFFF',width=1200,height=800).generate(' '.join(pos))
plt.figure(figsize=(5,5))
plt.imshow(wordcloud)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()
wordcloud = WordCloud(max_font_size=200,font_path='./NanumGothic.ttf',stopwords=STOPWORDS,background_color='#FFFFFF',width=1200,height=800).generate(' '.join(neg))
#%matplotlib inline #노트북 안에 그래프가 디스플레이
plt.figure(figsize=(5,5))
plt.imshow(wordcloud)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()
# df=[[],[]]
# #의사록 데이터 프레임 df로 가정
# import pandas as pd
# df= pd.read_csv('call_rate1.csv')
# for i in range(len(df)): # 문장으로 쪼갬 a는 한 회의록의 문장의 집합
#     a=df['content'][i].split('.')
#     total_score=0
#     for x in a:
#         tokens = mpck.tokenize(str(x)) #x는 a중에 한 문장
#         ngrams=mpck.ngramize(tokens)
#         pos=0
#         neg=0
#         for t in ngrams: # t는 한 글자
#             if t in df_dicpos["index"]:
#                 pos += 1
#             elif t in df_dicneg["index"]:
#                 neg +=1
#             else:
#                 continue
#         text_score=(pos-neg)/(pos+neg)
#     total_score=total_score+text_score

        ####### a를 또 ngram 분리 만약에 문장 안에 dicpos를 다 빼와 dicneg도
        # 그러면 문장별로 pos, neg 구별 -> 갯수로 점수 구하기
        # 점수를 구한 것을 모두 더 하기 
#df_newdata
#
# if df_newdata['total_count'] >

=======
#word는 한 문장 넣는 거
#designed by 호영
# def make_freqlist(ngrams):
#     freqlist={}
#     for ngram in ngrams:
#         if (ngram in freqlist):
#             freqlist[ngram]+=1
#         else:
#             freqlist=1
#     return freqlist
# df_newdata = pd.merge(A, B, left_on='', right_on='key', how='outer')
# df_newdata['up_count'].fillna(0)
# df_newdata['down_count'].fillna(0)
# df_newdata['total_count'] = df_newdata['up_count']+df_newdata['down_count']
# indexNames =df_newdata[df_newdata['total_count']<=15].index
# df_newdata.drop(indexNames,inplace=True)
# polarity=[]

# # #up_count의 총합
# # ################################################################################################################
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
pos=""
neg=""

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

text='안녕하세요 저는 황호영 입니다 오늘은 우리의 마지막 날이예요 여러분 고생하셨구요 사랑은 아니지만 좋아합니다'
alice_mask=np.array(Image.open('alice_mask.png'))
stopword = set(STOPWORDS)
stopword.add("said")
wc = WordCloud(background_color="white",max_words=200,mask=alice_mask,stopwords=stopword)
wc = wc.generate(text)
plt.figure(figsize=(8,8))
plt.imshow(alice_mask,cmap=plt.cm.gray,interpolation='bilinear')
plt.axis("off")
plt.show

for i in range(len(df_dicpos)):
    pos = pos + df_dicpos['index'][i]*df_dicpos['up_count'][i] + " "
for i in range(len(df_dicneg)):
    neg = neg + df_dicneg['index'][i]*df_dicneg['down_count'][i] + " "
wordcloud = WordCloud(max_font_size=200,font_path='./NanumGothic.ttf',stopwords=STOPWORDS,background_color='#FFFFFF',width=1200,height=800).generate(' '.join(pos))
plt.figure(figsize=(5,5))
plt.imshow(wordcloud)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()
wordcloud = WordCloud(max_font_size=200,font_path='./NanumGothic.ttf',stopwords=STOPWORDS,background_color='#FFFFFF',width=1200,height=800).generate(' '.join(neg))
#%matplotlib inline #노트북 안에 그래프가 디스플레이
plt.figure(figsize=(5,5))
plt.imshow(wordcloud)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()
# df=[[],[]]
# #의사록 데이터 프레임 df로 가정
# import pandas as pd
# df= pd.read_csv('call_rate1.csv')
# for i in range(len(df)): # 문장으로 쪼갬 a는 한 회의록의 문장의 집합
#     a=df['content'][i].split('.')
#     total_score=0
#     for x in a:
#         tokens = mpck.tokenize(str(x)) #x는 a중에 한 문장
#         ngrams=mpck.ngramize(tokens)
#         pos=0
#         neg=0
#         for t in ngrams: # t는 한 글자
#             if t in df_dicpos["index"]:
#                 pos += 1
#             elif t in df_dicneg["index"]:
#                 neg +=1
#             else:
#                 continue
#         text_score=(pos-neg)/(pos+neg)
#     total_score=total_score+text_score

        ####### a를 또 ngram 분리 만약에 문장 안에 dicpos를 다 빼와 dicneg도
        # 그러면 문장별로 pos, neg 구별 -> 갯수로 점수 구하기
        # 점수를 구한 것을 모두 더 하기 
#df_newdata
#
# if df_newdata['total_count'] >

>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62

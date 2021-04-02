import pandas as pd
from ekonlpy.sentiment import MPCK
mpck = MPCK()
a = pd.read_csv('w')#의사록 분류한 것 csv
pos = pd.read_csv('긍정사전수정.csv')#긍정사전
neg = pd.read_csv('부정사전수정.csv')#부정사전
contentTone_list=[]
for b in a :#전체 의사록 중에 하나 뽑기
    x=b.split('.')#문장 나누기
    up = 0
    down =0
    ngram_list=[]
    for i in x: #하나의 의사록에서 하나의 문장씩
        #문장 하나씩 구조분석
        tokens = mpck.tokenize(i)
        ngrams=mpck.ngramize(tokens)
        ngram_list.append(ngrams)
        posS = 0
        negG = 0
        for j in ngram_list:
            if j in pos:
                posS += 1
            elif j in neg:
                negG +=1
            else:
                pass
        sentence_tone = (posS-negG)/(posS+negG)
        if sentence_tone < 0 :
            down +=1
        elif sentence_tone == 0 :
            pass
        else :
            up +=1
    contentTone=(up-down)/(up+down)
    contentTone_list.append(contentTone)
#기준금리를 저기에 더하기
#다영한테 준 코드 쓰기 - 기준금리
#상관관계분석
#df=pd.DataFrame(lst).T
#corr = df.corr(method='pearson)
#print(corr)
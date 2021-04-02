import re
file = open("KETI_대화데이터_일상_오피스.txt", "r",encoding='utf-8')
strings = file.readlines()
#print(strings)
strings1=[]
for i in strings:
    text = re.sub('[a-zA-Z]','',i).strip()
    text = re.sub('[1\t]','',text).strip()
    text = re.sub('[2]','',text).strip()
    text = re.sub('[.]','',text).strip()
    text = re.sub('[""]','',text).strip()
    text = re.sub('[,]','',text).strip()
    text = text.replace('컴패니언',"호영님이 만든 짱구")#컴패니언이에요
    text = text.replace('컴패니언이에요',"호영님이 만들어주신 짱구이에요")
    text = text.replace('컴패니언입니다',"호영님이 만들어준 짱구입니다")
    if(text !=""):
        strings1.append(text)
#print(strings1[0])
#print(strings1[1])
import pandas as pd
import csv
f = open('text_sort.csv','w',encoding='utf-8',newline='')
wr = csv.writer(f)
wr.writerow(['Q','A','label'])
for i in range(0,len(strings1),2):
    a=strings1[i]
    b=strings1[i+1]
    c=0
    wr.writerow([a,b,c])


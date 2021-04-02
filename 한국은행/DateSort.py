#desigend by Hoyoung
#요곳이 재미짐


import pandas as pd
import datetime
date_data=[]
rate_data2=[]
def rate(star,en,rat):
    data = pd.date_range(start=star,end=en)
    data_list = data.strftime("%Y-%m-%d").tolist()
    for num in data_list :
        date_data.append(num)
        rate_data2.append(rat)

db = pd.read_csv("C:/Users/701/kdigital/lecture/nom_rate.csv",header=0,encoding='utf-8')
db=pd.DataFrame(db)
#- datetime.timedelta(days=i)
now = datetime.datetime.now()
now = datetime.datetime.strftime(now,"%Y.%m.%d")
converstart2 = db['날짜'][0]
rate(converstart2,now,db["기준금리"][0])

for i in range(32):#len(db['날짜'])):
    converstart = datetime.datetime.strptime(db['날짜'][i+1],"%Y.%m.%d").date()
    a=converstart- datetime.timedelta(days=1)
    converend = db['날짜'][i]
    rate(a - datetime.timedelta(days=1),converend,db["기준금리"][i+1])
    if a.strftime("%Y.%m.%d")=="2004.11.11":
        break
Rate_dataS={
    '날짜':date_data,
    '기준금리':rate_data2
}
Rate_dataS =pd.DataFrame(Rate_dataS)
Rate_dataS2 = Rate_dataS.drop_duplicates("날짜",keep="first")
Rate_dataS2 =Rate_dataS2.sort_values(by="날짜",ascending=False)
Rate_dataS2.to_csv('Rate_dataS2.csv',encoding='utf-8')
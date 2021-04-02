#desigend by Hoyoung
#요곳이 재미짐


import pandas as pd
import datetime
from datetime import timedelta
df= pd.read_csv('call_rate1.csv')
def daycopy(n):
    n1 = datetime.datetime.strptime(n,'%Y.%m.%d')
    time1 = n1 - timedelta(28)
    return time1
df['date2'] = df['date'].apply(daycopy)
#print(df.index)
call_2=[]
for i in range(28,len(df['콜금리'])+28):
    if i >= len(df['콜금리']) :
        call_2.append(0)
    else:
        call_2.append(df['콜금리'][i])
df["call2"]=call_2
up_down=[]
def up_down_call():
    for i in range(len(df['콜금리'])):
        if df["콜금리"][i]>df["call2"][i]:
            up_down.append('up')
        elif df["콜금리"][i]==df["call2"][i]:
            up_down.append('same')
        else:
            up_down.append('down')
up_down_call()
df["up_down"]=up_down
a=[]
for i in range(2837,2865):
    a.append(i)
df.drop(a,inplace=True)
print(df)
df.to_csv('call_rate_final.csv', encoding='utf-8')

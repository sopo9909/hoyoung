import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def change_date(n) :
    n = str(n)
    return n[:4]+"-"+n[4:6]+"-"+n[6:]

print('hello')

plt.rc('font',family='Malgun Gothic')
kr_daily = pd.read_csv('kr_daily.csv',header=0)
kr_daily['new_date'] = kr_daily['date'].apply(change_date)
kr_daily.index = kr_daily['new_date']
plt.figure(figsize=(12,5))
plt.subplot(121)
plt.xticks(rotation=80)
plt.plot(kr_daily["2020-05-18":]['confirmed'].index,kr_daily["2020-05-18":]['confirmed'].values,":r")
plt.title("확진자")
plt.show()
pd.to_datetime()
plt.subplot(122)
plt.rc('font',family='Malgun Gothic')
plt.xticks(rotation=80)
plt.bar(kr_daily["2020-05-18":]['death'].index,kr_daily["2020-05-18":]['death'].values,color='r')
plt.title("사망자")
plt.show()
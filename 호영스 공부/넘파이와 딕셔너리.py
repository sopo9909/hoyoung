import pandas as pd
import missingno as msno
import numpy as np

bank_dt = pd.read_csv('bank.csv')
bank_dt.info()
print(bank_dt.describe())
msno.matrix(bank_dt, figsize=(12,5),sparkline=False)

bank_dt = bank_dt.fillna({'contact':'unknown'})

time_index = pd.date_range("2020/01/01",periods=5,freq ="MS")
print(time_index)

df = pd.DataFrame(index = time_index)
df["Sales"] = [1.0,2.0,np.nan,np.nan,5.0]
df.interpolate()
df.ffill()
df.fillna(method='ffill')
df.bfill()
df.fillna(method="bfill")
df.interpolate(limit =2,limit_direction="forward") #limit 갯수만큼 채워짐
df.interpolate(limit =2,limit_direction="backward")

dict = {'One' :  [np.nan, np.nan, 95, 80],
    'Two' : [np.nan, np.nan, np.nan, np.nan],
    'Three':[52, np.nan, 80, 98],
    'Four':[np.nan, np.nan, np.nan, 65],
    'Five':[10, None, 30, 40],
    'Six': [np.nan, np.nan, np.nan, pd.NaT],
    'Seven': [np.nan, np.nan, None, np.nan],
    'Eight': [np.nan, np.nan, None, pd.NaT]}

df = pd.DataFrame(dict)
df.dropna(how="all")
df.dropna(how="all",axis=1)
df.dropna(subset=['One','Four'])

df['Year'] = df['new_Data'].dt.year
bank_dt[bank_dt['age'] < 8]
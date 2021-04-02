import pandas as pd
import mapboxgl
from mapboxgl.viz import *
import json
import os
from mapboxgl.utils import create_color_stops
with open('32.세종시_행정경계(읍면동).geojson',mode='rt',encoding='utf-8') as f:
    data = json.loads(f.read())
    f.close()
def rep(df):
    return df.replace(' ','')
data2=pd.read_csv('28.세종시_지역별_세대원수별_세대수.csv')
data2['1인비율']=data2['1인']/data2['계']
data2['2인비율']=data2['2인']/data2['계']
data2['3인이상비율']=(data2['계']-data2['1인']-data2['2인'])/data2['계']
data2['읍면동']=data2['읍면동'].apply(rep)
data3=data2.set_index("읍면동")
data3=data3.reindex(index=["조치원읍","연기면","연동면","부강면","금남면","장군면","연서면","전의면","전동면","소정면","도담동","고운동","종촌동","소담동","새롬동","아름동","한솔동","대평동","보람동"])
for i in range(19):
    data['features'][i]['properties']['1인비율']=data3.iloc[i]['1인비율']
    data['features'][i]['properties']['2인비율']=data3.iloc[i]['2인비율']
    data['features'][i]['properties']['3인이상비율']=data3.iloc[i]['3인이상비율']
token = os.getenv('pk.eyJ1Ijoic29wbzExMjMiLCJhIjoiY2ttbHVhOGE2MWUyYjJwbnowZ3B3NGh4YSJ9.jQpNT0TEodUp7FIcqKco5A')
center = [36.3, 127.16]
color_breaks = [0, 0.2, 0.3, 0.4, 0.5, 0.6]
color_stops = create_color_stops(color_breaks, colors='BuPu')
viz = ChoroplethViz(
    access_token=token,
    data=data,
    color_property='1인비율',
    color_stops=color_stops,
    center=center,
    zoom=10)
viz.show()
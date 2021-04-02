<<<<<<< HEAD
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
data=[{"price":120,"rooms":3,"location":"잠실동"},
{"price":1640,"rooms":2,"location":"천호동"},
{"price":1503,"rooms":1,"location":"신천동"},
{"price":14220,"rooms":21,"location":"방화동"},
{"price":17110,"rooms":5,"location":"잠실동"},
{"price":1120,"rooms":32,"location":"마곡동"}]

dv = DictVectorizer(sparse =False,dtype = np.int)#sparse =True 하면 압축하는 것
print(dv.fit_transform(data))#이름 바꾼 것이 가장 먼저 나옴#
dv.get_feature_names()#내가 바꾼 이름 나옴

text =["mobile phone","battlegrounds mobile game","phone game"]
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x = cv.fit_transform(text)
import pandas as pd
a=pd.DataFrame(x.toarray(),columns=cv.get_feature_names())
print(a)

text1 =["모바일 폰","배틀그라운드 모바일 게임","폰 게임"]
x = cv.fit_transform(text1)
a=pd.DataFrame(x.toarray(),columns=cv.get_feature_names())
print(a)

X=np.array([[np.nan,0,3],[3,7,9],[3,5,2],[4,np.nan,6],[8,8,1]])
y=np.array([14,16,-1,8,-5])
#from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer
imp = SimpleImputer(strategy='mean')
X2=imp.fit_transform(X)
print(X2)
model = LinearRegression()
model.fit(X2,y)
=======
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
data=[{"price":120,"rooms":3,"location":"잠실동"},
{"price":1640,"rooms":2,"location":"천호동"},
{"price":1503,"rooms":1,"location":"신천동"},
{"price":14220,"rooms":21,"location":"방화동"},
{"price":17110,"rooms":5,"location":"잠실동"},
{"price":1120,"rooms":32,"location":"마곡동"}]

dv = DictVectorizer(sparse =False,dtype = np.int)#sparse =True 하면 압축하는 것
print(dv.fit_transform(data))#이름 바꾼 것이 가장 먼저 나옴#
dv.get_feature_names()#내가 바꾼 이름 나옴

text =["mobile phone","battlegrounds mobile game","phone game"]
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x = cv.fit_transform(text)
import pandas as pd
a=pd.DataFrame(x.toarray(),columns=cv.get_feature_names())
print(a)

text1 =["모바일 폰","배틀그라운드 모바일 게임","폰 게임"]
x = cv.fit_transform(text1)
a=pd.DataFrame(x.toarray(),columns=cv.get_feature_names())
print(a)

X=np.array([[np.nan,0,3],[3,7,9],[3,5,2],[4,np.nan,6],[8,8,1]])
y=np.array([14,16,-1,8,-5])
#from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer
imp = SimpleImputer(strategy='mean')
X2=imp.fit_transform(X)
print(X2)
model = LinearRegression()
model.fit(X2,y)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
y_pred = model.predict(X2)
<<<<<<< HEAD
#%%
from os import sep
from matplotlib.colors import Normalize
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
redwine = pd.read_csv('c:/Users/701/kdigital/lecture/winequality-red.csv',sep=";",header=0)#파일이 안 나눠져있으니,sep으로 나눠줌. header = 0 <-제목이 0번째 있으면 이렇게 씀
redwine['type']='red'
#print(redwine)
whitewine = pd.read_csv('c:/Users/701/kdigital/lecture/winequality-white.csv',sep=";",header=0)
whitewine['type']='white'
wine_set = redwine.append(whitewine) #데이터 프레임 합치기
#print(wine_set.shape)
#print(wine_set["type"].value_counts())#몇 개씩 구성되어 있는 지 파악
#print(wine_set.type.value_counts())#몇 개씩 구성되어 있는 지 파악

wine_set.columns#컬룸이 무엇이 있는 지 확인
wine_setcolumns2 =[]
###컬룸 명 바꾸기
#new_col=["a","b","c","d","e"]
#wine_set.columns=new_col
for i in wine_set.columns:
    a= i.replace(" ","_")
    wine_setcolumns2.append(a)
wine_set.columns = wine_setcolumns2
#한 라인으로 바꾸기 wine.columns = wine.columns.str.replace(" ","_")
#print(wine_set.columns)
wine_set.describe()#요약 통계량 보여주기
wine_set.quality.describe()#퀄리티라는 컬럼만 요약하기
wine_set.quality.unique()#퀄리티 안의 특정값 추출
wine_set.quality.value_counts()

wine_set.groupby('type')["quality"].describe()#그룹으로 해서 요약 통계
wine_set.groupby('type')["quality"].quantile([0,0.25,0.5,0.75,1]).unstack("type")#5개로 분류 & 데이터 프레임으로 변환
red_q = wine_set.loc[wine_set["type"]=="red","quality"]
white_q = wine_set.loc[wine_set["type"]=="white","quality"]
#print(red_q)
#print(white_q)
# sns.set_style()
# sns.distplot(red_q,norm_hist = True,kde = False,color="red",label="Red Wine")
# sns.distplot(white_q,norm_hist = True,kde = False,color="blue",label="White Wine")
# plt.title("Distribution of Quality of Wine Type")
# plt.xlabel("Quality Score")
# plt.ylabel("Density")#norm_hist=True - 밀도 norm_hist=False - 개수
# plt.legend()
wine_set.groupby("type")['quality'].aggregate(["std","mean"])
import statsmodels.api as sm
t_stat,p_value, df = sm.stats.ttest_ind(red_q,white_q)
"t-stat: {:.3f},p-value:{:.4f}".format(t_stat,p_value)

wine_corr = wine_set.corr()
plus_cor=wine_corr.loc[wine_corr["quality"] > 0,"quality"]
minus_cor=wine_corr.loc[wine_corr["quality"] < 0,"quality"]
#print(plus_cor)
#print(minus_cor)
red_sample = wine_set.loc[wine_set["type"]=="red",:]
white_sample = wine_set.loc[wine_set["type"]=="white",:]
red_idx = np.random.choice(red_sample.index,replace=True,size=200)
white_idx = np.random.choice(white_sample.index,replace=True,size=200)
wine_sample = red_sample.loc[red_idx,].append(white_sample.loc[white_idx,])
wine_sample.head()
sns.set_style("dark")
sns.pairplot(wine_sample,vars=["quality","alcohol","residual_sugar"],kind="reg",plot_kws={"ci":False,"x_jitter":0.25,"y_jitter":0.25},diag_kind="hist",diag_kws={"bins":10,"alpha":1},hue="type",palette=dict(red="red",white="blue",markers=["o","s"]))
#print(wine_set)
from sklearn.linear_model import LinearRegression
model =LinearRegression(fit_intercept=True)
model.get_params()
X = wine_set.drop(["type","quality"],axis=1)
y = wine_set.quality #퀄리티을 y에 넣는다 ->퀄리티에 어떤 것이 가장 많이 영향을 주냐 이니까!->퀄리티가 제일 중요함
from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test = train_test_split(X,y,random_state=1)
model = LinearRegression(fit_intercept = True )#,n_job=None, Normalize=False)
model.fit(X_train,y_train)
data=np.array([6.3,0.3,0.34,1.6,0.049,14,132,0.994,3.3,0.49,9.5])
print(model.predict(np.reshape(data,(1,11))))
y_pred = model.predict(X_test)
def rmse(y_real,y_pred):
    return np.sqrt(np.mean((y_real-y_pred)**2))
np.round(rmse(y_test,y_pred),2)
from sklearn.metrics import mean_squared_error
np.round(np.sqrt(mean_squared_error(y_test,y_pred)),2)

#규제가 있는 선형 모델의 적합
from sklearn.linear_model import Ridge
model = Ridge(alpha=0.05)#릿지 : 람다가 패널티를 얼마나 부과하는가
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
np.round(np.sqrt(mean_squared_error(y_test,y_pred)),3)
from sklearn.linear_model import Lasso
model = Lasso(alpha=0.05)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
np.round(np.sqrt(mean_squared_error(y_test,y_pred)),3)
# %%
=======
#%%
from os import sep
from matplotlib.colors import Normalize
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
redwine = pd.read_csv('c:/Users/701/kdigital/lecture/winequality-red.csv',sep=";",header=0)#파일이 안 나눠져있으니,sep으로 나눠줌. header = 0 <-제목이 0번째 있으면 이렇게 씀
redwine['type']='red'
#print(redwine)
whitewine = pd.read_csv('c:/Users/701/kdigital/lecture/winequality-white.csv',sep=";",header=0)
whitewine['type']='white'
wine_set = redwine.append(whitewine) #데이터 프레임 합치기
#print(wine_set.shape)
#print(wine_set["type"].value_counts())#몇 개씩 구성되어 있는 지 파악
#print(wine_set.type.value_counts())#몇 개씩 구성되어 있는 지 파악

wine_set.columns#컬룸이 무엇이 있는 지 확인
wine_setcolumns2 =[]
###컬룸 명 바꾸기
#new_col=["a","b","c","d","e"]
#wine_set.columns=new_col
for i in wine_set.columns:
    a= i.replace(" ","_")
    wine_setcolumns2.append(a)
wine_set.columns = wine_setcolumns2
#한 라인으로 바꾸기 wine.columns = wine.columns.str.replace(" ","_")
#print(wine_set.columns)
wine_set.describe()#요약 통계량 보여주기
wine_set.quality.describe()#퀄리티라는 컬럼만 요약하기
wine_set.quality.unique()#퀄리티 안의 특정값 추출
wine_set.quality.value_counts()

wine_set.groupby('type')["quality"].describe()#그룹으로 해서 요약 통계
wine_set.groupby('type')["quality"].quantile([0,0.25,0.5,0.75,1]).unstack("type")#5개로 분류 & 데이터 프레임으로 변환
red_q = wine_set.loc[wine_set["type"]=="red","quality"]
white_q = wine_set.loc[wine_set["type"]=="white","quality"]
#print(red_q)
#print(white_q)
# sns.set_style()
# sns.distplot(red_q,norm_hist = True,kde = False,color="red",label="Red Wine")
# sns.distplot(white_q,norm_hist = True,kde = False,color="blue",label="White Wine")
# plt.title("Distribution of Quality of Wine Type")
# plt.xlabel("Quality Score")
# plt.ylabel("Density")#norm_hist=True - 밀도 norm_hist=False - 개수
# plt.legend()
wine_set.groupby("type")['quality'].aggregate(["std","mean"])
import statsmodels.api as sm
t_stat,p_value, df = sm.stats.ttest_ind(red_q,white_q)
"t-stat: {:.3f},p-value:{:.4f}".format(t_stat,p_value)

wine_corr = wine_set.corr()
plus_cor=wine_corr.loc[wine_corr["quality"] > 0,"quality"]
minus_cor=wine_corr.loc[wine_corr["quality"] < 0,"quality"]
#print(plus_cor)
#print(minus_cor)
red_sample = wine_set.loc[wine_set["type"]=="red",:]
white_sample = wine_set.loc[wine_set["type"]=="white",:]
red_idx = np.random.choice(red_sample.index,replace=True,size=200)
white_idx = np.random.choice(white_sample.index,replace=True,size=200)
wine_sample = red_sample.loc[red_idx,].append(white_sample.loc[white_idx,])
wine_sample.head()
sns.set_style("dark")
sns.pairplot(wine_sample,vars=["quality","alcohol","residual_sugar"],kind="reg",plot_kws={"ci":False,"x_jitter":0.25,"y_jitter":0.25},diag_kind="hist",diag_kws={"bins":10,"alpha":1},hue="type",palette=dict(red="red",white="blue",markers=["o","s"]))
#print(wine_set)
from sklearn.linear_model import LinearRegression
model =LinearRegression(fit_intercept=True)
model.get_params()
X = wine_set.drop(["type","quality"],axis=1)
y = wine_set.quality #퀄리티을 y에 넣는다 ->퀄리티에 어떤 것이 가장 많이 영향을 주냐 이니까!->퀄리티가 제일 중요함
from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test = train_test_split(X,y,random_state=1)
model = LinearRegression(fit_intercept = True )#,n_job=None, Normalize=False)
model.fit(X_train,y_train)
data=np.array([6.3,0.3,0.34,1.6,0.049,14,132,0.994,3.3,0.49,9.5])
print(model.predict(np.reshape(data,(1,11))))
y_pred = model.predict(X_test)
def rmse(y_real,y_pred):
    return np.sqrt(np.mean((y_real-y_pred)**2))
np.round(rmse(y_test,y_pred),2)
from sklearn.metrics import mean_squared_error
np.round(np.sqrt(mean_squared_error(y_test,y_pred)),2)

#규제가 있는 선형 모델의 적합
from sklearn.linear_model import Ridge
model = Ridge(alpha=0.05)#릿지 : 람다가 패널티를 얼마나 부과하는가
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
np.round(np.sqrt(mean_squared_error(y_test,y_pred)),3)
from sklearn.linear_model import Lasso
model = Lasso(alpha=0.05)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
np.round(np.sqrt(mean_squared_error(y_test,y_pred)),3)
# %%
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62

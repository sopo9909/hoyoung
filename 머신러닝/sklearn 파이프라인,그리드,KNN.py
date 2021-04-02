<<<<<<< HEAD
#%%
import re
from numpy.core.fromnumeric import reshape
from numpy.lib.function_base import append
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
clf = RandomForestClassifier(random_state=0)#0일때는 발생시키는 난수가 일정함
x=[[80,95,80],[67,88,75],[75,64,55],[100,46,65]]#이러한 점수가 있다
y=[1,1,0,0]#1일 때, 합격 , 0일 때, 불합격
clf.fit(x,y)#학습시킨다
print(clf.predict([[76,75,68]]))#이 값일 때, 합격 불합격
print(clf.predict([[86,75,88]]))

import seaborn as sns
from sklearn.datasets import load_iris
iris = sns.load_dataset("iris")
iris.info()
X = iris.drop("species",axis=1) ;X.head()# ; : 2개의 문장을 1개의 문장으로 나눠줌
X2=iris[["sepal_length","sepal_width","petal_length","petal_width","species"]]
iris=load_iris()
#iris["species"] = iris.species
print(type(iris))
print(iris.keys())
print(iris.feature_names)
print(iris.data[:5])
print(type(iris.data[:5]))
print(iris.target_names)

import numpy as np
import matplotlib.pyplot as plt
# rs = np.random.RandomState(10)
# X = 10*rs.rand(100)
# Y = 3*x +2*rs.rand(100)
# plt.scatter(x,y,s=10)
# from sklearn.linear_model import LinearRegression
# regr = LinearRegression(fit_intercept =True)
# X = x.reshape(-1,1)
# regr.fit(X,y)

# x_new = np.linspace(-1,11,num=100)
# x_new = x_new.reshape(-1,1)
# y_pred = regr.predict(x_new)
# plt.plot(x_new,y_pred,c="red")
# plt.scatter(x,y,s=10)

iris = load_iris()
X=iris.data
Y=iris.target
from sklearn.neighbors import KNeighborsClassifier
knn =KNeighborsClassifier(n_neighbors=1)
knn.fit(X,Y)

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X_train,X_test,Y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=50)
y_pred = knn.predict(X_test)
np.mean(y_test ==y_pred) #test 데이터와 모두 다 한 값을 비교 train으로 학습 시킨 것을 test로 실험해보고 결과를 내봄 

train_accuracy = []
test_accuracy2 = []
plus_all=[]
neighbors = range(1,20)
for n in neighbors:
    knn = KNeighborsClassifier(n_neighbors =n)
    knn.fit(X_train,Y_train)
    print("n= ",str(n) ," train = ",knn.score(X_train, Y_train), " test = ",knn.score(X_test,y_test))
    train_accuracy.append(knn.score(X_train, Y_train))
    test_accuracy2.append(knn.score(X_test,y_test))
    #test_accuracy.append(knn.score(X_test, y_test))
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.plot(neighbors,train_accuracy,label="train accuracy")
plt.plot(neighbors,test_accuracy2,label="test accuracy")
plt.xlabel("n_neighbors")
plt.ylabel("accuracy")
plt.legend()

# %%
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

def PolynomialRegression(degree=2,**kwargs):
    return make_pipeline(PolynomialFeatures(degree),LinearRegression(**kwargs))

import numpy as np
def make_data(N,err=1.0,seed=1):
    np.random.seed(seed)
    X=np.random.rand(N,1)**2
    y = 10-1./(X.ravel()+0.1)
    if err > 0:
        y+=err * np.random.randn(N)
    return X,y
X,y = make_data(40)
plt.style.use("seaborn-whitegrid")
X_test =np.linspace(-0.1,1.1,500).reshape(-1,1)
fig = plt.figure(figsize=(12,10))
for i,degree in enumerate([1,3,5,10],start=1):
    ax =fig.add_subplot(2,2,i)
    ax.scatter(X.ravel(),y,s=15)
    y_test = make_pipeline(PolynomialFeatures(degree),LinearRegression()).fit(X,y).predict(X_test)
    ax.plot(X_test.ravel(),y_test,label ='degree={0}'.format(degree))
    ax.set_xlim(-0.1,1.0)
    ax.set_ylim(-2,12)
    ax.legend(loc='best')

from sklearn.model_selection import GridSearchCV
param_grid = {"PolynomialFeatures__degree" : np.arange(21),
"LinearRegression__fit_intercept" : [True,False],
"LinearRegression__normalize" : [True,False]}
grid = GridSearchCV(PolynomialRegression(),param_grid,cv=7)
grid.fit(X,y)
grid.best_params_
# %%
=======
#%%
import re
from numpy.core.fromnumeric import reshape
from numpy.lib.function_base import append
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
clf = RandomForestClassifier(random_state=0)#0일때는 발생시키는 난수가 일정함
x=[[80,95,80],[67,88,75],[75,64,55],[100,46,65]]#이러한 점수가 있다
y=[1,1,0,0]#1일 때, 합격 , 0일 때, 불합격
clf.fit(x,y)#학습시킨다
print(clf.predict([[76,75,68]]))#이 값일 때, 합격 불합격
print(clf.predict([[86,75,88]]))

import seaborn as sns
from sklearn.datasets import load_iris
iris = sns.load_dataset("iris")
iris.info()
X = iris.drop("species",axis=1) ;X.head()# ; : 2개의 문장을 1개의 문장으로 나눠줌
X2=iris[["sepal_length","sepal_width","petal_length","petal_width","species"]]
iris=load_iris()
#iris["species"] = iris.species
print(type(iris))
print(iris.keys())
print(iris.feature_names)
print(iris.data[:5])
print(type(iris.data[:5]))
print(iris.target_names)

import numpy as np
import matplotlib.pyplot as plt
# rs = np.random.RandomState(10)
# X = 10*rs.rand(100)
# Y = 3*x +2*rs.rand(100)
# plt.scatter(x,y,s=10)
# from sklearn.linear_model import LinearRegression
# regr = LinearRegression(fit_intercept =True)
# X = x.reshape(-1,1)
# regr.fit(X,y)

# x_new = np.linspace(-1,11,num=100)
# x_new = x_new.reshape(-1,1)
# y_pred = regr.predict(x_new)
# plt.plot(x_new,y_pred,c="red")
# plt.scatter(x,y,s=10)

iris = load_iris()
X=iris.data
Y=iris.target
from sklearn.neighbors import KNeighborsClassifier
knn =KNeighborsClassifier(n_neighbors=1)
knn.fit(X,Y)

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X_train,X_test,Y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=50)
y_pred = knn.predict(X_test)
np.mean(y_test ==y_pred) #test 데이터와 모두 다 한 값을 비교 train으로 학습 시킨 것을 test로 실험해보고 결과를 내봄 

train_accuracy = []
test_accuracy2 = []
plus_all=[]
neighbors = range(1,20)
for n in neighbors:
    knn = KNeighborsClassifier(n_neighbors =n)
    knn.fit(X_train,Y_train)
    print("n= ",str(n) ," train = ",knn.score(X_train, Y_train), " test = ",knn.score(X_test,y_test))
    train_accuracy.append(knn.score(X_train, Y_train))
    test_accuracy2.append(knn.score(X_test,y_test))
    #test_accuracy.append(knn.score(X_test, y_test))
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.plot(neighbors,train_accuracy,label="train accuracy")
plt.plot(neighbors,test_accuracy2,label="test accuracy")
plt.xlabel("n_neighbors")
plt.ylabel("accuracy")
plt.legend()

# %%
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

def PolynomialRegression(degree=2,**kwargs):
    return make_pipeline(PolynomialFeatures(degree),LinearRegression(**kwargs))

import numpy as np
def make_data(N,err=1.0,seed=1):
    np.random.seed(seed)
    X=np.random.rand(N,1)**2
    y = 10-1./(X.ravel()+0.1)
    if err > 0:
        y+=err * np.random.randn(N)
    return X,y
X,y = make_data(40)
plt.style.use("seaborn-whitegrid")
X_test =np.linspace(-0.1,1.1,500).reshape(-1,1)
fig = plt.figure(figsize=(12,10))
for i,degree in enumerate([1,3,5,10],start=1):
    ax =fig.add_subplot(2,2,i)
    ax.scatter(X.ravel(),y,s=15)
    y_test = make_pipeline(PolynomialFeatures(degree),LinearRegression()).fit(X,y).predict(X_test)
    ax.plot(X_test.ravel(),y_test,label ='degree={0}'.format(degree))
    ax.set_xlim(-0.1,1.0)
    ax.set_ylim(-2,12)
    ax.legend(loc='best')

from sklearn.model_selection import GridSearchCV
param_grid = {"PolynomialFeatures__degree" : np.arange(21),
"LinearRegression__fit_intercept" : [True,False],
"LinearRegression__normalize" : [True,False]}
grid = GridSearchCV(PolynomialRegression(),param_grid,cv=7)
grid.fit(X,y)
grid.best_params_
# %%
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62

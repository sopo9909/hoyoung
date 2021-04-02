<<<<<<< HEAD
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import numpy as np
data = pd.read_csv('price_data.csv',header=0,sep=',')
data = data.dropna(axis=0)
X = data.drop("year",axis=1)
X_corr = X.corr()
#print(X_corr)
X = X.drop("avgPrice",axis=1)
#print(X)
y = data["avgPrice"]
#print(y)
model = LinearRegression(fit_intercept=True)
model2=Lasso()
param_grid={'alpha':[0.5,1,1.5]}
grid_search = GridSearchCV(model2,param_grid=param_grid)
grid_search.fit(X,y)
model.fit(X,y)
best_model = grid_search.best_estimator_
a=input("평균온도는?")
b=input("최저온도는?")
c=input("최고온도는?")
d=input("강수량은?")
newdata = np.array([float(a),float(b),float(c),float(d)])
print("배추값의 예상은??!")
print(model.predict(np.reshape(newdata,(1,4))))
print(best_model.predict(np.reshape(newdata,(1,4))))
#y_pred = model.predict(X_test)
=======
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import numpy as np
data = pd.read_csv('price_data.csv',header=0,sep=',')
data = data.dropna(axis=0)
X = data.drop("year",axis=1)
X_corr = X.corr()
#print(X_corr)
X = X.drop("avgPrice",axis=1)
#print(X)
y = data["avgPrice"]
#print(y)
model = LinearRegression(fit_intercept=True)
model2=Lasso()
param_grid={'alpha':[0.5,1,1.5]}
grid_search = GridSearchCV(model2,param_grid=param_grid)
grid_search.fit(X,y)
model.fit(X,y)
best_model = grid_search.best_estimator_
a=input("평균온도는?")
b=input("최저온도는?")
c=input("최고온도는?")
d=input("강수량은?")
newdata = np.array([float(a),float(b),float(c),float(d)])
print("배추값의 예상은??!")
print(model.predict(np.reshape(newdata,(1,4))))
print(best_model.predict(np.reshape(newdata,(1,4))))
#y_pred = model.predict(X_test)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62

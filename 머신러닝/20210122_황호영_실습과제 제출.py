<<<<<<< HEAD
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model
import os
import pandas as pd
import numpy as np
from tensorflow.keras import datasets,layers ,models
from tensorflow.python.keras.layers.core import Dense
from tensorflow.python.keras.engine.sequential import Sequential
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
# data = pd.read_csv('input3_out1 .csv',sep=',')
# from sklearn.linear_model import LinearRegression
# model =LinearRegression(fit_intercept=True)
# model.get_params()
# X = wine_set.drop(["type","quality"],axis=1)
# y = wine_set.quality #퀄리티을 y에 넣는다 ->퀄리티에 어떤 것이 가장 많이 영향을 주냐 이니까!->퀄리티가 제일 중요함
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train,y_test = train_test_split(X,y,random_state=1)
# model = LinearRegression(fit_intercept = True )#,n_job=None, Normalize=False)
# model.fit(X_train,y_train)
# input
# data=np.array([])
# print(model.predict(np.reshape(data,(1,11))))
# y_pred = model.predict(X_test)

data1 = pd.read_csv('input3_out1 .csv',sep=',')
dataset = np.loadtxt("input3_out1 .csv",delimiter=",")
X = dataset[:,0:8]
Y = dataset[:,8]
model = Sequential()
model.add(layers.Dense(12,activation='relu'))
model.add(layers.Dense(15,activation='relu'))
model.add(layers.Dense(8,activation='relu'))
model.add(layers.Dense(10,activation='relu'))
model.add(layers.Dense(1, activation='softmax'))
model.compile(optimizer='adam',loss ='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(X,Y,epochs=5)
=======
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model
import os
import pandas as pd
import numpy as np
from tensorflow.keras import datasets,layers ,models
from tensorflow.python.keras.layers.core import Dense
from tensorflow.python.keras.engine.sequential import Sequential
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
# data = pd.read_csv('input3_out1 .csv',sep=',')
# from sklearn.linear_model import LinearRegression
# model =LinearRegression(fit_intercept=True)
# model.get_params()
# X = wine_set.drop(["type","quality"],axis=1)
# y = wine_set.quality #퀄리티을 y에 넣는다 ->퀄리티에 어떤 것이 가장 많이 영향을 주냐 이니까!->퀄리티가 제일 중요함
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train,y_test = train_test_split(X,y,random_state=1)
# model = LinearRegression(fit_intercept = True )#,n_job=None, Normalize=False)
# model.fit(X_train,y_train)
# input
# data=np.array([])
# print(model.predict(np.reshape(data,(1,11))))
# y_pred = model.predict(X_test)

data1 = pd.read_csv('input3_out1 .csv',sep=',')
dataset = np.loadtxt("input3_out1 .csv",delimiter=",")
X = dataset[:,0:8]
Y = dataset[:,8]
model = Sequential()
model.add(layers.Dense(12,activation='relu'))
model.add(layers.Dense(15,activation='relu'))
model.add(layers.Dense(8,activation='relu'))
model.add(layers.Dense(10,activation='relu'))
model.add(layers.Dense(1, activation='softmax'))
model.compile(optimizer='adam',loss ='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(X,Y,epochs=5)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62

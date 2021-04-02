<<<<<<< HEAD
from numpy.core.fromnumeric import reshape
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0)#0일때는 발생시키는 난수가 일정함
x=[[1,2,3],[11,12,13],[234,23,456]]
y=[0,1,2]#1,2,3일 때는 0 ,11,12,13일때는 1을 뽑아냄
clf.fit(x,y)#학습시킨다
print(clf.predict(x))#만약에 값이 없으면 0으로 나옴
print(clf.predict([[234,23,456]]))#이 값이 어디에 있을까?!-그것을 y에서 찾는거지

import numpy as np
rs = np.random.RandomState(10)
x=10 *rs.rand(5)
print(x)
y=2*x -1*rs.rand(5)
print(y)
print(x.shape, y.shape)
x=x.reshape(-1,1)# 니가 맞게 찾아주세요,원하는 차원수
print(x.shape)
=======
from numpy.core.fromnumeric import reshape
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0)#0일때는 발생시키는 난수가 일정함
x=[[1,2,3],[11,12,13],[234,23,456]]
y=[0,1,2]#1,2,3일 때는 0 ,11,12,13일때는 1을 뽑아냄
clf.fit(x,y)#학습시킨다
print(clf.predict(x))#만약에 값이 없으면 0으로 나옴
print(clf.predict([[234,23,456]]))#이 값이 어디에 있을까?!-그것을 y에서 찾는거지

import numpy as np
rs = np.random.RandomState(10)
x=10 *rs.rand(5)
print(x)
y=2*x -1*rs.rand(5)
print(y)
print(x.shape, y.shape)
x=x.reshape(-1,1)# 니가 맞게 찾아주세요,원하는 차원수
print(x.shape)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
print(reshape(-3,1))
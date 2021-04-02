<<<<<<< HEAD
from inspect import Parameter
from numpy.lib.function_base import vectorize
import pandas as pd
from pandas.core.arrays import sparse
from scipy.sparse.construct import random
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score,roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression #Logistic(Regression)Classifier
from sklearn.svm import SVC #Support Vector Machine
from sklearn.naive_bayes import GaussianNB #Naive Bayesian
from sklearn.neighbors import KNeighborsClassifier #K Nearest Neighbor
from sklearn.ensemble import RandomForestClassifier #Random Forest
from sklearn.ensemble import GradientBoostingClassifier #Gradient Boosing
from sklearn.neural_network import MLPClassifier #Neural Network
from sklearn import model_selection
from sklearn.tree import export_graphviz
from IPython.core.display import Image
import numpy as np
from sklearn.preprocessing import StandardScaler
import pydotplus
train_df = pd.read_csv("C:/Users/701/kdigital/lecture/train.csv",nrows=2000)#1만까지 만
train_df = train_df.drop(["id","hour","device_id","device_ip"],axis=1)
label_column="click"
X_dict_train = list(train_df.drop(label_column,axis=1).T.to_dict().values())#19개 컬럼이 ->4569개로 만들어짐
y_train = train_df[label_column] #결과로 산출하고 싶은 click수를 y로 
test_df=pd.read_csv("C:/Users/701/kdigital/lecture/train.csv",header=0,skiprows=(1,2000),nrows=2000)
test_df = test_df.drop(["id","hour","device_id","device_ip"],axis=1)
X_dict_test =list(test_df.drop(label_column,axis=1).T.to_dict().values()) # .T 하면 행과 열이 바뀜 #딕셔너리로 변경함 #values해서 하나하나
y_test = test_df[label_column]
vectorizer = DictVectorizer(sparse=True)#벡터로 변환->이진->희소(압축해서 데이터를 가지고 있음)
X_train = vectorizer.fit_transform(X_dict_train)
X_test = vectorizer.fit_transform(X_dict_test)

models = []
models.append(("LR", LogisticRegression()))
models.append(("DT", DecisionTreeClassifier()))
models.append(("SVM", SVC()))
models.append(("NB", GaussianNB()))
models.append(("KNN", KNeighborsClassifier()))
models.append(("RF", RandomForestClassifier()))
models.append(("GB", GradientBoostingClassifier()))
models.append(("ANN", MLPClassifier()))

Parameters ={"max_depth":[3,10,None]}
decision_tree = DecisionTreeClassifier(criterion="gini",min_samples_split=30)
grid_search = GridSearchCV(decision_tree,Parameters,n_jobs=-1,cv=3,scoring="roc_auc")
grid_search.fit(X_train,y_train) # 그리드로 최적화하기
grid_search.best_params_ #max_depth 구하기 <-
tree = DecisionTreeClassifier(max_depth =10)
tree.fit(X_train,y_train)

#1은 의사결정 모델
decision_tree_best=grid_search.best_estimator_
y_pred1 = decision_tree_best.predict(X_test)
np.unique(y_pred1,return_counts=True)
accuracy_score(y_test,y_pred1)
confusion_matrix(y_test,y_pred1)
y_pred_proba1 = decision_tree_best.predict_proba(X_test)[:,1] #클릭을 할 확률과 클릭을 안 할 확률 중 클릭을 할 확률만 추출
fpr1,tpr1,_ =roc_curve(y_test,y_pred_proba1)
auc1 = roc_auc_score(y_test,y_pred_proba1)
#2는 KNN
knn =KNeighborsClassifier(n_neighbor =3)
knn.fit(X_train,y_train)
y_pred2 = knn.predict(X_test)

plt.plot(fpr1,tpr1,"r-",label="DecisionTreeClassifier")
plt.plot([0,1],[0,1],"b--",label="random guess")
plt.xlabel("false positive rate")
plt.ylabel("true positive rate")
plt.title("AUC={0:.2f}".format(auc1))
=======
from inspect import Parameter
from numpy.lib.function_base import vectorize
import pandas as pd
from pandas.core.arrays import sparse
from scipy.sparse.construct import random
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score,roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression #Logistic(Regression)Classifier
from sklearn.svm import SVC #Support Vector Machine
from sklearn.naive_bayes import GaussianNB #Naive Bayesian
from sklearn.neighbors import KNeighborsClassifier #K Nearest Neighbor
from sklearn.ensemble import RandomForestClassifier #Random Forest
from sklearn.ensemble import GradientBoostingClassifier #Gradient Boosing
from sklearn.neural_network import MLPClassifier #Neural Network
from sklearn import model_selection
from sklearn.tree import export_graphviz
from IPython.core.display import Image
import numpy as np
from sklearn.preprocessing import StandardScaler
import pydotplus
train_df = pd.read_csv("C:/Users/701/kdigital/lecture/train.csv",nrows=2000)#1만까지 만
train_df = train_df.drop(["id","hour","device_id","device_ip"],axis=1)
label_column="click"
X_dict_train = list(train_df.drop(label_column,axis=1).T.to_dict().values())#19개 컬럼이 ->4569개로 만들어짐
y_train = train_df[label_column] #결과로 산출하고 싶은 click수를 y로 
test_df=pd.read_csv("C:/Users/701/kdigital/lecture/train.csv",header=0,skiprows=(1,2000),nrows=2000)
test_df = test_df.drop(["id","hour","device_id","device_ip"],axis=1)
X_dict_test =list(test_df.drop(label_column,axis=1).T.to_dict().values()) # .T 하면 행과 열이 바뀜 #딕셔너리로 변경함 #values해서 하나하나
y_test = test_df[label_column]
vectorizer = DictVectorizer(sparse=True)#벡터로 변환->이진->희소(압축해서 데이터를 가지고 있음)
X_train = vectorizer.fit_transform(X_dict_train)
X_test = vectorizer.fit_transform(X_dict_test)

models = []
models.append(("LR", LogisticRegression()))
models.append(("DT", DecisionTreeClassifier()))
models.append(("SVM", SVC()))
models.append(("NB", GaussianNB()))
models.append(("KNN", KNeighborsClassifier()))
models.append(("RF", RandomForestClassifier()))
models.append(("GB", GradientBoostingClassifier()))
models.append(("ANN", MLPClassifier()))

Parameters ={"max_depth":[3,10,None]}
decision_tree = DecisionTreeClassifier(criterion="gini",min_samples_split=30)
grid_search = GridSearchCV(decision_tree,Parameters,n_jobs=-1,cv=3,scoring="roc_auc")
grid_search.fit(X_train,y_train) # 그리드로 최적화하기
grid_search.best_params_ #max_depth 구하기 <-
tree = DecisionTreeClassifier(max_depth =10)
tree.fit(X_train,y_train)

#1은 의사결정 모델
decision_tree_best=grid_search.best_estimator_
y_pred1 = decision_tree_best.predict(X_test)
np.unique(y_pred1,return_counts=True)
accuracy_score(y_test,y_pred1)
confusion_matrix(y_test,y_pred1)
y_pred_proba1 = decision_tree_best.predict_proba(X_test)[:,1] #클릭을 할 확률과 클릭을 안 할 확률 중 클릭을 할 확률만 추출
fpr1,tpr1,_ =roc_curve(y_test,y_pred_proba1)
auc1 = roc_auc_score(y_test,y_pred_proba1)
#2는 KNN
knn =KNeighborsClassifier(n_neighbor =3)
knn.fit(X_train,y_train)
y_pred2 = knn.predict(X_test)

plt.plot(fpr1,tpr1,"r-",label="DecisionTreeClassifier")
plt.plot([0,1],[0,1],"b--",label="random guess")
plt.xlabel("false positive rate")
plt.ylabel("true positive rate")
plt.title("AUC={0:.2f}".format(auc1))
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
plt.legend(loc="lower right")
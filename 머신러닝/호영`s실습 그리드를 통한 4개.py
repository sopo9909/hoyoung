<<<<<<< HEAD
#%%
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
from sklearn.utils.validation import check_random_state
train_df = pd.read_csv("C:/Users/701/kdigital/lecture/train.csv",nrows=2000)#1만까지 만
train_df = train_df.drop(["id","hour","device_id","device_ip"],axis=1)
label_column="click"
X_dict_train = list(train_df.drop(label_column,axis=1).T.to_dict().values())#19개 컬럼이 ->4569개로 만들어짐
y_train = train_df[label_column] #결과로 산출하고 싶은 click수를 y로 
test_df=pd.read_csv("C:/Users/701/kdigital/lecture/train.csv",header=0,skiprows=(1,2001),nrows=2000)
test_df = test_df.drop(["id","hour","device_id","device_ip"],axis=1)
X_dict_test =list(test_df.drop(label_column,axis=1).T.to_dict().values()) # .T 하면 행과 열이 바뀜 #딕셔너리로 변경함 #values해서 하나하나
y_test = test_df[label_column]
vectorizer = DictVectorizer(sparse=True)#벡터로 변환->이진->희소(압축해서 데이터를 가지고 있음)
X_train = vectorizer.fit_transform(X_dict_train)
X_test = vectorizer.fit_transform(X_dict_test)
Parameters ={"max_depth":[3,5,None]}
decision_tree = DecisionTreeClassifier(criterion="gini",min_samples_split=30)
grid_search = GridSearchCV(decision_tree,Parameters,n_jobs=-1,cv=3,scoring="roc_auc")
grid_search.fit(X_train,y_train) # 그리드로 최적화하기
grid_search.best_params_ #max_depth 구하기 <-
#1은 의사결정 모델
decision_tree_best=grid_search.best_estimator_
y_pred1 = decision_tree_best.predict(X_test)
np.unique(y_pred1,return_counts=True)
print(accuracy_score(y_test,y_pred1))
print(confusion_matrix(y_test,y_pred1))
y_pred_proba1 = decision_tree_best.predict_proba(X_test)[:,1] #클릭을 할 확률과 클릭을 안 할 확률 중 클릭을 할 확률만 추출
fpr1,tpr1,_ =roc_curve(y_test,y_pred_proba1)
auc1 = roc_auc_score(y_test,y_pred_proba1)
#2는 KNN
knn =KNeighborsClassifier()
param_gri =[{'n_neighbors':range(3,10)}]
gs=GridSearchCV(estimator =knn,param_grid=param_gri,scoring="roc_auc")
gs.fit(X_train,y_train)
knn_model = gs.best_estimator_
y_pred2 = knn_model.predict(X_test)
np.unique(y_pred2,return_counts=True)
print(accuracy_score(y_test,y_pred2))
print(confusion_matrix(y_test,y_pred2))
roc_auc_score(y_test,y_pred2)
y_pred_proba2 = knn_model.predict_proba(X_test)[:,1]
fpr2,tpr2,_ =roc_curve(y_test,y_pred_proba2)
auc2 = roc_auc_score(y_test,y_pred_proba2)
#3은 랜덤포레스트
rf = RandomForestClassifier(random_state=1)
param_grid = [{'n_estimators':range(1,5,1),'max_depth':[6,8,10,12],'min_samples_leaf':[8,12,18],'min_samples_split':[8,16,20]}]
gs2=GridSearchCV(estimator=rf,param_grid=param_grid,scoring="roc_auc",cv=5,n_jobs=-1)
gs2.fit(X_train,y_train)
model2=gs2.best_estimator_
y_pred3 = model2.predict(X_test)
np.unique(y_pred3,return_counts=True)
print(accuracy_score(y_test,y_pred3))
print(confusion_matrix(y_test,y_pred3))
roc_auc_score(y_test,y_pred3)
y_pred_proba3 = model2.predict_proba(X_test)[:,1]
fpr3,tpr3,_ =roc_curve(y_test,y_pred_proba3)
auc3 = roc_auc_score(y_test,y_pred_proba3)
#4는 로지스틱
clf=LogisticRegression()
param_grid2 = [{'C': np.linspace(0.1,10,100)}]
gs3 = GridSearchCV(estimator=clf,param_grid=param_grid2,scoring="roc_auc",cv=5,n_jobs=-1)
gs3.fit(X_train,y_train)
model3=gs3.best_estimator_
y_pred4 = model3.predict(X_test)
np.unique(y_pred4,return_counts=True)
print(accuracy_score(y_test,y_pred4))
print(confusion_matrix(y_test,y_pred4))
roc_auc_score(y_test,y_pred4)
y_pred_proba4 = model3.predict_proba(X_test)[:,1]
fpr4,tpr4,_ =roc_curve(y_test,y_pred_proba4)
auc4 = roc_auc_score(y_test,y_pred_proba4)
plt.plot(fpr1,tpr1,"r-",label="DecisionTreeClassifier")
plt.plot(fpr2,tpr2,"c-",label="KNN")
plt.plot(fpr3,tpr3,"y-",label="RandomForest")
plt.plot(fpr4,tpr4,"g-",label="Logistic")
plt.plot([0,1],[0,1],"b--",label="random guess")
plt.xlabel("false positive rate")
plt.ylabel("true positive rate")
plt.title("AUC_dt={0:.2f}/AUC_knn={1:.2f}/AUC_rf={2:.2f}/AUC_lg={3:.2f}".format(auc1,auc2,auc3,auc4))#,"AUC={0:.2f}".format(auc2),"AUC={0:.2f}".format(auc3),"AUC={0:.2f}".format(auc4))
plt.legend(loc="lower right")
# %%
=======
#%%
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
from sklearn.utils.validation import check_random_state
train_df = pd.read_csv("C:/Users/701/kdigital/lecture/train.csv",nrows=2000)#1만까지 만
train_df = train_df.drop(["id","hour","device_id","device_ip"],axis=1)
label_column="click"
X_dict_train = list(train_df.drop(label_column,axis=1).T.to_dict().values())#19개 컬럼이 ->4569개로 만들어짐
y_train = train_df[label_column] #결과로 산출하고 싶은 click수를 y로 
test_df=pd.read_csv("C:/Users/701/kdigital/lecture/train.csv",header=0,skiprows=(1,2001),nrows=2000)
test_df = test_df.drop(["id","hour","device_id","device_ip"],axis=1)
X_dict_test =list(test_df.drop(label_column,axis=1).T.to_dict().values()) # .T 하면 행과 열이 바뀜 #딕셔너리로 변경함 #values해서 하나하나
y_test = test_df[label_column]
vectorizer = DictVectorizer(sparse=True)#벡터로 변환->이진->희소(압축해서 데이터를 가지고 있음)
X_train = vectorizer.fit_transform(X_dict_train)
X_test = vectorizer.fit_transform(X_dict_test)
Parameters ={"max_depth":[3,5,None]}
decision_tree = DecisionTreeClassifier(criterion="gini",min_samples_split=30)
grid_search = GridSearchCV(decision_tree,Parameters,n_jobs=-1,cv=3,scoring="roc_auc")
grid_search.fit(X_train,y_train) # 그리드로 최적화하기
grid_search.best_params_ #max_depth 구하기 <-
#1은 의사결정 모델
decision_tree_best=grid_search.best_estimator_
y_pred1 = decision_tree_best.predict(X_test)
np.unique(y_pred1,return_counts=True)
print(accuracy_score(y_test,y_pred1))
print(confusion_matrix(y_test,y_pred1))
y_pred_proba1 = decision_tree_best.predict_proba(X_test)[:,1] #클릭을 할 확률과 클릭을 안 할 확률 중 클릭을 할 확률만 추출
fpr1,tpr1,_ =roc_curve(y_test,y_pred_proba1)
auc1 = roc_auc_score(y_test,y_pred_proba1)
#2는 KNN
knn =KNeighborsClassifier()
param_gri =[{'n_neighbors':range(3,10)}]
gs=GridSearchCV(estimator =knn,param_grid=param_gri,scoring="roc_auc")
gs.fit(X_train,y_train)
knn_model = gs.best_estimator_
y_pred2 = knn_model.predict(X_test)
np.unique(y_pred2,return_counts=True)
print(accuracy_score(y_test,y_pred2))
print(confusion_matrix(y_test,y_pred2))
roc_auc_score(y_test,y_pred2)
y_pred_proba2 = knn_model.predict_proba(X_test)[:,1]
fpr2,tpr2,_ =roc_curve(y_test,y_pred_proba2)
auc2 = roc_auc_score(y_test,y_pred_proba2)
#3은 랜덤포레스트
rf = RandomForestClassifier(random_state=1)
param_grid = [{'n_estimators':range(1,5,1),'max_depth':[6,8,10,12],'min_samples_leaf':[8,12,18],'min_samples_split':[8,16,20]}]
gs2=GridSearchCV(estimator=rf,param_grid=param_grid,scoring="roc_auc",cv=5,n_jobs=-1)
gs2.fit(X_train,y_train)
model2=gs2.best_estimator_
y_pred3 = model2.predict(X_test)
np.unique(y_pred3,return_counts=True)
print(accuracy_score(y_test,y_pred3))
print(confusion_matrix(y_test,y_pred3))
roc_auc_score(y_test,y_pred3)
y_pred_proba3 = model2.predict_proba(X_test)[:,1]
fpr3,tpr3,_ =roc_curve(y_test,y_pred_proba3)
auc3 = roc_auc_score(y_test,y_pred_proba3)
#4는 로지스틱
clf=LogisticRegression()
param_grid2 = [{'C': np.linspace(0.1,10,100)}]
gs3 = GridSearchCV(estimator=clf,param_grid=param_grid2,scoring="roc_auc",cv=5,n_jobs=-1)
gs3.fit(X_train,y_train)
model3=gs3.best_estimator_
y_pred4 = model3.predict(X_test)
np.unique(y_pred4,return_counts=True)
print(accuracy_score(y_test,y_pred4))
print(confusion_matrix(y_test,y_pred4))
roc_auc_score(y_test,y_pred4)
y_pred_proba4 = model3.predict_proba(X_test)[:,1]
fpr4,tpr4,_ =roc_curve(y_test,y_pred_proba4)
auc4 = roc_auc_score(y_test,y_pred_proba4)
plt.plot(fpr1,tpr1,"r-",label="DecisionTreeClassifier")
plt.plot(fpr2,tpr2,"c-",label="KNN")
plt.plot(fpr3,tpr3,"y-",label="RandomForest")
plt.plot(fpr4,tpr4,"g-",label="Logistic")
plt.plot([0,1],[0,1],"b--",label="random guess")
plt.xlabel("false positive rate")
plt.ylabel("true positive rate")
plt.title("AUC_dt={0:.2f}/AUC_knn={1:.2f}/AUC_rf={2:.2f}/AUC_lg={3:.2f}".format(auc1,auc2,auc3,auc4))#,"AUC={0:.2f}".format(auc2),"AUC={0:.2f}".format(auc3),"AUC={0:.2f}".format(auc4))
plt.legend(loc="lower right")
# %%
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62

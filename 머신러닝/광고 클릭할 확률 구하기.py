<<<<<<< HEAD
#%%
#의사결정트리
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
from sklearn.tree import export_graphviz
from IPython.core.display import Image
import numpy as np
import pydotplus
train_df = pd.read_csv("C:/Users/701/kdigital/lecture/train.csv",nrows=100000)#1만까지 만 불러오기
#필요없는 것 다 빼기
train_df = train_df.drop(["id","hour","device_id","device_ip"],axis=1)
#Y값은 결국 click
label_column="click"
#click이라는 것 버리고, 전치 행렬 -> 딕셔너리로 만들고 ->값들만 가져와서 ->리스트로 만듬
X_dict_train = list(train_df.drop(label_column,axis=1).T.to_dict().values())#19개 컬럼이 ->4569개로 만들어짐
#Y값을 타겟으로
y_train = train_df[label_column] #결과로 산출하고 싶은 click수를 y로 
#테스트도 정의 해주기
test_df=pd.read_csv("C:/Users/701/kdigital/lecture/train.csv",header=0,skiprows=(1,100000),nrows=100000)#1만부터 시작
test_df = test_df.drop(["id","hour","device_id","device_ip"],axis=1)
X_dict_test =list(test_df.drop(label_column,axis=1).T.to_dict().values()) # .T 하면 행과 열이 바뀜 #딕셔너리로 변경함 #values해서 하나하나
y_test = test_df[label_column]

####벡터화
vectorizer = DictVectorizer(sparse=True)#벡터로 변환->이진->희소(압축해서 데이터를 가지고 있음)
X_train = vectorizer.fit_transform(X_dict_train)#x트레인값을 변경해즘
X_test = vectorizer.fit_transform(X_dict_test)
#최종 깂이는 3~10
Parameters ={"max_depth":[3,10,None]}
decision_tree = DecisionTreeClassifier(criterion="gini",min_samples_split=30)
grid_search = GridSearchCV(decision_tree,Parameters,n_jobs=-1,cv=3,scoring="roc_auc")
grid_search.fit(X_train,y_train) # 그리드로 최적화하기
grid_search.best_params_ #max_depth 구하기 <-
tree = DecisionTreeClassifier(max_depth =10)
tree.fit(X_train,y_train)
dot_data=export_graphviz(tree,out_file=None,feature_names=vectorizer.feature_names_,class_names=["0","1"],rounded =True,filled =True,impurity=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.set_size('"5,5!"')
graph.write_png("train2.png")
Image("train2.png")

decision_tree_best=grid_search.best_estimator_
y_pred = decision_tree_best.predict(X_test)
np.unique(y_pred,return_counts=True)
accuracy_score(y_test,y_pred)
confusion_matrix(y_test,y_pred)
y_pred_proba = decision_tree_best.predict_proba(X_test)[:,1] #클릭을 할 확률과 클릭을 안 할 확률 중 클릭을 할 확률만 추출
fpr,tpr,_ =roc_curve(y_test,y_pred_proba)
auc = roc_auc_score(y_test,y_pred_proba)
plt.plot(fpr,tpr,"r-",label="DecisionTreeClassifier")
plt.plot([0,1],[0,1],"b--",label="random guess")
plt.xlabel("false positive rate")
plt.ylabel("true positive rate")
plt.title("AUC={0:.2f}".format(auc))
plt.legend(loc="lower right")
# %%
=======
#%%
#의사결정트리
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
from sklearn.tree import export_graphviz
from IPython.core.display import Image
import numpy as np
import pydotplus
train_df = pd.read_csv("C:/Users/701/kdigital/lecture/train.csv",nrows=100000)#1만까지 만 불러오기
#필요없는 것 다 빼기
train_df = train_df.drop(["id","hour","device_id","device_ip"],axis=1)
#Y값은 결국 click
label_column="click"
#click이라는 것 버리고, 전치 행렬 -> 딕셔너리로 만들고 ->값들만 가져와서 ->리스트로 만듬
X_dict_train = list(train_df.drop(label_column,axis=1).T.to_dict().values())#19개 컬럼이 ->4569개로 만들어짐
#Y값을 타겟으로
y_train = train_df[label_column] #결과로 산출하고 싶은 click수를 y로 
#테스트도 정의 해주기
test_df=pd.read_csv("C:/Users/701/kdigital/lecture/train.csv",header=0,skiprows=(1,100000),nrows=100000)#1만부터 시작
test_df = test_df.drop(["id","hour","device_id","device_ip"],axis=1)
X_dict_test =list(test_df.drop(label_column,axis=1).T.to_dict().values()) # .T 하면 행과 열이 바뀜 #딕셔너리로 변경함 #values해서 하나하나
y_test = test_df[label_column]

####벡터화
vectorizer = DictVectorizer(sparse=True)#벡터로 변환->이진->희소(압축해서 데이터를 가지고 있음)
X_train = vectorizer.fit_transform(X_dict_train)#x트레인값을 변경해즘
X_test = vectorizer.fit_transform(X_dict_test)
#최종 깂이는 3~10
Parameters ={"max_depth":[3,10,None]}
decision_tree = DecisionTreeClassifier(criterion="gini",min_samples_split=30)
grid_search = GridSearchCV(decision_tree,Parameters,n_jobs=-1,cv=3,scoring="roc_auc")
grid_search.fit(X_train,y_train) # 그리드로 최적화하기
grid_search.best_params_ #max_depth 구하기 <-
tree = DecisionTreeClassifier(max_depth =10)
tree.fit(X_train,y_train)
dot_data=export_graphviz(tree,out_file=None,feature_names=vectorizer.feature_names_,class_names=["0","1"],rounded =True,filled =True,impurity=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.set_size('"5,5!"')
graph.write_png("train2.png")
Image("train2.png")

decision_tree_best=grid_search.best_estimator_
y_pred = decision_tree_best.predict(X_test)
np.unique(y_pred,return_counts=True)
accuracy_score(y_test,y_pred)
confusion_matrix(y_test,y_pred)
y_pred_proba = decision_tree_best.predict_proba(X_test)[:,1] #클릭을 할 확률과 클릭을 안 할 확률 중 클릭을 할 확률만 추출
fpr,tpr,_ =roc_curve(y_test,y_pred_proba)
auc = roc_auc_score(y_test,y_pred_proba)
plt.plot(fpr,tpr,"r-",label="DecisionTreeClassifier")
plt.plot([0,1],[0,1],"b--",label="random guess")
plt.xlabel("false positive rate")
plt.ylabel("true positive rate")
plt.title("AUC={0:.2f}".format(auc))
plt.legend(loc="lower right")
# %%
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62

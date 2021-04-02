<<<<<<< HEAD
import pandas as pd
import numpy as np
url ='https://han.gl/zNMZu'
breast_cancer=pd.read_csv(url,header=None)
breast_cancer.columns =["id_number","clump_thickness","unif_cell_size","unif_cell_shape","marg_adhesion","single_epith_cell_size","bare_nuclei","bland_chromatin","normal_nucleoli","mitoses","class"]
breast_cancer.isnull().values.sum()
breast_cancer['bare_nuclei'] = breast_cancer['bare_nuclei'].replace('?',np.NAN)
breast_cancer['bare_nuclei'] =\
breast_cancer['bare_nuclei'].fillna(breast_cancer['bare_nuclei'].value_count().index[0])
breast_cancer['cancer_ind'] = 0
breast_cancer.loc[breast_cancer['class']==4,'cancer_ind']=1
#불필요한 변수 제거 및 표준화 적용
X = breast_cancer.drop(["id_number","class","cancer_ind"],axis=1)
y = breast_cancer.cancer_ind
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=0.3,random_state=42)
#데이터 표준화 작업
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
from sklearn.neighbors import KNeighborsClassifier
knn =KNeighborsClassifier(n_neighbor =3)
knn.fit(X_train_scaled,y_train)
from sklearn.metrics import accuracy_score,confusion_matrix,roc_auc_score
y_pred = knn.predict(X_test_scaled)
accuracy_score(y_test,y_pred)#양성을 양성이라 말하고 음성을 음성이라 말하는 확률
confusion_matrix(y_test,y_pred)
roc_auc_score(y_test,y_pred)
#그리드 서치를 이용한 하이퍼파라미터의 최적 값 선택
from sklearn.model_selection import GridSearchCV
grid_search = GridSearchCV(knn,{"n_neighbors":[1,2,3,4,5]},n_jobs =-1,cv=7,scoring="roc_auc")
grid_search.fit(X_train_scaled,y_train)
grid_search.best_params_
knn_bset =grid_search.best_estimator_
y_pred = knn_bset.predict(X_test_scaled)
accuracy_score(y_test,y_pred)
confusion_matrix(y_test,y_pred)
=======
import pandas as pd
import numpy as np
url ='https://han.gl/zNMZu'
breast_cancer=pd.read_csv(url,header=None)
breast_cancer.columns =["id_number","clump_thickness","unif_cell_size","unif_cell_shape","marg_adhesion","single_epith_cell_size","bare_nuclei","bland_chromatin","normal_nucleoli","mitoses","class"]
breast_cancer.isnull().values.sum()
breast_cancer['bare_nuclei'] = breast_cancer['bare_nuclei'].replace('?',np.NAN)
breast_cancer['bare_nuclei'] =\
breast_cancer['bare_nuclei'].fillna(breast_cancer['bare_nuclei'].value_count().index[0])
breast_cancer['cancer_ind'] = 0
breast_cancer.loc[breast_cancer['class']==4,'cancer_ind']=1
#불필요한 변수 제거 및 표준화 적용
X = breast_cancer.drop(["id_number","class","cancer_ind"],axis=1)
y = breast_cancer.cancer_ind
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=0.3,random_state=42)
#데이터 표준화 작업
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
from sklearn.neighbors import KNeighborsClassifier
knn =KNeighborsClassifier(n_neighbor =3)
knn.fit(X_train_scaled,y_train)
from sklearn.metrics import accuracy_score,confusion_matrix,roc_auc_score
y_pred = knn.predict(X_test_scaled)
accuracy_score(y_test,y_pred)#양성을 양성이라 말하고 음성을 음성이라 말하는 확률
confusion_matrix(y_test,y_pred)
roc_auc_score(y_test,y_pred)
#그리드 서치를 이용한 하이퍼파라미터의 최적 값 선택
from sklearn.model_selection import GridSearchCV
grid_search = GridSearchCV(knn,{"n_neighbors":[1,2,3,4,5]},n_jobs =-1,cv=7,scoring="roc_auc")
grid_search.fit(X_train_scaled,y_train)
grid_search.best_params_
knn_bset =grid_search.best_estimator_
y_pred = knn_bset.predict(X_test_scaled)
accuracy_score(y_test,y_pred)
confusion_matrix(y_test,y_pred)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
roc_auc_score(y_test,y_pred)
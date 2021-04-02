<<<<<<< HEAD
import json
from flask import Flask, request, make_response
from slacker import Slacker
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
import re
from numpy.core.fromnumeric import reshape
from numpy.lib.function_base import append
from sklearn.ensemble import RandomForestClassifier
from IPython.core.display import Image
from sklearn.model_selection import train_test_split
import datetime
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import TensorBoard
from numpy.lib.function_base import gradient
from IPython.core.display import Image
import numpy as np
from sklearn.preprocessing import StandardScaler
import pydotplus
from sklearn.utils.validation import check_random_state
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import numpy as np
from numpy.lib.function_base import gradient
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model
import os

from tensorflow.python.keras.preprocessing.sequence import pad_sequences
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

###데이터셋 다운로드 하기###
imdb = keras.datasets.imdb
#빈번하게 등장하는 만개를 가져옴
(train_data, train_labels) ,(test_data, test_labels) =imdb.load_data(num_words=10000)
print("훈련 샘플: {}, 레이블: {}".format(len(train_data), len(train_labels)))
#리뷰 텍스트는 어희 사전의 특정 단어를 나타내는 정수로 변환
#훈련 샘플은 리뷰에 나오는 단어를 나타냄
#레이블은 긍정은 1, 부정은 0
print(train_data[0])
#영화리뷰들의 길이가 다름 ->첫번째 리뷰와 두번째 리뷰의 단어 수 추출
print(len(train_data[0]), len(train_data[1]))
#첫번째, 두번째 리뷰의 긍정과 부정을 부여줌
print(train_labels[0], train_labels[1])

###정수를 단어로 다시 변환하기###
#단어와 정수 인덱스를 매핑한 딕셔너리 생성
#각 단어의 인덱스를 가져옴
word_index = imdb.get_word_index()
#단어 하나하나 다 함
#워드 인덱스를 읽어서 아이템으로 추출
# v+3을 하는 이유는 0,1,2,3에 새롭게 하려고 이 데이터가 원래 1부터 시작해서 3해도 됨
word_index = {k:(v+3)for k,v in word_index.items()}
word_index["<PAD>"] = 0 #집합
word_index["<START>"] = 1 #시작
word_index["<UNK>"] = 2  # unknown
word_index["<UNUSED>"] = 3#사용하지 않음
#인덱스와 단어의 순서 변경
#원래 단어 : 숫자 -> 숫자 : 단어
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
#텍스트(트레인 데이터)를 받으면 <-이거는 숫자야 =>이것을 문자로 보여주고 싶어
#인덱스를 주고 단어를 찾아와라
#그리고 그것을 join을 통해 문장으로 만들어줘라
def decode_review(text):
    return ' '.join([reverse_word_index.get(i,'?') for i in text])
#리뷰 데이터를 글자로 해서 문장으로 만들어서 보여줌
decode_review(train_data[0])


###데이터 준비
#데이터를 신경망에 주입하기 전에 텐서로 변환해야함
#원-핫인코딩 대신에 정수 배열의 길이가 모두 같도록 패딩을 추가해서
#max_length *num_reviews 크기의 ㅇ정수 텐서를 만듬
#이런 형태의 텐서를 다룰 수 있는 임베딩 층을 신경망의 첫번째 층으로 사용할 수 있음
#pad_sequences는 문장의 길이를 맞추는 함수임

train_data = keras.preprocessing.sequence.pad_sequences(train_data,value=word_index["<PAD>"],padding='post',maxlen=256)
test_data = keras.preprocessing.sequence.pad_sequences(test_data,value=word_index["<PAD>"],padding='post',maxlen=256)
#샘플 길이 확인
print(len(train_data[0]),len(train_data[1]))
#데이터를 
print(train_data[0])
#영화 리뷰 데이터셋에 적용된 어휘 사전의 크기(단어 1만개)
vocab_size = 10000
model = keras.Sequential()
#얼마나 많은 층을 사용할 것인가?
#각 층에 얼마나 많은 은닉 유닛을 사용할 것인가?!
#예측할 레이블을 0~1 고로 sigmoid를 사용한다

#embedding - 정수로 인코딩된 단어를 입력받고 각 단어 인덱스에 해당하는 임베딩 벡터를 찾음
#이 벡터는 모델이 훈련되면서 학습.
#이 벡터는 출력 배열에 새로운 차원으로 추가
#최종 차원은 batch,sequence, embedding임.
model.add(keras.layers.Embedding(vocab_size,16,input_shape=(None,)))
##중요##
#layers.GlobalAveragePooling1D()은 sequence차원에 대해 평균을 계산하여
#각 샘플에 대해 고정된 길이의 출력벡터를 반환
#길이가 다른 입력을 다루기 위해서 사용함
#GlobalAveragePooling1D 레이어는 고정된 크기(여기에선 16)의 출력 벡터를 리턴합니다. 
#입력으로 shape가 (25000, 256, 16)인 배열이 사용됩니다.
#두번째 차원(리뷰당 단어개수 256개) 방향으로 평균을 구하여 
#shape가 (25000, 16)인 배열을 생성합니다.  
#입력으로 사용되는 리뷰에 포함된 단어 개수가 변경되더라도 
#같은 크기의 벡터로 처리할 수 있게 됩니다
model.add(keras.layers.GlobalAveragePooling1D())
#16개의 은닉 유닛을 가진 완전 연결된 층을 거침
#뉴런이 16개인 함수에 입력 벡터를 통과
model.add(keras.layers.Dense(16,activation='relu'))
#하나의 출력을 만들어냄. sigmoid를 통해 신뢰도를 나타냄
model.add(keras.layers.Dense(1,activation='sigmoid'))

###손실 함수와 옵티마이저###
#모델이 훈련하기 위해 손실함수와 옵티마이저
#이진 분류 문제(긍정,부정)이므로 sigmoid함수를 사용하고
#손실함수로는 binary_crossentropy를 사용 ->이것은 확률 분포 간의 거리를 측정
#->정답인 타깃 분포와 예측 분포 사이의 거리 = binary_crossentropy

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

###검증 세트 만들기 ###
x_val = train_data[:10000]
#train 데이터를 겹치지 않게 하기 위해
partial_x_train = train_data[10000:]
#train 데이터를 겹치지 않게 하기 위해
y_val = train_labels[:10000]
partial_y_train = train_labels[10000:]
####모델 훈련####
#배치는 512개로 하여 만듬
#40번의 에포크 동안 훈련
#x_train과 y_train 텐서에 있는 모든 샘플에 대해 40번 반복
history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=40,
                    batch_size=512,
                    validation_data=(x_val, y_val),
                    verbose=1)
###verbose = 2는 2개 값을 반환한다는 의미
results = model.evaluate(test_data,  test_labels, verbose=2)
###histroy는 현재 딕셔너리 형태
history_dict = history.history
history_dict.keys()

acc = history_dict['accuracy']
val_acc = history_dict['val_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']
epochs = range(1, len(acc) + 1)
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()


####그림 초기화 plt.clf()
plt.clf()   # 그림을 초기화합니다
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

=======
import json
from flask import Flask, request, make_response
from slacker import Slacker
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
import re
from numpy.core.fromnumeric import reshape
from numpy.lib.function_base import append
from sklearn.ensemble import RandomForestClassifier
from IPython.core.display import Image
from sklearn.model_selection import train_test_split
import datetime
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import TensorBoard
from numpy.lib.function_base import gradient
from IPython.core.display import Image
import numpy as np
from sklearn.preprocessing import StandardScaler
import pydotplus
from sklearn.utils.validation import check_random_state
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import numpy as np
from numpy.lib.function_base import gradient
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model
import os

from tensorflow.python.keras.preprocessing.sequence import pad_sequences
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

###데이터셋 다운로드 하기###
imdb = keras.datasets.imdb
#빈번하게 등장하는 만개를 가져옴
(train_data, train_labels) ,(test_data, test_labels) =imdb.load_data(num_words=10000)
print("훈련 샘플: {}, 레이블: {}".format(len(train_data), len(train_labels)))
#리뷰 텍스트는 어희 사전의 특정 단어를 나타내는 정수로 변환
#훈련 샘플은 리뷰에 나오는 단어를 나타냄
#레이블은 긍정은 1, 부정은 0
print(train_data[0])
#영화리뷰들의 길이가 다름 ->첫번째 리뷰와 두번째 리뷰의 단어 수 추출
print(len(train_data[0]), len(train_data[1]))
#첫번째, 두번째 리뷰의 긍정과 부정을 부여줌
print(train_labels[0], train_labels[1])

###정수를 단어로 다시 변환하기###
#단어와 정수 인덱스를 매핑한 딕셔너리 생성
#각 단어의 인덱스를 가져옴
word_index = imdb.get_word_index()
#단어 하나하나 다 함
#워드 인덱스를 읽어서 아이템으로 추출
# v+3을 하는 이유는 0,1,2,3에 새롭게 하려고 이 데이터가 원래 1부터 시작해서 3해도 됨
word_index = {k:(v+3)for k,v in word_index.items()}
word_index["<PAD>"] = 0 #집합
word_index["<START>"] = 1 #시작
word_index["<UNK>"] = 2  # unknown
word_index["<UNUSED>"] = 3#사용하지 않음
#인덱스와 단어의 순서 변경
#원래 단어 : 숫자 -> 숫자 : 단어
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
#텍스트(트레인 데이터)를 받으면 <-이거는 숫자야 =>이것을 문자로 보여주고 싶어
#인덱스를 주고 단어를 찾아와라
#그리고 그것을 join을 통해 문장으로 만들어줘라
def decode_review(text):
    return ' '.join([reverse_word_index.get(i,'?') for i in text])
#리뷰 데이터를 글자로 해서 문장으로 만들어서 보여줌
decode_review(train_data[0])


###데이터 준비
#데이터를 신경망에 주입하기 전에 텐서로 변환해야함
#원-핫인코딩 대신에 정수 배열의 길이가 모두 같도록 패딩을 추가해서
#max_length *num_reviews 크기의 ㅇ정수 텐서를 만듬
#이런 형태의 텐서를 다룰 수 있는 임베딩 층을 신경망의 첫번째 층으로 사용할 수 있음
#pad_sequences는 문장의 길이를 맞추는 함수임

train_data = keras.preprocessing.sequence.pad_sequences(train_data,value=word_index["<PAD>"],padding='post',maxlen=256)
test_data = keras.preprocessing.sequence.pad_sequences(test_data,value=word_index["<PAD>"],padding='post',maxlen=256)
#샘플 길이 확인
print(len(train_data[0]),len(train_data[1]))
#데이터를 
print(train_data[0])
#영화 리뷰 데이터셋에 적용된 어휘 사전의 크기(단어 1만개)
vocab_size = 10000
model = keras.Sequential()
#얼마나 많은 층을 사용할 것인가?
#각 층에 얼마나 많은 은닉 유닛을 사용할 것인가?!
#예측할 레이블을 0~1 고로 sigmoid를 사용한다

#embedding - 정수로 인코딩된 단어를 입력받고 각 단어 인덱스에 해당하는 임베딩 벡터를 찾음
#이 벡터는 모델이 훈련되면서 학습.
#이 벡터는 출력 배열에 새로운 차원으로 추가
#최종 차원은 batch,sequence, embedding임.
model.add(keras.layers.Embedding(vocab_size,16,input_shape=(None,)))
##중요##
#layers.GlobalAveragePooling1D()은 sequence차원에 대해 평균을 계산하여
#각 샘플에 대해 고정된 길이의 출력벡터를 반환
#길이가 다른 입력을 다루기 위해서 사용함
#GlobalAveragePooling1D 레이어는 고정된 크기(여기에선 16)의 출력 벡터를 리턴합니다. 
#입력으로 shape가 (25000, 256, 16)인 배열이 사용됩니다.
#두번째 차원(리뷰당 단어개수 256개) 방향으로 평균을 구하여 
#shape가 (25000, 16)인 배열을 생성합니다.  
#입력으로 사용되는 리뷰에 포함된 단어 개수가 변경되더라도 
#같은 크기의 벡터로 처리할 수 있게 됩니다
model.add(keras.layers.GlobalAveragePooling1D())
#16개의 은닉 유닛을 가진 완전 연결된 층을 거침
#뉴런이 16개인 함수에 입력 벡터를 통과
model.add(keras.layers.Dense(16,activation='relu'))
#하나의 출력을 만들어냄. sigmoid를 통해 신뢰도를 나타냄
model.add(keras.layers.Dense(1,activation='sigmoid'))

###손실 함수와 옵티마이저###
#모델이 훈련하기 위해 손실함수와 옵티마이저
#이진 분류 문제(긍정,부정)이므로 sigmoid함수를 사용하고
#손실함수로는 binary_crossentropy를 사용 ->이것은 확률 분포 간의 거리를 측정
#->정답인 타깃 분포와 예측 분포 사이의 거리 = binary_crossentropy

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

###검증 세트 만들기 ###
x_val = train_data[:10000]
#train 데이터를 겹치지 않게 하기 위해
partial_x_train = train_data[10000:]
#train 데이터를 겹치지 않게 하기 위해
y_val = train_labels[:10000]
partial_y_train = train_labels[10000:]
####모델 훈련####
#배치는 512개로 하여 만듬
#40번의 에포크 동안 훈련
#x_train과 y_train 텐서에 있는 모든 샘플에 대해 40번 반복
history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=40,
                    batch_size=512,
                    validation_data=(x_val, y_val),
                    verbose=1)
###verbose = 2는 2개 값을 반환한다는 의미
results = model.evaluate(test_data,  test_labels, verbose=2)
###histroy는 현재 딕셔너리 형태
history_dict = history.history
history_dict.keys()

acc = history_dict['accuracy']
val_acc = history_dict['val_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']
epochs = range(1, len(acc) + 1)
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()


####그림 초기화 plt.clf()
plt.clf()   # 그림을 초기화합니다
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
plt.show()
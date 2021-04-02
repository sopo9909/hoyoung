<<<<<<< HEAD

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import numpy as np
mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test) =mnist.load_data()
x_train,x_test = x_train/255.0,x_test/255.0
#층을 쌓아서 모델을 구성 ->falatten:28*28을 784개의 1차원의 array로 만듬->128로 나누고 ->20%를 버리고
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)),tf.keras.layers.Dense(128,activation='relu'),tf.keras.layers.Dropout(0.2),tf.keras.layers.Dense(64,activation='relu'),tf.keras.layers.Dense(32,activation='relu'),tf.keras.layers.Dense(10,activation='softmax')])
model.compile(optimizer='SGD',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
#모델 훈련
model.fit(x_train,y_train,epochs=5)
#모델 평가
a=model.evaluate(x_test,y_test,verbose=2)
print(a)
import matplotlib.pyplot as plt
def draw(no):
    plt.figure()
    plt.imshow(x_train[no])
    plt.colorbar
    plt.grid(False)
    print("label은 = ",y_train[no])
draw(4)
#테스트 데이터 예측
predictions = model.predict(x_test)
print(predictions[0])
a=np.argmax(predictions[0])
print(a)
print(y_test[0])

=======

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import numpy as np
mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test) =mnist.load_data()
x_train,x_test = x_train/255.0,x_test/255.0
#층을 쌓아서 모델을 구성 ->falatten:28*28을 784개의 1차원의 array로 만듬->128로 나누고 ->20%를 버리고
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)),tf.keras.layers.Dense(128,activation='relu'),tf.keras.layers.Dropout(0.2),tf.keras.layers.Dense(64,activation='relu'),tf.keras.layers.Dense(32,activation='relu'),tf.keras.layers.Dense(10,activation='softmax')])
model.compile(optimizer='SGD',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
#모델 훈련
model.fit(x_train,y_train,epochs=5)
#모델 평가
a=model.evaluate(x_test,y_test,verbose=2)
print(a)
import matplotlib.pyplot as plt
def draw(no):
    plt.figure()
    plt.imshow(x_train[no])
    plt.colorbar
    plt.grid(False)
    print("label은 = ",y_train[no])
draw(4)
#테스트 데이터 예측
predictions = model.predict(x_test)
print(predictions[0])
a=np.argmax(predictions[0])
print(a)
print(y_test[0])

>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62

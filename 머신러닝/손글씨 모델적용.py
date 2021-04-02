<<<<<<< HEAD
import os
import tensorflow as tf
from tensorflow.keras import datasets,layers ,models
from tensorflow.python.keras.backend import conv2d
from tensorflow.python.keras.layers.core import Dense
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

(train_images, train_labels) , (test_images , test_labels) = datasets.mnist.load_data()
#훈련 이미지 6만개
train_images = train_images.reshape((60000,28,28,1))# 6만개, 28 = 세로, 28 = 가로, 1 = 흑백
#테스트 이미지 만개
test_images = test_images.reshape((10000,28,28,1))
#픽셀을 0~1사이로 만든다(정규화)
train_images, test_images = train_images/255.0,test_images/255.0
model = models.Sequential()
#32개의 필터를 적용하겠다.
model.add(layers.Conv2D(32,(3,3),activation ='relu',input_shape=(28,28,1)))
#CNN은 배치 크기를 제외하고 
#(이미지 높이, 이미지 너비, 컬러 채널) 크기의 텐서(tensor)를 입력으로 받음
model.add(layers.MaxPooling2D((2,2)))
#Conv2D는 CNN의 레이어
model.add(layers.Conv2D(64,(3,3),activation='relu'))
#2D공간 데이터에 대한 최대 풀링 작업
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64,(3,3),activation='relu'))
#이 윗부분은 높이,너비,채널 크기의 3D텐서.
#높이와 너비 차원은 네트워크가 깊어질수록 감소함
#Conv2D층에서 출력 채널의 수는 첫번째 매개변수에 의해 결정됨
#일반적으로 높이와 너비가 줄어듦에 따라 Conv2D층의 출력채널을 늘릴 수 있음

model.add(layers.Flatten())
model.add(layers.Dense(64,activation='relu'))
model.add(layers.Dense(10,activation='softmax'))
model.compile(optimizer='adam',loss ='sparse_categorical_crossentropy',metrics=['accuracy'])
#모델을 완성하려면, 마지막 합성곱 층의 출력 텐서를 하나 이상의 Dense층에 주입하여 분류를 수행함.
#Dense층은 벡터(1D)를 입력으로 받는데, 출력은 3D임
#고로 3D출력을 1D로 펼치겠담.
#그다음 하나 이상의 Dense층을 그위에 추가하겠음
#Mnist 데이터는 10갸의 클래스가 있으므로 마지막의 Dense층에 10개의 출력과 소프트맥스활성화 함수를 사용함.

model.fit(train_images,train_labels,epochs=5)

test_loss,test_acc = model.evaluate(test_images,test_labels,verbose=2)
print(test_acc)
=======
import os
import tensorflow as tf
from tensorflow.keras import datasets,layers ,models
from tensorflow.python.keras.backend import conv2d
from tensorflow.python.keras.layers.core import Dense
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

(train_images, train_labels) , (test_images , test_labels) = datasets.mnist.load_data()
#훈련 이미지 6만개
train_images = train_images.reshape((60000,28,28,1))# 6만개, 28 = 세로, 28 = 가로, 1 = 흑백
#테스트 이미지 만개
test_images = test_images.reshape((10000,28,28,1))
#픽셀을 0~1사이로 만든다(정규화)
train_images, test_images = train_images/255.0,test_images/255.0
model = models.Sequential()
#32개의 필터를 적용하겠다.
model.add(layers.Conv2D(32,(3,3),activation ='relu',input_shape=(28,28,1)))
#CNN은 배치 크기를 제외하고 
#(이미지 높이, 이미지 너비, 컬러 채널) 크기의 텐서(tensor)를 입력으로 받음
model.add(layers.MaxPooling2D((2,2)))
#Conv2D는 CNN의 레이어
model.add(layers.Conv2D(64,(3,3),activation='relu'))
#2D공간 데이터에 대한 최대 풀링 작업
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64,(3,3),activation='relu'))
#이 윗부분은 높이,너비,채널 크기의 3D텐서.
#높이와 너비 차원은 네트워크가 깊어질수록 감소함
#Conv2D층에서 출력 채널의 수는 첫번째 매개변수에 의해 결정됨
#일반적으로 높이와 너비가 줄어듦에 따라 Conv2D층의 출력채널을 늘릴 수 있음

model.add(layers.Flatten())
model.add(layers.Dense(64,activation='relu'))
model.add(layers.Dense(10,activation='softmax'))
model.compile(optimizer='adam',loss ='sparse_categorical_crossentropy',metrics=['accuracy'])
#모델을 완성하려면, 마지막 합성곱 층의 출력 텐서를 하나 이상의 Dense층에 주입하여 분류를 수행함.
#Dense층은 벡터(1D)를 입력으로 받는데, 출력은 3D임
#고로 3D출력을 1D로 펼치겠담.
#그다음 하나 이상의 Dense층을 그위에 추가하겠음
#Mnist 데이터는 10갸의 클래스가 있으므로 마지막의 Dense층에 10개의 출력과 소프트맥스활성화 함수를 사용함.

model.fit(train_images,train_labels,epochs=5)

test_loss,test_acc = model.evaluate(test_images,test_labels,verbose=2)
print(test_acc)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62

<<<<<<< HEAD
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
#데이터 불러오기
fashion_mnist = keras.datasets.fashion_mnist
#load_data()는 네 개의 넘파이 배열로 변경
(train_images,train_labels),(test_images,test_labels) =fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
print(train_images.shape)
print(len(train_labels))
print(test_images.shape)
print(len(test_labels))
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()
#이미지는 28*28의 크기이고, 픽셀 값이 0~255사이임
#아래는 픽셀값을 조정하는 것
train_images =train_images/ 255.0
test_images = test_images / 255.0
plt.figure(figsize=(10,10))#PLT의 사이즈를 조정함 figsize
for i in range(25):#등장할 사진의 갯수
    plt.subplot(5,5,i+1)#내가 그림을 그리는 영역을 정해줌 i+1은 그곳에서 몇 번째!
    plt.xticks([])#x축의 눈금을 표시합니다
    plt.yticks([])#y축의 눈금을 표시합니다
    plt.grid(False) #눈금자를 볼 것인지 안 볼것인지
    plt.imshow(train_images[i],cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()
#Sequential은 정확히 하나의 입력에서 하나의 출력이 있는 경우
#keras.layers를 통해 접근
#flatten은 28*28->784인 1차원 배열로 변환 ->가중치는 없고 데이터만 변환
#softmax로 현재이미지가 10개 클래스 중 하나에 속할 확률을 출력하게 함
model = keras.Sequential([keras.layers.Flatten(input_shape=(28, 28)),keras.layers.Dense(128, activation='relu'),keras.layers.Dense(10, activation='softmax')])
#Dense는 전합층(완전히 연결된 층)을 추가
#모델을 기계가 이해할 수 있도록 만들어줌
#optimizer는 훈련과정 설정, 모델업데이터하는 방법
#loss는 사용할 손실 함수를 설정
#metrics 훈련을 모니터링하기 위한 지표->올바르게 분류된 이미지의 비율인 정확도를 사용
model.compile(optimizer='adam',loss = 'sparse_categorical_crossentropy',metrics=['accuracy'])
#모델 학습
model.fit(train_images, train_labels, epochs=5)
#모델 평가
#verbose는 학습 중 출력되는 문구 설정 2는 배치마다 손실정보 출력
#evaluate는 모델의 정확도를 평가
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\n테스트 정확도:', test_acc) #새로운 데이터에서 과대적합 때문에 성능이 낮음 
predictions = model.predict(test_images)#테스트모델로 예측
print(predictions[0])#각 이미지의 레이블을 예측 <- 각 레이블에 해당하는 신뢰도
print(np.argmax(predictions[0]))#가장 신뢰성이 높은 레이블은??
print(test_labels[0])#이제 확인해보는 거지 <-실제랑 위에 것이랑 맞는지
def plot_image(i, predictions_array, true_label, img):#예시 하나와 이름,확률,예측값
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary) #색을 알아서 정해줌
    predicted_label = np.argmax(predictions_array)#가장 신뢰성 있는 것을 넣음
    if predicted_label == true_label:#만약에 맞다면
        color = 'blue'#잘되면 블루로
    else:
        color = 'red' #잘못되었으면 red로
    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],100*np.max(predictions_array),class_names[true_label]),color=color)
def plot_value_array(i, predictions_array, true_label):#진짜 이름이랑 예측률 등을 다 만들어줌 
    predictions_array, true_label = predictions_array[i], true_label[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)
    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')
i = 0 # 0번째의 이미지, 예측, 신뢰도 점수
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels)
plt.show()
i = 12
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels)#이미지를 넣으면 predictions으로 나옴
plt.show()
# 처음 X 개의 테스트 이미지와 예측 레이블, 진짜 레이블을 출력합니다
# 올바른 예측은 파랑색으로 잘못된 예측은 빨강색으로 나타냅니다
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows)) #글자 쓰는 곳, 사진, 결과
for i in range(num_images): #사진 갯수 3*5
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, predictions, test_labels, test_images)
    plt.subplot(num_rows, 2*num_cols, 2*i+2)
    plot_value_array(i, predictions, test_labels)
plt.show()
#새로운 이미지 사진 등록
#이미지 사진을 28*28로 변환
#np.array.img로 만들고 예측하기
img = test_images[0] #테스트에서 이미지 선택 내가 이미지 넣고싶으면 여기에 넣음
print(img.shape) #한 번에 샘플의 묶음 또는 배치로 예측을 만듬 ->2차원배열로 만듬
img = (np.expand_dims(img,0))
print(img.shape)
predictions_single = model.predict(img)#예측해봄
print(predictions_single)#결과는 어디에 가장 가깝니?!
plot_value_array(0, predictions_single, test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)#그림을 그리자, x좌표에 class_name으로
=======
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
#데이터 불러오기
fashion_mnist = keras.datasets.fashion_mnist
#load_data()는 네 개의 넘파이 배열로 변경
(train_images,train_labels),(test_images,test_labels) =fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
print(train_images.shape)
print(len(train_labels))
print(test_images.shape)
print(len(test_labels))
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()
#이미지는 28*28의 크기이고, 픽셀 값이 0~255사이임
#아래는 픽셀값을 조정하는 것
train_images =train_images/ 255.0
test_images = test_images / 255.0
plt.figure(figsize=(10,10))#PLT의 사이즈를 조정함 figsize
for i in range(25):#등장할 사진의 갯수
    plt.subplot(5,5,i+1)#내가 그림을 그리는 영역을 정해줌 i+1은 그곳에서 몇 번째!
    plt.xticks([])#x축의 눈금을 표시합니다
    plt.yticks([])#y축의 눈금을 표시합니다
    plt.grid(False) #눈금자를 볼 것인지 안 볼것인지
    plt.imshow(train_images[i],cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()
#Sequential은 정확히 하나의 입력에서 하나의 출력이 있는 경우
#keras.layers를 통해 접근
#flatten은 28*28->784인 1차원 배열로 변환 ->가중치는 없고 데이터만 변환
#softmax로 현재이미지가 10개 클래스 중 하나에 속할 확률을 출력하게 함
model = keras.Sequential([keras.layers.Flatten(input_shape=(28, 28)),keras.layers.Dense(128, activation='relu'),keras.layers.Dense(10, activation='softmax')])
#Dense는 전합층(완전히 연결된 층)을 추가
#모델을 기계가 이해할 수 있도록 만들어줌
#optimizer는 훈련과정 설정, 모델업데이터하는 방법
#loss는 사용할 손실 함수를 설정
#metrics 훈련을 모니터링하기 위한 지표->올바르게 분류된 이미지의 비율인 정확도를 사용
model.compile(optimizer='adam',loss = 'sparse_categorical_crossentropy',metrics=['accuracy'])
#모델 학습
model.fit(train_images, train_labels, epochs=5)
#모델 평가
#verbose는 학습 중 출력되는 문구 설정 2는 배치마다 손실정보 출력
#evaluate는 모델의 정확도를 평가
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\n테스트 정확도:', test_acc) #새로운 데이터에서 과대적합 때문에 성능이 낮음 
predictions = model.predict(test_images)#테스트모델로 예측
print(predictions[0])#각 이미지의 레이블을 예측 <- 각 레이블에 해당하는 신뢰도
print(np.argmax(predictions[0]))#가장 신뢰성이 높은 레이블은??
print(test_labels[0])#이제 확인해보는 거지 <-실제랑 위에 것이랑 맞는지
def plot_image(i, predictions_array, true_label, img):#예시 하나와 이름,확률,예측값
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary) #색을 알아서 정해줌
    predicted_label = np.argmax(predictions_array)#가장 신뢰성 있는 것을 넣음
    if predicted_label == true_label:#만약에 맞다면
        color = 'blue'#잘되면 블루로
    else:
        color = 'red' #잘못되었으면 red로
    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],100*np.max(predictions_array),class_names[true_label]),color=color)
def plot_value_array(i, predictions_array, true_label):#진짜 이름이랑 예측률 등을 다 만들어줌 
    predictions_array, true_label = predictions_array[i], true_label[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)
    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')
i = 0 # 0번째의 이미지, 예측, 신뢰도 점수
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels)
plt.show()
i = 12
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels)#이미지를 넣으면 predictions으로 나옴
plt.show()
# 처음 X 개의 테스트 이미지와 예측 레이블, 진짜 레이블을 출력합니다
# 올바른 예측은 파랑색으로 잘못된 예측은 빨강색으로 나타냅니다
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows)) #글자 쓰는 곳, 사진, 결과
for i in range(num_images): #사진 갯수 3*5
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, predictions, test_labels, test_images)
    plt.subplot(num_rows, 2*num_cols, 2*i+2)
    plot_value_array(i, predictions, test_labels)
plt.show()
#새로운 이미지 사진 등록
#이미지 사진을 28*28로 변환
#np.array.img로 만들고 예측하기
img = test_images[0] #테스트에서 이미지 선택 내가 이미지 넣고싶으면 여기에 넣음
print(img.shape) #한 번에 샘플의 묶음 또는 배치로 예측을 만듬 ->2차원배열로 만듬
img = (np.expand_dims(img,0))
print(img.shape)
predictions_single = model.predict(img)#예측해봄
print(predictions_single)#결과는 어디에 가장 가깝니?!
plot_value_array(0, predictions_single, test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)#그림을 그리자, x좌표에 class_name으로
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
np.argmax(predictions_single[0])
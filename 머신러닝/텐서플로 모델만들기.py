<<<<<<< HEAD
from numpy.lib.function_base import gradient
import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model

mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test) = mnist.load_data()
x_train, x_test = x_train/255.0 , x_test/255.0

#채널 차원을 추가합니다.
x_train = x_train[...,tf.newaxis]
x_test = x_test[...,tf.newaxis]
train_ds = tf.data.Dataset.from_tensor_slices((x_train,y_train)).shuffle(10000).batch(32)
test_ds = tf.data.Dataset.from_tensor_slices((x_test,y_test)).batch(32)
#keras의 모델 서브클래싱 API를 사용 tf.keras모델 만듬
class MyModel(Model):
    def __init__(self):
        super(MyModel,self).__init__()
        self.conv1 = Conv2D(32,3,activation='relu')
        self.flatten = Flatten()
        self.d1 = Dense(128,activation='relu')
        self.d2 = Dense(10,activation='softmax')
    def call(self, x):
        x = self.conv1(x)
        x = self.flatten(x)
        x = self.d1(x)
        return self.d2(x)
model = MyModel()
#옵티마이저와 손실함수 선택
loss_object = tf.keras.losses.SparseCategoricalCrossentropy()
optimizer = tf.keras.optimizers.Adam()
#성능 지표 선택, 결과 출력
train_loss = tf.keras.metrics.Mean(name="train_loss")
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name="train_accuracy")
test_loss = tf.keras.metrics.Mean(name="test_loss")
test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name="test_accuracy")
#tf.GradientTape를 사용해 모델 훈련
@tf.function
def train_step(images, labels):
    with tf.GradientTape() as tape:
        predictions = model(images)
        loss = loss_object(labels,predictions)
    gradients = tape.gradient(loss,model.trainable_variables)
    optimizer.apply_gradients(zip(gradients,model.trainable_variables))
    train_loss(loss)
    train_accuracy(labels,predictions)
@tf.function
def test_step(images,labels):
    predictions =model(images)
    t_loss = loss_object(labels,predictions)
    test_loss(t_loss)
    test_accuracy(labels,predictions)
EPOCHS = 5
for epoch in range(EPOCHS):
    for images, labels in train_ds:
        train_step(images,labels)
    for test_images,test_labels in test_ds:
        test_step(test_images,test_labels)
    template='에포크: {}, 손실: {}, 정확도: {}, 테스트 손실: {}, 테스트 정확도: {}'
=======
from numpy.lib.function_base import gradient
import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model

mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test) = mnist.load_data()
x_train, x_test = x_train/255.0 , x_test/255.0

#채널 차원을 추가합니다.
x_train = x_train[...,tf.newaxis]
x_test = x_test[...,tf.newaxis]
train_ds = tf.data.Dataset.from_tensor_slices((x_train,y_train)).shuffle(10000).batch(32)
test_ds = tf.data.Dataset.from_tensor_slices((x_test,y_test)).batch(32)
#keras의 모델 서브클래싱 API를 사용 tf.keras모델 만듬
class MyModel(Model):
    def __init__(self):
        super(MyModel,self).__init__()
        self.conv1 = Conv2D(32,3,activation='relu')
        self.flatten = Flatten()
        self.d1 = Dense(128,activation='relu')
        self.d2 = Dense(10,activation='softmax')
    def call(self, x):
        x = self.conv1(x)
        x = self.flatten(x)
        x = self.d1(x)
        return self.d2(x)
model = MyModel()
#옵티마이저와 손실함수 선택
loss_object = tf.keras.losses.SparseCategoricalCrossentropy()
optimizer = tf.keras.optimizers.Adam()
#성능 지표 선택, 결과 출력
train_loss = tf.keras.metrics.Mean(name="train_loss")
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name="train_accuracy")
test_loss = tf.keras.metrics.Mean(name="test_loss")
test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name="test_accuracy")
#tf.GradientTape를 사용해 모델 훈련
@tf.function
def train_step(images, labels):
    with tf.GradientTape() as tape:
        predictions = model(images)
        loss = loss_object(labels,predictions)
    gradients = tape.gradient(loss,model.trainable_variables)
    optimizer.apply_gradients(zip(gradients,model.trainable_variables))
    train_loss(loss)
    train_accuracy(labels,predictions)
@tf.function
def test_step(images,labels):
    predictions =model(images)
    t_loss = loss_object(labels,predictions)
    test_loss(t_loss)
    test_accuracy(labels,predictions)
EPOCHS = 5
for epoch in range(EPOCHS):
    for images, labels in train_ds:
        train_step(images,labels)
    for test_images,test_labels in test_ds:
        test_step(test_images,test_labels)
    template='에포크: {}, 손실: {}, 정확도: {}, 테스트 손실: {}, 테스트 정확도: {}'
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
    print(template.format(epoch+1,train_loss.result(),train_accuracy.result()*100,test_loss.result(),test_accuracy.result()*100))
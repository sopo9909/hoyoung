<<<<<<< HEAD
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
from datetime import datetime
startTime = datetime.now()
#os.environ["CUDA_VISIBLE_DEVICES"] = "0"
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels),(test_images, test_labels)=fashion_mnist.load_data()
class_names = ['T-shirt/top','Trouser','Pullover','Derss','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
def create_model():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28,28)),
        keras.layers.Dense(128,activation='relu'), 
        keras.layers.Dense(10,activation='softmax') 
    ])
    model.compile(optimizer='adam',
                 loss = 'sparse_categorical_crossentropy', 
                 metrics=['accuracy']) 
    return model
import os
checkpoint_path = 'training_1/cp.ckpt'
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath = checkpoint_path, save_weights_only=True,verbose=1)
model=create_model()
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images,test_labels),callbacks=[cp_callback])
loss,acc = model.evaluate(test_images,test_labels,verbose=2)
print("훈련된지 않은 모델의 정확도 : {:5.2f}%".format(100*acc))
# 가중치 로드
model.load_weights(checkpoint_path)
# 모델 재평가
loss,acc = model.evaluate(test_images,test_labels,verbose=2)
#파일 이름에 에포크 번호 포함
checkpoint_path = 'training_1/cp-{epoch:04d}.ckpt'
checkpoint_dir = os.path.dirname(checkpoint_path)
# 다섯번째 에포크마다 저장(저장 주기 설정)
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath = checkpoint_path,
    save_weights_only=True,
    verbose=1,
    save_freq="epoch")
# 새로운 모델 객체
model = create_model()
# checkpoint_path 가중치 저장
model.save_weights(checkpoint_path.format(epoch=0))
model.fit(train_images,
          train_labels,
          epochs=10,
          validation_data=(test_images,test_labels),
          callbacks=[cp_callback],
          verbose=0)
latest = tf.train.latest_checkpoint(checkpoint_dir)
latest
# warning 메시지 숨기기
import warnings
warnings.filterwarnings(action="ignore")
# 새로운 모델 객체
model = create_model()
#최종 체크포인트 로드
model.load_weights(latest)
# 모델 적용
loss,acc = model.evaluate(test_images, test_labels, verbose=2)
# weights 저장
model.save_weights("./checkpoints/my_checkpoint")
# weights 읽어오기
model1 = create_model()
model1.load_weights("./checkpoints/my_checkpoint")
# 모델 적용
loss,acc = model1.evaluate(test_images, test_labels, verbose=2)
print("결과:", datetime.now() - startTime)
=======
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
from datetime import datetime
startTime = datetime.now()
#os.environ["CUDA_VISIBLE_DEVICES"] = "0"
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels),(test_images, test_labels)=fashion_mnist.load_data()
class_names = ['T-shirt/top','Trouser','Pullover','Derss','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
def create_model():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28,28)),
        keras.layers.Dense(128,activation='relu'), 
        keras.layers.Dense(10,activation='softmax') 
    ])
    model.compile(optimizer='adam',
                 loss = 'sparse_categorical_crossentropy', 
                 metrics=['accuracy']) 
    return model
import os
checkpoint_path = 'training_1/cp.ckpt'
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath = checkpoint_path, save_weights_only=True,verbose=1)
model=create_model()
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images,test_labels),callbacks=[cp_callback])
loss,acc = model.evaluate(test_images,test_labels,verbose=2)
print("훈련된지 않은 모델의 정확도 : {:5.2f}%".format(100*acc))
# 가중치 로드
model.load_weights(checkpoint_path)
# 모델 재평가
loss,acc = model.evaluate(test_images,test_labels,verbose=2)
#파일 이름에 에포크 번호 포함
checkpoint_path = 'training_1/cp-{epoch:04d}.ckpt'
checkpoint_dir = os.path.dirname(checkpoint_path)
# 다섯번째 에포크마다 저장(저장 주기 설정)
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath = checkpoint_path,
    save_weights_only=True,
    verbose=1,
    save_freq="epoch")
# 새로운 모델 객체
model = create_model()
# checkpoint_path 가중치 저장
model.save_weights(checkpoint_path.format(epoch=0))
model.fit(train_images,
          train_labels,
          epochs=10,
          validation_data=(test_images,test_labels),
          callbacks=[cp_callback],
          verbose=0)
latest = tf.train.latest_checkpoint(checkpoint_dir)
latest
# warning 메시지 숨기기
import warnings
warnings.filterwarnings(action="ignore")
# 새로운 모델 객체
model = create_model()
#최종 체크포인트 로드
model.load_weights(latest)
# 모델 적용
loss,acc = model.evaluate(test_images, test_labels, verbose=2)
# weights 저장
model.save_weights("./checkpoints/my_checkpoint")
# weights 읽어오기
model1 = create_model()
model1.load_weights("./checkpoints/my_checkpoint")
# 모델 적용
loss,acc = model1.evaluate(test_images, test_labels, verbose=2)
print("결과:", datetime.now() - startTime)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62

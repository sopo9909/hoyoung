<<<<<<< HEAD
import os
import tensorflow as tf
from tensorflow import keras
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
train_labels = train_labels[:1000]#1000개만 가져오기
test_labels = test_labels[:1000]#1000개만 가져오기
train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0#사이즈 정하기
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0#사이즈 정하기
# 간단한 Sequential 모델을 정의합니다
def create_model():#Sequential으로 모델을 하나 만드는 것 전체를 함수로 만듬
  model = tf.keras.models.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10)
  ])
  model.compile(optimizer='adam',
                loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])
  return model
# 모델 객체를 만듭니다
model = create_model() #위의 모델 만드는 함수
# 모델 구조를 출력합니다
model.summary()
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
# 모델의 가중치를 저장하는 콜백 만들기->특별한 것 아니고 이어서 훈련하게 하는 것
#epochs가 하나될 때마다 저장함
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)
# 새로운 콜백으로 모델 훈련하기
model.fit(train_images, 
          train_labels,  
          epochs=10,
          validation_data=(test_images,test_labels),
          callbacks=[cp_callback])  # 콜백을 훈련에 전달합니다
#텐서플로 체크포인트 파일을 만들고 에포크가 종료될 때마다 업데이트!
#훈련하지 않은 새로운 모델을 만들어 보겠음 
#가중치만 복원할 땐 원본 모델과 동일한 구조로 모델을 만들어야 함
#여기서는 동일한 구조로 모델을 만들었으므로 다른 객체이지만 가중치를 공유할 수 있음
#훈련하지 않은 새 모델을 만들고 테스트 세트에서 평가해 보죠. 
#훈련되지 않은 모델의 성능은 무작위로 선택하는 정도의 수준임
#모델을 다시 불러오고
model = create_model()
# 모델을 평가합니다
loss, acc = model.evaluate(test_images,  test_labels, verbose=2)
print("훈련되지 않은 모델의 정확도: {:5.2f}%".format(100*acc))
#가중치 로드
#체크포인트에서 가중치를 로드하고 다시 평가해 보겠음 #load_weights(): 가중치를 로드하는 방법 
model.load_weights(checkpoint_path)
#모델 재평가
loss,acc = model.evaluate(test_images,  test_labels, verbose=2)
print("복원된 모델의 정확도: {:5.2f}%".format(100*acc))
#파일 이름에 에포크 번호를 포함시킵니다(`str.format` 포맷)
#새로운 모델을 훈련하고 다섯 번의 에포크마다 고유한 이름으로 체크포인트를 저장해 보겠음.
checkpoint_path = "training_2/cp-{epoch:04d}.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)#위치 지정
#다섯 번째 에포크마다 가중치를 저장하기 위한 콜백을 만듭니다
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path, 
    verbose=1, 
    save_weights_only=True,
    period=5)
#새로운 모델 객체를 만듭니다
model = create_model()
#`checkpoint_path` 포맷을 사용하는 가중치를 저장합니다
model.save_weights(checkpoint_path.format(epoch=0))
#새로운 콜백을 사용하여 모델을 훈련합니다
model.fit(train_images, 
          train_labels,
          epochs=50, 
          callbacks=[cp_callback],
          validation_data=(test_images,test_labels),
          verbose=0)
#만들어진 체크포인트를 확인해 보고 마지막 체크포인트를 선택해 보겠습니다:
latest = tf.train.latest_checkpoint(checkpoint_dir)
print(latest)
#서플로는 기본적으로 최근 5개의 체크포인트만 저장합니다.
#모델을 초기화하고 최근 체크포인트를 로드하여 테스트해 보겠습니다
#새로운 모델 객체를 만듭니다
model = create_model()
#이전에 저장한 가중치를 로드합니다
model.load_weights(latest)
#모델을 재평가합니다
loss, acc = model.evaluate(test_images, test_labels, verbose=2)
print("복원된 모델의 정확도: {:5.2f}%".format(100*acc))

###수동으로 가중치 저장하기###
# 가중치를 저장합니다
model.save_weights('./checkpoints/my_checkpoint')
# 새로운 모델 객체를 만듭니다
model = create_model()
# 가중치를 복원함
model.load_weights('./checkpoints/my_checkpoint')
# 다시 모델을 평가함
loss,acc = model.evaluate(test_images,  test_labels, verbose=2)
print("복원된 모델의 정확도: {:5.2f}%".format(100*acc))
###전체 모델 저장하기###
# 새로운 모델 객체를 만들고 훈련함
model = create_model()
model.fit(train_images, train_labels, epochs=5)

### SavedModel로 전체 모델을 저장합니다 ###
model.save('saved_model/my_model')
new_model = tf.keras.models.load_model('saved_model/my_model')
# 모델 구조를 확인함
new_model.summary()
# 복원된 모델을 평가함
loss, acc = new_model.evaluate(test_images,  test_labels, verbose=2)
print('복원된 모델의 정확도: {:5.2f}%'.format(100*acc))
print(new_model.predict(test_images).shape)
# 새로운 모델 객체를 만들고 훈련함
model = create_model()
model.fit(train_images, train_labels, epochs=5)
# 전체 모델을 HDF5 파일로 저장함 <-여기에는 다 들어감
# '.h5' 확장자는 이 모델이 HDF5로 저장되었다는 것을 나타냄
model.save('my_model.h5')
# 가중치와 옵티마이저를 포함하여 정확히 동일한 모델을 다시 생성함
new_model = tf.keras.models.load_model('my_model.h5')
# 모델 구조를 출력파악
new_model.summary()
loss, acc = new_model.evaluate(test_images,  test_labels, verbose=2)
=======
import os
import tensorflow as tf
from tensorflow import keras
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
train_labels = train_labels[:1000]#1000개만 가져오기
test_labels = test_labels[:1000]#1000개만 가져오기
train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0#사이즈 정하기
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0#사이즈 정하기
# 간단한 Sequential 모델을 정의합니다
def create_model():#Sequential으로 모델을 하나 만드는 것 전체를 함수로 만듬
  model = tf.keras.models.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10)
  ])
  model.compile(optimizer='adam',
                loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])
  return model
# 모델 객체를 만듭니다
model = create_model() #위의 모델 만드는 함수
# 모델 구조를 출력합니다
model.summary()
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
# 모델의 가중치를 저장하는 콜백 만들기->특별한 것 아니고 이어서 훈련하게 하는 것
#epochs가 하나될 때마다 저장함
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)
# 새로운 콜백으로 모델 훈련하기
model.fit(train_images, 
          train_labels,  
          epochs=10,
          validation_data=(test_images,test_labels),
          callbacks=[cp_callback])  # 콜백을 훈련에 전달합니다
#텐서플로 체크포인트 파일을 만들고 에포크가 종료될 때마다 업데이트!
#훈련하지 않은 새로운 모델을 만들어 보겠음 
#가중치만 복원할 땐 원본 모델과 동일한 구조로 모델을 만들어야 함
#여기서는 동일한 구조로 모델을 만들었으므로 다른 객체이지만 가중치를 공유할 수 있음
#훈련하지 않은 새 모델을 만들고 테스트 세트에서 평가해 보죠. 
#훈련되지 않은 모델의 성능은 무작위로 선택하는 정도의 수준임
#모델을 다시 불러오고
model = create_model()
# 모델을 평가합니다
loss, acc = model.evaluate(test_images,  test_labels, verbose=2)
print("훈련되지 않은 모델의 정확도: {:5.2f}%".format(100*acc))
#가중치 로드
#체크포인트에서 가중치를 로드하고 다시 평가해 보겠음 #load_weights(): 가중치를 로드하는 방법 
model.load_weights(checkpoint_path)
#모델 재평가
loss,acc = model.evaluate(test_images,  test_labels, verbose=2)
print("복원된 모델의 정확도: {:5.2f}%".format(100*acc))
#파일 이름에 에포크 번호를 포함시킵니다(`str.format` 포맷)
#새로운 모델을 훈련하고 다섯 번의 에포크마다 고유한 이름으로 체크포인트를 저장해 보겠음.
checkpoint_path = "training_2/cp-{epoch:04d}.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)#위치 지정
#다섯 번째 에포크마다 가중치를 저장하기 위한 콜백을 만듭니다
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path, 
    verbose=1, 
    save_weights_only=True,
    period=5)
#새로운 모델 객체를 만듭니다
model = create_model()
#`checkpoint_path` 포맷을 사용하는 가중치를 저장합니다
model.save_weights(checkpoint_path.format(epoch=0))
#새로운 콜백을 사용하여 모델을 훈련합니다
model.fit(train_images, 
          train_labels,
          epochs=50, 
          callbacks=[cp_callback],
          validation_data=(test_images,test_labels),
          verbose=0)
#만들어진 체크포인트를 확인해 보고 마지막 체크포인트를 선택해 보겠습니다:
latest = tf.train.latest_checkpoint(checkpoint_dir)
print(latest)
#서플로는 기본적으로 최근 5개의 체크포인트만 저장합니다.
#모델을 초기화하고 최근 체크포인트를 로드하여 테스트해 보겠습니다
#새로운 모델 객체를 만듭니다
model = create_model()
#이전에 저장한 가중치를 로드합니다
model.load_weights(latest)
#모델을 재평가합니다
loss, acc = model.evaluate(test_images, test_labels, verbose=2)
print("복원된 모델의 정확도: {:5.2f}%".format(100*acc))

###수동으로 가중치 저장하기###
# 가중치를 저장합니다
model.save_weights('./checkpoints/my_checkpoint')
# 새로운 모델 객체를 만듭니다
model = create_model()
# 가중치를 복원함
model.load_weights('./checkpoints/my_checkpoint')
# 다시 모델을 평가함
loss,acc = model.evaluate(test_images,  test_labels, verbose=2)
print("복원된 모델의 정확도: {:5.2f}%".format(100*acc))
###전체 모델 저장하기###
# 새로운 모델 객체를 만들고 훈련함
model = create_model()
model.fit(train_images, train_labels, epochs=5)

### SavedModel로 전체 모델을 저장합니다 ###
model.save('saved_model/my_model')
new_model = tf.keras.models.load_model('saved_model/my_model')
# 모델 구조를 확인함
new_model.summary()
# 복원된 모델을 평가함
loss, acc = new_model.evaluate(test_images,  test_labels, verbose=2)
print('복원된 모델의 정확도: {:5.2f}%'.format(100*acc))
print(new_model.predict(test_images).shape)
# 새로운 모델 객체를 만들고 훈련함
model = create_model()
model.fit(train_images, train_labels, epochs=5)
# 전체 모델을 HDF5 파일로 저장함 <-여기에는 다 들어감
# '.h5' 확장자는 이 모델이 HDF5로 저장되었다는 것을 나타냄
model.save('my_model.h5')
# 가중치와 옵티마이저를 포함하여 정확히 동일한 모델을 다시 생성함
new_model = tf.keras.models.load_model('my_model.h5')
# 모델 구조를 출력파악
new_model.summary()
loss, acc = new_model.evaluate(test_images,  test_labels, verbose=2)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
print('복원된 모델의 정확도: {:5.2f}%'.format(100*acc))
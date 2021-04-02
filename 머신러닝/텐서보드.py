<<<<<<< HEAD
#%%
#텐서보드
#%load_ext tensorboard
import os
import tensorflow as tf
import datetime
from tensorflow.keras.callbacks import TensorBoard
from tensorflow import keras
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

def create_model():
  return tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
  ])
model = create_model()
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
#저장해야할 위치 + 파일이름(시분초로)
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
#언제 실행할 것이냐?! 콜백으로 한다.
#histogram
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model.fit(x=x_train, 
          y=y_train, 
          epochs=5, 
          validation_data=(x_test, y_test), 
          callbacks=[tensorboard_callback])
#tensorboard --logdir logs/fit #저장 폴더명을 적어준다 #실행하려면 터미널창에 입력





# train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
# test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))
# train_dataset = train_dataset.shuffle(60000).batch(64)
# test_dataset = test_dataset.batch(64)
# loss_object = tf.keras.losses.SparseCategoricalCrossentropy()
# optimizer = tf.keras.optimizers.Adam()
# #매트릭스 정의
# train_loss = tf.keras.metrics.Mean('train_loss', dtype=tf.float32)
# train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy('train_accuracy')
# test_loss = tf.keras.metrics.Mean('test_loss', dtype=tf.float32)
# test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy('test_accuracy')
# #교육 및 테스트 기능
# def train_step(model, optimizer, x_train, y_train):
#   with tf.GradientTape() as tape:
#     predictions = model(x_train, training=True)
#     loss = loss_object(y_train, predictions)
#   grads = tape.gradient(loss, model.trainable_variables)
#   optimizer.apply_gradients(zip(grads, model.trainable_variables))
#   train_loss(loss)
#   train_accuracy(y_train, predictions)
# def test_step(model, x_test, y_test):
#   predictions = model(x_test)
#   loss = loss_object(y_test, predictions)
#   test_loss(loss)
#   test_accuracy(y_test, predictions)
# current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
# train_log_dir = 'logs/gradient_tape/' + current_time + '/train'
# test_log_dir = 'logs/gradient_tape/' + current_time + '/test'
# train_summary_writer = tf.summary.create_file_writer(train_log_dir)
# test_summary_writer = tf.summary.create_file_writer(test_log_dir)
# model = create_model() # reset our model
# EPOCHS = 5
# for epoch in range(EPOCHS):
#   for (x_train, y_train) in train_dataset:
#     train_step(model, optimizer, x_train, y_train)
#   with train_summary_writer.as_default():
#     tf.summary.scalar('loss', train_loss.result(), step=epoch)
#     tf.summary.scalar('accuracy', train_accuracy.result(), step=epoch)
#   for (x_test, y_test) in test_dataset:
#     test_step(model, x_test, y_test)
#   with test_summary_writer.as_default():
#     tf.summary.scalar('loss', test_loss.result(), step=epoch)
#     tf.summary.scalar('accuracy', test_accuracy.result(), step=epoch)
#   template = 'Epoch {}, Loss: {}, Accuracy: {}, Test Loss: {}, Test Accuracy: {}'
#   print (template.format(epoch+1,
#                          train_loss.result(), 
#                          train_accuracy.result()*100,
#                          test_loss.result(), 
#                          test_accuracy.result()*100))
#   # Reset metrics every epoch
#   train_loss.reset_states()
#   test_loss.reset_states()
#   train_accuracy.reset_states()
#   test_accuracy.reset_states()
# #%tensorboard --logdir logs/gradient_tape
# %%
=======
#%%
#텐서보드
#%load_ext tensorboard
import os
import tensorflow as tf
import datetime
from tensorflow.keras.callbacks import TensorBoard
from tensorflow import keras
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

def create_model():
  return tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
  ])
model = create_model()
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
#저장해야할 위치 + 파일이름(시분초로)
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
#언제 실행할 것이냐?! 콜백으로 한다.
#histogram
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model.fit(x=x_train, 
          y=y_train, 
          epochs=5, 
          validation_data=(x_test, y_test), 
          callbacks=[tensorboard_callback])
#tensorboard --logdir logs/fit #저장 폴더명을 적어준다 #실행하려면 터미널창에 입력





# train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
# test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))
# train_dataset = train_dataset.shuffle(60000).batch(64)
# test_dataset = test_dataset.batch(64)
# loss_object = tf.keras.losses.SparseCategoricalCrossentropy()
# optimizer = tf.keras.optimizers.Adam()
# #매트릭스 정의
# train_loss = tf.keras.metrics.Mean('train_loss', dtype=tf.float32)
# train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy('train_accuracy')
# test_loss = tf.keras.metrics.Mean('test_loss', dtype=tf.float32)
# test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy('test_accuracy')
# #교육 및 테스트 기능
# def train_step(model, optimizer, x_train, y_train):
#   with tf.GradientTape() as tape:
#     predictions = model(x_train, training=True)
#     loss = loss_object(y_train, predictions)
#   grads = tape.gradient(loss, model.trainable_variables)
#   optimizer.apply_gradients(zip(grads, model.trainable_variables))
#   train_loss(loss)
#   train_accuracy(y_train, predictions)
# def test_step(model, x_test, y_test):
#   predictions = model(x_test)
#   loss = loss_object(y_test, predictions)
#   test_loss(loss)
#   test_accuracy(y_test, predictions)
# current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
# train_log_dir = 'logs/gradient_tape/' + current_time + '/train'
# test_log_dir = 'logs/gradient_tape/' + current_time + '/test'
# train_summary_writer = tf.summary.create_file_writer(train_log_dir)
# test_summary_writer = tf.summary.create_file_writer(test_log_dir)
# model = create_model() # reset our model
# EPOCHS = 5
# for epoch in range(EPOCHS):
#   for (x_train, y_train) in train_dataset:
#     train_step(model, optimizer, x_train, y_train)
#   with train_summary_writer.as_default():
#     tf.summary.scalar('loss', train_loss.result(), step=epoch)
#     tf.summary.scalar('accuracy', train_accuracy.result(), step=epoch)
#   for (x_test, y_test) in test_dataset:
#     test_step(model, x_test, y_test)
#   with test_summary_writer.as_default():
#     tf.summary.scalar('loss', test_loss.result(), step=epoch)
#     tf.summary.scalar('accuracy', test_accuracy.result(), step=epoch)
#   template = 'Epoch {}, Loss: {}, Accuracy: {}, Test Loss: {}, Test Accuracy: {}'
#   print (template.format(epoch+1,
#                          train_loss.result(), 
#                          train_accuracy.result()*100,
#                          test_loss.result(), 
#                          test_accuracy.result()*100))
#   # Reset metrics every epoch
#   train_loss.reset_states()
#   test_loss.reset_states()
#   train_accuracy.reset_states()
#   test_accuracy.reset_states()
# #%tensorboard --logdir logs/gradient_tape
# %%
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62

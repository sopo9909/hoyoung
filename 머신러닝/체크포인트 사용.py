<<<<<<< HEAD
import tensorflow as tf
x = tf.Variable(10.)
checkpoint = tf.train.Checkpoint(x=x)
x.assign(2.)   # 변수에 새로운 값을 할당하고 저장
checkpoint_path = './ckpt/'
checkpoint.save('./ckpt/') #체크포인트 저장
x.assign(11.)
#체크포인트 복구
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_path))
print(x)

import os

model = tf.keras.Sequential([
  tf.keras.layers.Conv2D(16,[3,3], activation='relu'),
  tf.keras.layers.GlobalAveragePooling2D(),
  tf.keras.layers.Dense(10)
])
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
checkpoint_dir = 'path/to/model_dir'
if not os.path.exists(checkpoint_dir):
  os.makedirs(checkpoint_dir)
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
root = tf.train.Checkpoint(optimizer=optimizer,model=model)

root.save(checkpoint_prefix)
=======
import tensorflow as tf
x = tf.Variable(10.)
checkpoint = tf.train.Checkpoint(x=x)
x.assign(2.)   # 변수에 새로운 값을 할당하고 저장
checkpoint_path = './ckpt/'
checkpoint.save('./ckpt/') #체크포인트 저장
x.assign(11.)
#체크포인트 복구
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_path))
print(x)

import os

model = tf.keras.Sequential([
  tf.keras.layers.Conv2D(16,[3,3], activation='relu'),
  tf.keras.layers.GlobalAveragePooling2D(),
  tf.keras.layers.Dense(10)
])
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
checkpoint_dir = 'path/to/model_dir'
if not os.path.exists(checkpoint_dir):
  os.makedirs(checkpoint_dir)
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
root = tf.train.Checkpoint(optimizer=optimizer,model=model)

root.save(checkpoint_prefix)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
root.restore(tf.train.latest_checkpoint(checkpoint_dir))
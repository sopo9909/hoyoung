<<<<<<< HEAD
#import tensorflow as tf
import numpy as np
# a =[[1,2,3],[4,5,6],[7,8,9]]
# b =[[1,1,1,],[1,1,1],[1,1,1]]
# print(a+b)
# d=np.append(a,b,axis=1)
# print(d)
# #c = [sum(t) for t in zip(a,b)]
# c =[[0]*3 for i in range(3)]
# for i in range(0,3):
#     for j in range(0,3):
#         c[i][j] =a[i][j] + b[i][j]
# print(c)
m = np.array([[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]])
a=m[1,2]
print(a)
b=m[2,4]
print(b)
c=m[1,1:3]
print(c)
d=m[1:3,2]
print(d)
e=m[0:2,3:5]
print(e)

#from tensorflow import tf
import tensorflow as tf
# model = tf.keras.Sequential()
# model.add(tf.keras.layers.Dense(64,activation ='relu'))
# model.add(tf.keras.layers.Dense(64,activation ='relu'))
# model.add(tf.keras.layers.Dense(10,activation ='softmax'))
# model.compile(optimizer=tf.keras.optimizers.Adam(0.001),loss ='categorical croossentropy',metrics=['accuracy'])
# model.fit(train_data,labels,epochs=10,batch_size=32)
# model.evaluate(test_data,labels)

###
# input = tf.keras.Input(shape=(784,),name='img')
# h1 =tf.keras.layers.Dense(64,activation ='relu')(input)
# h2 =tf.keras.layers.Dense(64,activation ='relu')(h1)
# output = tf.keras.layers.Dense(10,activation='softmax')(h2)
# model = tf.keras.Model(input,output)

# x = tf.constant(1)
# y = tf.constant(2)
# z = tf.constant(3)
# a =x*y +z
# print(a)
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
# a = tf.constant([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
# print(a)
# b = tf.constant(a,[-1,6])
# tf.transpose(b) #전치행렬(행과 열을 바꿔서 )
print(tf.__version__)

a_data =[1,2,3,4,5]
b_data =[-1,-1,-1,-1,-1]
a=tf.constant(a_data)
b=tf.constant(b_data)
c=a*b
print(c)
c.numpy()
a_data =[1,2,3,4,5]
b_data=[1,4,6,4,9]
a=tf.constant(a_data)
b=tf.constant(b_data)
c=tf.equal(a,b)
=======
#import tensorflow as tf
import numpy as np
# a =[[1,2,3],[4,5,6],[7,8,9]]
# b =[[1,1,1,],[1,1,1],[1,1,1]]
# print(a+b)
# d=np.append(a,b,axis=1)
# print(d)
# #c = [sum(t) for t in zip(a,b)]
# c =[[0]*3 for i in range(3)]
# for i in range(0,3):
#     for j in range(0,3):
#         c[i][j] =a[i][j] + b[i][j]
# print(c)
m = np.array([[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]])
a=m[1,2]
print(a)
b=m[2,4]
print(b)
c=m[1,1:3]
print(c)
d=m[1:3,2]
print(d)
e=m[0:2,3:5]
print(e)

#from tensorflow import tf
import tensorflow as tf
# model = tf.keras.Sequential()
# model.add(tf.keras.layers.Dense(64,activation ='relu'))
# model.add(tf.keras.layers.Dense(64,activation ='relu'))
# model.add(tf.keras.layers.Dense(10,activation ='softmax'))
# model.compile(optimizer=tf.keras.optimizers.Adam(0.001),loss ='categorical croossentropy',metrics=['accuracy'])
# model.fit(train_data,labels,epochs=10,batch_size=32)
# model.evaluate(test_data,labels)

###
# input = tf.keras.Input(shape=(784,),name='img')
# h1 =tf.keras.layers.Dense(64,activation ='relu')(input)
# h2 =tf.keras.layers.Dense(64,activation ='relu')(h1)
# output = tf.keras.layers.Dense(10,activation='softmax')(h2)
# model = tf.keras.Model(input,output)

# x = tf.constant(1)
# y = tf.constant(2)
# z = tf.constant(3)
# a =x*y +z
# print(a)
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
# a = tf.constant([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
# print(a)
# b = tf.constant(a,[-1,6])
# tf.transpose(b) #전치행렬(행과 열을 바꿔서 )
print(tf.__version__)

a_data =[1,2,3,4,5]
b_data =[-1,-1,-1,-1,-1]
a=tf.constant(a_data)
b=tf.constant(b_data)
c=a*b
print(c)
c.numpy()
a_data =[1,2,3,4,5]
b_data=[1,4,6,4,9]
a=tf.constant(a_data)
b=tf.constant(b_data)
c=tf.equal(a,b)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
print(c)
<<<<<<< HEAD
import numpy as np
import time

size = 10000000
#list
x = list(range(size))
y = list(range(size))
start_time = time.time()
z = [x[i]+x[i] for i in range(size)]
print("리스트 걸린시간", time.time()-start_time)
#adlist
x = np.arange(size)
y = np.arange(size)
start_time = time.time()
z = x + y
print("넘파이 걸린시간", time.time()-start_time)

x = np.uint(64)
print(x)
print(type(x))
y = np.uint([1,2,3,4])
print(y)
print(type(y))
print(y.dtype)
z = np.float32([1,2,3,4])
print(z)
print(type(z))
print(z.dtype)
w = np.array([1,2,3,4],dtype=np.float16)
print(w)
print(type(w))
print(w.dtype)
#u = np.int32(u)
#print(u.dtype)
=======
import numpy as np
import time

size = 10000000
#list
x = list(range(size))
y = list(range(size))
start_time = time.time()
z = [x[i]+x[i] for i in range(size)]
print("리스트 걸린시간", time.time()-start_time)
#adlist
x = np.arange(size)
y = np.arange(size)
start_time = time.time()
z = x + y
print("넘파이 걸린시간", time.time()-start_time)

x = np.uint(64)
print(x)
print(type(x))
y = np.uint([1,2,3,4])
print(y)
print(type(y))
print(y.dtype)
z = np.float32([1,2,3,4])
print(z)
print(type(z))
print(z.dtype)
w = np.array([1,2,3,4],dtype=np.float16)
print(w)
print(type(w))
print(w.dtype)
#u = np.int32(u)
#print(u.dtype)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
#np.issubdtype(u.dtype, np.int32) #float32
import numpy as np
import random

x=[1,2,3,4,5,6,7,8,9]
y=[10,20,30,40,50,60,70,80,90]

ax=np.array(x).reshape(3,3)
ay=np.array(y).reshape(3,3)

print(ax+ay)
print(ax.dot(ay))

a = np.linspace(1,20,30)
print(a+10)

c= np.random.randint(1,100,size=(2,10,10))
v= np.where(c>=50,1,2)
print(c)
print(v)
print(v[1,5:10,5:10])

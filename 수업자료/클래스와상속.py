<<<<<<< HEAD
import numpy as np


class charater:
    def __init__(self):
        self.health = 200

    def move(self):
        self.health -= 10
        pass

    def rest(self):
        self.health += 10
        pass

    def checkHealth(self):
        print("너의 피는?",self.health)

class knight(charater):
    def __init__(self):
        super().__init__()
    def move(self):
        self.health -= 15
    def attack(self):
        print("공격합니다")
class healer(charater):
    def __init__(self):
        super().__init__()
        self.Mana = 100
    def heal(self):
        self.Mana -= 10
        input("누구를 치료하겠습니까?")
        charater.rest()
    def checkMana(self):
        print("너의 마나는?",self.Mana)

#healer(매개변수수)

x = np.arange(20)
print(x[1:3])

x= np.arange(20).reshape(4,5)
print(x)
print(x[1:3])
print(x[1:3,1:3])

x = np.arange(30).reshape(2,5,3)
print(x)
print(x[:,3:5,1])

a = np.arange(20).reshape(4,5)
print(a[1][1])
print(a[1,1])
print(a[[1,1],[1,2]])
print(a>3)
print(a[a>3])
print(a[a==1])
print(a[a!=1])
print(a[(a>3)&(a<8)])

np.random.rand(5,5)
np.random.randint(1,10)
print(np.random.randint(1,10,size=(5)))
print(np.random.randint(1,10,size=(5,5)))

x = np.arange(10).reshape(2,5)
y = np.arange(10,20).reshape(2,5)
z=np.concatenate([x,y])
w=np.concatenate([x,y],axis=1)
print(z)
print(w)
q = np.arange(16).reshape(4,4)
np.split(x,2) # 2개씩 분해

e = np.arange(1,10).reshape(3,3)
r = np.arange(1,4)
print(e+r)

k = np.arange(4).reshape(2,2)
l = np.arange(4).reshape(2,2)

np.mean(k)
np.median(k)
np.std(k)
np.var(k)
np.sum(k)
np.cumsum(k)
np.cumprod(k)
np.min(k)
np.max(k)
np.argmax(k)
np.argmin(k)
np.any(k>4)
np.any(k<4)

=======
import numpy as np


class charater:
    def __init__(self):
        self.health = 200

    def move(self):
        self.health -= 10
        pass

    def rest(self):
        self.health += 10
        pass

    def checkHealth(self):
        print("너의 피는?",self.health)

class knight(charater):
    def __init__(self):
        super().__init__()
    def move(self):
        self.health -= 15
    def attack(self):
        print("공격합니다")
class healer(charater):
    def __init__(self):
        super().__init__()
        self.Mana = 100
    def heal(self):
        self.Mana -= 10
        input("누구를 치료하겠습니까?")
        charater.rest()
    def checkMana(self):
        print("너의 마나는?",self.Mana)

#healer(매개변수수)

x = np.arange(20)
print(x[1:3])

x= np.arange(20).reshape(4,5)
print(x)
print(x[1:3])
print(x[1:3,1:3])

x = np.arange(30).reshape(2,5,3)
print(x)
print(x[:,3:5,1])

a = np.arange(20).reshape(4,5)
print(a[1][1])
print(a[1,1])
print(a[[1,1],[1,2]])
print(a>3)
print(a[a>3])
print(a[a==1])
print(a[a!=1])
print(a[(a>3)&(a<8)])

np.random.rand(5,5)
np.random.randint(1,10)
print(np.random.randint(1,10,size=(5)))
print(np.random.randint(1,10,size=(5,5)))

x = np.arange(10).reshape(2,5)
y = np.arange(10,20).reshape(2,5)
z=np.concatenate([x,y])
w=np.concatenate([x,y],axis=1)
print(z)
print(w)
q = np.arange(16).reshape(4,4)
np.split(x,2) # 2개씩 분해

e = np.arange(1,10).reshape(3,3)
r = np.arange(1,4)
print(e+r)

k = np.arange(4).reshape(2,2)
l = np.arange(4).reshape(2,2)

np.mean(k)
np.median(k)
np.std(k)
np.var(k)
np.sum(k)
np.cumsum(k)
np.cumprod(k)
np.min(k)
np.max(k)
np.argmax(k)
np.argmin(k)
np.any(k>4)
np.any(k<4)

>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
np.where(x>4,x,10)
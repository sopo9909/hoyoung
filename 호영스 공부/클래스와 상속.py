class Dog:
    def __init__(self,name,color):
        self.hungry = 0
        self.name = name
        self.color = color

    def eat(self):
        self.hungry -= 10
        print("밥먹음 ",self.hungry)
    def walk(self):
        self.hungry += 10
        print("산책",self.hungry)
    def showme(self):
        print(f"{self.name}:{self.hungry}")

choco =Dog("choco", "black")
jjong =Dog("jjong","white")

choco.eat()
choco.eat()
choco.walk()
print(choco.hungry)
print(jjong.hungry)
#jjong.hungry = 10 으로 값을 바꿔줄 수도 있음
#비공개 속성 - self__hungry = 0하면
#jjong.__hungry += 100 하면 안 됨 외부에서 접근하지 못 하게 함 <-헝그리를 못 변하게

class Cat():
    Cat__count= 0 #클래스 속성
    def __init__(self,name,color):
        self.name = name
        self.color = color
        Cat.Cat__count +=1 #클래스 속성 접근
    def catcount(self):
        print("총 고양이는 : ",Cat.Cat__count)
hello= Cat("Hello","black")
hello.catcount()
tom = Cat("tom","white")
hello.catcount()

class Car():
    car__count = 0
    def __init__(self,name,cc,proyear):
        self.__name = name
        self.__cc = cc
        self.__proyear = proyear
        Car.car__count +=1
    def finame(self):
        print(self.__name)
    def chname(self,name):
        self.__name = name
    def carCount(self):
        print("총 차는 ",Car.car__count,"대 입니다.")
    def opcc(self):
        if self.__cc > 2000:
            print("대형입니다요")
        elif self.__cc >=1000:
            print("중형입니다요")
        else:
            print("소형입니다요")
benz = Car("benz",200,201)
benz.opcc()
benz.carCount()
kia = Car("kia",23223,12)
kia.opcc()
kia.chname("toyota")
kia.finame()
kia.carCount()

class Animal():
    def __init__(self):
        self.hungry = 0
    def eat(self):
        self.hungry -= 10
        print("밥 먹음",self.hungry)
    def walk(self):
        self.hungry += 10
        print("산책함",self.hungry)
class Dog(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        print("멍멍")
    def eat(self,type):
        super().eat()
        print("왈왈")
        if type =="rice":
            print("멍멍")
        else:
            print("안 먹어")
dog = Dog()
dog.eat("rice")
dog.eat("r")
#에러가 나면 그곳에서 멈춤
try:
    for i in range(10,-10,-1):
        print(10/i)
except :
    print("에런데")

import pickle

try:
    with open("data3.p","rb") as file:
        name = pickle.load(file)
        address = pickle.load(file)
        email = pickle.load(file)
        print(name,address,email)
except:
    print("입력해라 이자식아!!!!!!")
    with open("data3.p","wb") as file:
        name = input("이름이 모니 : ")
        address = input("주소는 뭐니 : ")
        email = input("이메일은? : ")
        pickle.dump(name,file)
        pickle.dump(address,file)
        pickle.dump(email,file)

    print("이제 읽는다")

    with open("data3.p","rb") as file:
            name = pickle.load(file)
            address = pickle.load(file)
            email = pickle.load(file)
            print("너의 이름은 ",name,"너의 주소는 ",address,"너의 이메일은 ",email)

class NotNumberException(Exception):
    def __init__(self):
        super().__init__("잘못된 숫자입니다.")
def gugudan(num):
    if num < 1 or num >9:
        raise NotNumberException
    else:
        for i in range(1,10):
            print(f"{num}*{i}={num * i}")
try:
    gugu = int(input("몇단을 외워볼래??"))
    gugudan(gugu)
except NotNumberException as e:
    print("1~9사이 숫자를 넣어야지")

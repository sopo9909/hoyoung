<<<<<<< HEAD
word=["school","game","piano","science","hotel","mountain"]
c =[i for i in word if len(i) >= 6]
print("실행 : ")
print(c)

word=["school","game","piano","science","hotel","mountain"]
c =[len(j) for j in word ]
print("실행 : ")
print(c)

a=[[10,20],[30,40],[50,60]]
b=[[2,3],[4,5],[6,7]]

c=[]
for i in range(len(a)):
    temp =[]
    for j in range(len(a[i])):
        temp.append(a[i][j]*b[i][j])
    c.append(temp)
print(c)

x= []
ad=1
for i in range(3):
    temp =[]
    for j in range(2):
        temp.append(ad)
        ad+=1
    x.append(temp)
print(x)

file = open("file.txt", "w")
file.write("First File")
file.close()

file =open("file.txt", "r")
text=file.read()
print(text)
file.close()

with open("file.txt") as file:
    text = file.read()
    print(text)

import pickle
text = ["first file","Second Line"]
with open("data.pkl","wb") as file:
    pickle.dump(text,file)

with open("data.pkl","rb") as file:
    data = pickle.load(file)
    print(type(data))
    print(data)

name = "tom"
age = 24
address = '서울시 마포구'
scores ={"python":90, "deeplearning": 95, "database":85}
with open("data2.pkl", "wb") as file:
    pickle.dump(name.file)
    pickle.dump(age.file)
    pickle.dump(address.file)
    pickle.dump(scores.file)
with open("data2.pkl","rb") as file:
    name2 = pickle.load(file)
    age2 = pickle.load(file)
    address2 = pickle.load(file)
    scores2 = pickle.load(file)
# func 대신 add 가능
def func(a,b):
    print("함수입니다")
    return a + b
# 실행 방법은 func(a,b)

lis = [1,2,3,1,4,2,1,]
def allindex(my_list,elem):
    temp_list =[]
    for i,e in enumerate(my_list):
        if e ==elem:
            temp_list.append(i)
    return temp_list
aw = int(input("찾고 싶은 값을 써람!"))
=======
word=["school","game","piano","science","hotel","mountain"]
c =[i for i in word if len(i) >= 6]
print("실행 : ")
print(c)

word=["school","game","piano","science","hotel","mountain"]
c =[len(j) for j in word ]
print("실행 : ")
print(c)

a=[[10,20],[30,40],[50,60]]
b=[[2,3],[4,5],[6,7]]

c=[]
for i in range(len(a)):
    temp =[]
    for j in range(len(a[i])):
        temp.append(a[i][j]*b[i][j])
    c.append(temp)
print(c)

x= []
ad=1
for i in range(3):
    temp =[]
    for j in range(2):
        temp.append(ad)
        ad+=1
    x.append(temp)
print(x)

file = open("file.txt", "w")
file.write("First File")
file.close()

file =open("file.txt", "r")
text=file.read()
print(text)
file.close()

with open("file.txt") as file:
    text = file.read()
    print(text)

import pickle
text = ["first file","Second Line"]
with open("data.pkl","wb") as file:
    pickle.dump(text,file)

with open("data.pkl","rb") as file:
    data = pickle.load(file)
    print(type(data))
    print(data)

name = "tom"
age = 24
address = '서울시 마포구'
scores ={"python":90, "deeplearning": 95, "database":85}
with open("data2.pkl", "wb") as file:
    pickle.dump(name.file)
    pickle.dump(age.file)
    pickle.dump(address.file)
    pickle.dump(scores.file)
with open("data2.pkl","rb") as file:
    name2 = pickle.load(file)
    age2 = pickle.load(file)
    address2 = pickle.load(file)
    scores2 = pickle.load(file)
# func 대신 add 가능
def func(a,b):
    print("함수입니다")
    return a + b
# 실행 방법은 func(a,b)

lis = [1,2,3,1,4,2,1,]
def allindex(my_list,elem):
    temp_list =[]
    for i,e in enumerate(my_list):
        if e ==elem:
            temp_list.append(i)
    return temp_list
aw = int(input("찾고 싶은 값을 써람!"))
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
allindex(lis,aw)
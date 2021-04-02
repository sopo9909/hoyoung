<<<<<<< HEAD
def allindex(list,a):
    i = 0
    re =[]
    for x in list:
        if x == a:
            re.append(i)
        i +=1
    return re

lis = [1,2,3,1,4,2,1]
print(allindex(lis,1))

def func(*args):
    for arg in args:
        print(arg)
func(1)
func(1,2,3,4,5)

def funcc(a,*argss):
    print(a,end="  ")
    for arg in argss:
        print(arg, end="")
funcc(100,1,2,3,4,5,)

print()
def calc(a,*args):
    if a == "+":
        x=0
        for arg in args:
            x += arg
        return x
    elif a == "*":
        x=1
        for arg in args:
            x *= arg
        return x

print(calc("+",1,2,3,4,5))
print(calc("*",1,2,3,4,5))

keys = ["name","age","address"]
users = ["tom",20,"incheon"]
dic = list(zip(keys,users))
=======
def allindex(list,a):
    i = 0
    re =[]
    for x in list:
        if x == a:
            re.append(i)
        i +=1
    return re

lis = [1,2,3,1,4,2,1]
print(allindex(lis,1))

def func(*args):
    for arg in args:
        print(arg)
func(1)
func(1,2,3,4,5)

def funcc(a,*argss):
    print(a,end="  ")
    for arg in argss:
        print(arg, end="")
funcc(100,1,2,3,4,5,)

print()
def calc(a,*args):
    if a == "+":
        x=0
        for arg in args:
            x += arg
        return x
    elif a == "*":
        x=1
        for arg in args:
            x *= arg
        return x

print(calc("+",1,2,3,4,5))
print(calc("*",1,2,3,4,5))

keys = ["name","age","address"]
users = ["tom",20,"incheon"]
dic = list(zip(keys,users))
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
print(dic)
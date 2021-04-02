def calcutator(op,n1,n2):
    rec = 0
    if op =="+":
        rec = n1+n2
    elif op =="-":
        rec = n1+n2
    elif op =="*":
        rec = n1*n2
    elif op == "/":
        rec = n1/n2
    else:
        print("함수를 넣어야지~ 안넣으면 맞아죽지~~")
    return rec

print(calcutator("*",3,4))

def func1(*args):
    for i in args:
        print(i)

func1(20,40,60)
func1(80,100)

def showEmployee(a,salary=9000):
    print("Employee",a,"salary is",salary)
showEmployee("Ben",9000)
showEmployee("Ben")

def fun2(name,age):
    print("이름은 :",name,"나이는 :",age)

aw = input("당신의 이름는?")
bw = input("당신의 나이은?")
fun2(aw,bw)
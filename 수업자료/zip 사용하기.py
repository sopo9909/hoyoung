<<<<<<< HEAD
user = int(input("숫자를 입력하세요:"))
for i in range(user+1):
    if i%2==1:
        continue
    else:
        print(i)


print("hello word")
print("감사합니다")

c = [ i for i in range(10) if i%2==0]
print(c)

d = [i*j for i in range(1,10) for j in range(1,10)]
print(d)

keys = ["name","age","address"]
users = ["tom",12 ,"incheon"]
codes = [1,2,3]
for (k,d,c) in zip(keys,users,codes):
    print("{}({}) : {}".format(k,c,d))

=======
user = int(input("숫자를 입력하세요:"))
for i in range(user+1):
    if i%2==1:
        continue
    else:
        print(i)


print("hello word")
print("감사합니다")

c = [ i for i in range(10) if i%2==0]
print(c)

d = [i*j for i in range(1,10) for j in range(1,10)]
print(d)

keys = ["name","age","address"]
users = ["tom",12 ,"incheon"]
codes = [1,2,3]
for (k,d,c) in zip(keys,users,codes):
    print("{}({}) : {}".format(k,c,d))

>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62

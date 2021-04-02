key = ['ten', 'twenty','thirty']
value = [10,20,30]

sampleDict = dict(zip(key,value))
print(sampleDict)

dict1 = {'ten':10, 'twenty': 20,'thirty':30}
dict2 = {'thirty': 30, 'fourty': 40,'fifty': 50}
#dic 합 구하기
dict3 = {**dict1, **dict2}
print(dict3)

samDic = {"class":{
    "student": {
        "name" : "Mike",
        "marks":{
            "physics":70,
            "history":80
        }
    }
}}
#dict의 밑에 밑에 구하기
print(samDic['class']['student']['marks']['history'])

samDic2 = {"name": "Kelly","age" : 25,"salary":8000,"city": "new york"}
keys = ["name","salary"]
#키 값으로 값 뽑아서 dic 만들기
newsamDic2 = {k : samDic2[k] for k in keys}
print(newsamDic2)

sampleDict3 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
#키 값으로 제거하기
keysToRemove = ["name", "salary"]
newsamdic3 = {k: sampleDict3[k] for k in sampleDict3.keys()-keysToRemove}
print(newsamdic3)

sampleDict4 = {'a': 100, 'b': 200, 'c': 300}
print(200 in sampleDict4.values())

#키값 변경하기
sampleDict5 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sampleDict5['location'] = sampleDict5.pop('city')
print(sampleDict5)

#최소값 찾아내기
sampleDict6 = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(min(sampleDict6, key=sampleDict6.get))

def calc(operation, *nums):
    sum = 0
    for num in nums:
        if operation == "+":
            sum += num
        elif operation =="*":
            if sum == 0:
                sum =1
            sum *= num
    return  sum
sum = calc("*",1,2,3,4,5)
print(sum)

def test(end):
    if end ==0:
        return
    print('재귀함수')
    end -= 1
    test(end)
test(5)
#알고 있는 값에서 update
sampleDict6 = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}
sampleDict6['emp3']['salary'] = 8500
print(sampleDict6)

def f_sum(n):
    if n==0:
        return 0
    return n + f_sum(n-1)
print(f_sum(5))
#이거 중요!! 제일 마지막부터 나옴
def f_number(na):
    if na == 0:
        return
#재귀 함수를 앞에 두고 프린트를 하면 앞에서 나옴
    f_number(int(na/10))
    print(na%10)

f_number(1234)
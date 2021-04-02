plus_ten = lambda x: x+10
print(plus_ten(1))
print((lambda x: x+10)(1))

a=[1,2,3,4,5,6,7,8,9,10]
def f(x):
    if x % 2 == 0:
        return 0
    else:
        return x
list(map(f,a))

# 짝수 면 0이고 아니면 x를 반환
list(map(lambda x:0 if x % 2 == 0 else x,a ))
#람다 조건식 결과 if 조건식 else 결과 2 if 조건식2 else 결과 3
(lambda x: x+10)(1)

#람다를 이용하여 키 값 및 벨류값 구하기
score ={'이름':'강다영','수학':80,'과학':70}
keys = list(map(lambda x : x, score))
values = list(map(lambda x : score[x],score))
#맵은 갯수가 변화지 않음
a=[1,2,3,4,5,6,7,8,9,10]
list(map(lambda x:2 if x%2==0 else 3 if x%3 ==0 else 1,a))
#필터는 양이 줄어듬 -걸리지기 때문에
ax=[2,6,4,3,6,8,3,9,6]
list(filter(lambda  x: x>2 and x<8,ax))

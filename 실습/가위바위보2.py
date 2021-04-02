<<<<<<< HEAD
import random #random
x = 1
total = 0
win = 0
sc =["가위","바위","보"]
while x in [1,2,3]:
    y=random.randint(1,3)
    print()
    x=int(input("가위(1),바위(2),보(3)을 입력해주세요"))
    if x in [1,2,3]:
        print("유저 : ",end=" ")
        print(sc[x-1],end=" ")
        print(",컴퓨터 :",end=" ")
        print(sc[y-1],end=" ")
        if x != y:
            if x == y+1:
                win += 1
            elif x == 1 and y == 3:
                win += 1
        total += 1
print("게임종료 (전체:{} ,승리:{})".format(total,win))

import pickle
SaveT = total
SaveW = win

with open("data3.pkl","wb") as file:
    pickle.dump(SaveT,file)
    pickle.dump(SaveW,file)

with open("data.pkl","rb") as file:
    total = SaveT
    win = SaveW


con = int(input("게임을 다시 하고 싶으면 0을 누르시오"))
if con== 0:
    x = 1
    sc =["가위","바위","보"]
    while x in [1,2,3]:
        y=random.randint(1,3)
        print()
        x=int(input("가위(1),바위(2),보(3)을 입력해주세요"))
        if x in [1,2,3]:
            print("유저 : ",end=" ")
            print(sc[x-1],end=" ")
            print(",컴퓨터 :",end=" ")
            print(sc[y-1],end=" ")
            if x != y:
                if x == y+1:
                    win += 1
                elif x == 1 and y == 3:
                    win += 1
            total += 1
    print("게임종료 (전체:{} ,승리:{})".format(total,win))
=======
import random #random
x = 1
total = 0
win = 0
sc =["가위","바위","보"]
while x in [1,2,3]:
    y=random.randint(1,3)
    print()
    x=int(input("가위(1),바위(2),보(3)을 입력해주세요"))
    if x in [1,2,3]:
        print("유저 : ",end=" ")
        print(sc[x-1],end=" ")
        print(",컴퓨터 :",end=" ")
        print(sc[y-1],end=" ")
        if x != y:
            if x == y+1:
                win += 1
            elif x == 1 and y == 3:
                win += 1
        total += 1
print("게임종료 (전체:{} ,승리:{})".format(total,win))

import pickle
SaveT = total
SaveW = win

with open("data3.pkl","wb") as file:
    pickle.dump(SaveT,file)
    pickle.dump(SaveW,file)

with open("data.pkl","rb") as file:
    total = SaveT
    win = SaveW


con = int(input("게임을 다시 하고 싶으면 0을 누르시오"))
if con== 0:
    x = 1
    sc =["가위","바위","보"]
    while x in [1,2,3]:
        y=random.randint(1,3)
        print()
        x=int(input("가위(1),바위(2),보(3)을 입력해주세요"))
        if x in [1,2,3]:
            print("유저 : ",end=" ")
            print(sc[x-1],end=" ")
            print(",컴퓨터 :",end=" ")
            print(sc[y-1],end=" ")
            if x != y:
                if x == y+1:
                    win += 1
                elif x == 1 and y == 3:
                    win += 1
            total += 1
    print("게임종료 (전체:{} ,승리:{})".format(total,win))
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62

<<<<<<< HEAD
import pickle
start = int(input("메뉴를 선택해주세요 1-입력,2-조회,3-삭제,0-종료:"))
totallist=[[],[],[],[]]
i = 0
while True:
    if start == 1 and i == 0:
        print("입력값을 입력해주세요")
        name= input("이름 : ")
        math = int(input("수학 : "))
        science = int(input("과학 : "))
        english = int(input("영어 : "))
        totallist[0].append(name)
        totallist[1].append(math)
        totallist[2].append(science)
        totallist[3].append(english)
        with open("data12.pickle","wb") as file:
            pickle.dump(totallist,file)
        i += 1
    elif start == 1 and i>0:
        with open("data12.pickle", "rb") as file:
            totallist = pickle.load(file)
        print("입력값을 입력해주세요")
        name = input("이름 : ")
        math = int(input("수학 : "))
        science = int(input("과학 : "))
        english = int(input("영어 : "))
        totallist[0].append(name)
        totallist[1].append(math)
        totallist[2].append(science)
        totallist[3].append(english)

        with open("data12.pickle","wb") as file:
            pickle.dump(totallist,file)
        i += 1
    elif start == 2 and i > 0: #조회
        with open("data12.pickle","rb") as file:
            totallist = pickle.load(file)
        for x in range(i):
            print("[{}] 이름 : {} 수학 : {} 과학 : {}".format(x,totallist[0][x],totallist[1][x],totallist[2][x],totallist[3][x] ))
    elif start == 2 and i ==0:
        print("입력한 값이 없자나!!! 뭘 조회를 하냐?")
    elif start == 3 and i > 0:#삭제
        with open("data12.pickle", "rb")as file:
            totallist = pickle.load(file)
        delx = int(input("삭제할 번호를 입력해주세요"))
        totallist[0].pop(delx)
        totallist[1].pop(delx)
        totallist[2].pop(delx)
        totallist[3].pop(delx)
        i -= 1
        with open("data12.pickle","wb") as file:
            pickle.dump(totallist,file)
        print("삭제가 완료되었습니다.")
    elif start == 3 and i ==0:
        print("입력한 값이 없자나!!! 뭘 삭제를 하냐")
    elif start == 0:
        print("종료되었습니다.")
        break
    else:
        print("잘못된 숫자입니다. 다른 숫자를 입력해주세요!!")

=======
import pickle
start = int(input("메뉴를 선택해주세요 1-입력,2-조회,3-삭제,0-종료:"))
totallist=[[],[],[],[]]
i = 0
while True:
    if start == 1 and i == 0:
        print("입력값을 입력해주세요")
        name= input("이름 : ")
        math = int(input("수학 : "))
        science = int(input("과학 : "))
        english = int(input("영어 : "))
        totallist[0].append(name)
        totallist[1].append(math)
        totallist[2].append(science)
        totallist[3].append(english)
        with open("data12.pickle","wb") as file:
            pickle.dump(totallist,file)
        i += 1
    elif start == 1 and i>0:
        with open("data12.pickle", "rb") as file:
            totallist = pickle.load(file)
        print("입력값을 입력해주세요")
        name = input("이름 : ")
        math = int(input("수학 : "))
        science = int(input("과학 : "))
        english = int(input("영어 : "))
        totallist[0].append(name)
        totallist[1].append(math)
        totallist[2].append(science)
        totallist[3].append(english)

        with open("data12.pickle","wb") as file:
            pickle.dump(totallist,file)
        i += 1
    elif start == 2 and i > 0: #조회
        with open("data12.pickle","rb") as file:
            totallist = pickle.load(file)
        for x in range(i):
            print("[{}] 이름 : {} 수학 : {} 과학 : {}".format(x,totallist[0][x],totallist[1][x],totallist[2][x],totallist[3][x] ))
    elif start == 2 and i ==0:
        print("입력한 값이 없자나!!! 뭘 조회를 하냐?")
    elif start == 3 and i > 0:#삭제
        with open("data12.pickle", "rb")as file:
            totallist = pickle.load(file)
        delx = int(input("삭제할 번호를 입력해주세요"))
        totallist[0].pop(delx)
        totallist[1].pop(delx)
        totallist[2].pop(delx)
        totallist[3].pop(delx)
        i -= 1
        with open("data12.pickle","wb") as file:
            pickle.dump(totallist,file)
        print("삭제가 완료되었습니다.")
    elif start == 3 and i ==0:
        print("입력한 값이 없자나!!! 뭘 삭제를 하냐")
    elif start == 0:
        print("종료되었습니다.")
        break
    else:
        print("잘못된 숫자입니다. 다른 숫자를 입력해주세요!!")

>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
    start = int(input("메뉴를 선택해주세요 1-입력,2-조회,3-삭제,0-종료:"))
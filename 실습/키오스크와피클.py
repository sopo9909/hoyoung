<<<<<<< HEAD
import pickle
start = int(input("메뉴를 선택해주세요 1-입력,2-조회,3-삭제,0-종료:"))
totallist=[]
namelist=[]
mathlist = []
sciencelist =[]
englisthlist =[]
namelist2=[]
mathlist2 = []
sciencelist2 =[]
englisthlist2 =[]

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
        with open("data11.pickle","wb") as file:
            pickle.dump(namelist,file)
            pickle.dump(mathlist,file)
            pickle.dump(sciencelist,file)
            pickle.dump(englisthlist,file)
        i += 1
    elif start == 1 and i>0:
        with open("data11.pickle", "rb"):
            namelist2 = pickle.load(file)
            mathlist2 = pickle.load(file)
            sciencelist2 = pickle.load(file)
            englisthlist2 = pickle.load(file)
        print("입력값을 입력해주세요")
        name = input("이름 : ")
        math = int(input("수학 : "))
        science = int(input("과학 : "))
        english = int(input("영어 : "))
        namelist2.append(name)
        mathlist2.append(math)
        sciencelist2.append(science)
        englisthlist2.append(english)

        with open("data11.pickle","wb") as file:
            pickle.dump(namelist2, file)
            pickle.dump(mathlist2, file)
            pickle.dump(sciencelist2, file)
            pickle.dump(englisthlist2, file)
        i += 1
    elif start == 2 and i > 0: #조회
        with open("data11.pickle","rb"):
            namelist2 = pickle.load(file)
            mathlist2 = pickle.load(file)
            sciencelist2 = pickle.load(file)
            englisthlist2 = pickle.load(file)
        for x in range(i+1):
            print(x,end=" ")
            print(namelist2[x],end=" ")
            print(mathlist2[x], end=" ")
            print(sciencelist2[x], end=" ")
            print(englisthlist2[x], end=" ")
    elif start == 2 and i ==0:
        print("입력한 값이 없자나!!! 뭘 조회를 하냐?")
    elif start == 3 and i > 0:#삭제
        with open("data11.pickle", "rb"):
            namelist2 = pickle.load(file)
            mathlist2 = pickle.load(file)
            sciencelist2 = pickle.load(file)
            englisthlist2 = pickle.load(file)
        delx = int(input("삭제할 번호를 입력해주세요"))
        namelist.pop(delx)
        mathlist.pop(delx)
        sciencelist.pop(delx)
        englisthlist.pop(delx)
        i -= 1
        with open("data11.pickle","wb") as file:
            pickle.dump(namelist,file)
            pickle.dump(mathlist,file)
            pickle.dump(sciencelist,file)
            pickle.dump(englisthlist,file)
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
totallist=[]
namelist=[]
mathlist = []
sciencelist =[]
englisthlist =[]
namelist2=[]
mathlist2 = []
sciencelist2 =[]
englisthlist2 =[]

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
        with open("data11.pickle","wb") as file:
            pickle.dump(namelist,file)
            pickle.dump(mathlist,file)
            pickle.dump(sciencelist,file)
            pickle.dump(englisthlist,file)
        i += 1
    elif start == 1 and i>0:
        with open("data11.pickle", "rb"):
            namelist2 = pickle.load(file)
            mathlist2 = pickle.load(file)
            sciencelist2 = pickle.load(file)
            englisthlist2 = pickle.load(file)
        print("입력값을 입력해주세요")
        name = input("이름 : ")
        math = int(input("수학 : "))
        science = int(input("과학 : "))
        english = int(input("영어 : "))
        namelist2.append(name)
        mathlist2.append(math)
        sciencelist2.append(science)
        englisthlist2.append(english)

        with open("data11.pickle","wb") as file:
            pickle.dump(namelist2, file)
            pickle.dump(mathlist2, file)
            pickle.dump(sciencelist2, file)
            pickle.dump(englisthlist2, file)
        i += 1
    elif start == 2 and i > 0: #조회
        with open("data11.pickle","rb"):
            namelist2 = pickle.load(file)
            mathlist2 = pickle.load(file)
            sciencelist2 = pickle.load(file)
            englisthlist2 = pickle.load(file)
        for x in range(i+1):
            print(x,end=" ")
            print(namelist2[x],end=" ")
            print(mathlist2[x], end=" ")
            print(sciencelist2[x], end=" ")
            print(englisthlist2[x], end=" ")
    elif start == 2 and i ==0:
        print("입력한 값이 없자나!!! 뭘 조회를 하냐?")
    elif start == 3 and i > 0:#삭제
        with open("data11.pickle", "rb"):
            namelist2 = pickle.load(file)
            mathlist2 = pickle.load(file)
            sciencelist2 = pickle.load(file)
            englisthlist2 = pickle.load(file)
        delx = int(input("삭제할 번호를 입력해주세요"))
        namelist.pop(delx)
        mathlist.pop(delx)
        sciencelist.pop(delx)
        englisthlist.pop(delx)
        i -= 1
        with open("data11.pickle","wb") as file:
            pickle.dump(namelist,file)
            pickle.dump(mathlist,file)
            pickle.dump(sciencelist,file)
            pickle.dump(englisthlist,file)
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
<<<<<<< HEAD
dic1 = {}
menu = int(input("메뉴를 선택해주세요 (1-입력, 2-조회, 3-삭제, 0-종료) : "))
i = 0
while True:
    if menu ==0:
        print("종료 되었습니다.")
        break
    elif menu ==1:
        name = input("이름 : ")
        math = input("수학 : ")
        science = input("과학 : ")
        english = input("영어 : ")
        dic1.setdefault(i,{"이름" :name,"수학":math,"과학":science,"영어":english})
        i+=1
    elif menu == 2:
        print(dic1)
    elif menu == 3:
        delx = int(input("삭제하고 싶은 곳을 적어주세요"))
        dic1.pop(delx)
=======
dic1 = {}
menu = int(input("메뉴를 선택해주세요 (1-입력, 2-조회, 3-삭제, 0-종료) : "))
i = 0
while True:
    if menu ==0:
        print("종료 되었습니다.")
        break
    elif menu ==1:
        name = input("이름 : ")
        math = input("수학 : ")
        science = input("과학 : ")
        english = input("영어 : ")
        dic1.setdefault(i,{"이름" :name,"수학":math,"과학":science,"영어":english})
        i+=1
    elif menu == 2:
        print(dic1)
    elif menu == 3:
        delx = int(input("삭제하고 싶은 곳을 적어주세요"))
        dic1.pop(delx)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
    menu = int(input("메뉴를 선택해주세요 (1-입력, 2-조회, 3-삭제, 0-종료) : "))
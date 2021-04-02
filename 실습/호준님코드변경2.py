<<<<<<< HEAD
new_list = []
while True:
    a = int(input("메뉴 선택 1-입력,2-조회,3-삭제,0-종료 : "))
    if a==1 :
        name = input("이름 : ")
        math = input("수학 : ")
        science = input("과학 : ")
        english = input("영어 : ")
        new = ("이름 : {}, 수학 : {}, 과학 : {}, 영어 : {}".format(name,math,science,english))
        new_list.append(new)
    elif a==2 :
        print(new_list)
    elif a ==3:
        print(new_list)
        b = int(input("삭제할 번호를 입력해주세요"))
        new_list.pop(b)
        print('삭제가 완료되었습니다.')
    else :
=======
new_list = []
while True:
    a = int(input("메뉴 선택 1-입력,2-조회,3-삭제,0-종료 : "))
    if a==1 :
        name = input("이름 : ")
        math = input("수학 : ")
        science = input("과학 : ")
        english = input("영어 : ")
        new = ("이름 : {}, 수학 : {}, 과학 : {}, 영어 : {}".format(name,math,science,english))
        new_list.append(new)
    elif a==2 :
        print(new_list)
    elif a ==3:
        print(new_list)
        b = int(input("삭제할 번호를 입력해주세요"))
        new_list.pop(b)
        print('삭제가 완료되었습니다.')
    else :
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
        print("종료")
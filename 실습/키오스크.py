<<<<<<< HEAD
import pickle
#if scores.pkl 있는지 체크
scores = [{"이름":"이민호","수학":60,"과학":90,"영어":100}]
while True:
    menu = input("메뉴를 선택해주세요")
    if menu == "1":
        name = input("이름")
        math = input("수학")
        science = input("과학")
        english = input("영어")
        student ={"이름":name, "수학":math, "과학":science,"영어":english}
        scores.append(student)
    elif menu == "2":
        with open("scores.pkl","rb") as f:
            scores = pickle.load(f)
    elif menu == "3":

    elif menu == "0":
        print("종료합니다")
        with open("scores.pkl", "wb") as f:
            pickle.dump(scores,f)
=======
import pickle
#if scores.pkl 있는지 체크
scores = [{"이름":"이민호","수학":60,"과학":90,"영어":100}]
while True:
    menu = input("메뉴를 선택해주세요")
    if menu == "1":
        name = input("이름")
        math = input("수학")
        science = input("과학")
        english = input("영어")
        student ={"이름":name, "수학":math, "과학":science,"영어":english}
        scores.append(student)
    elif menu == "2":
        with open("scores.pkl","rb") as f:
            scores = pickle.load(f)
    elif menu == "3":

    elif menu == "0":
        print("종료합니다")
        with open("scores.pkl", "wb") as f:
            pickle.dump(scores,f)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
        break
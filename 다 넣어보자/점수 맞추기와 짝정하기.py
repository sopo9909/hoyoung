numbers = [12,32,55,12,32,4,86,50]
print(list(map(lambda x:"합격" if x>60 else "대기"if x>50 else "불합격",numbers)))
a=[1,2,3,4,5,6,7,8,9,10]
list(map(lambda x : 0 if x%2==0 else 0 if x%3==0 else x,a))
print(list(map(lambda x : 0 if x%2==0 else 0 if x%3==0 else x,a)))

def find(x):
    a = x.split(".")
    if "jpg" in a:
        return x
    else:
        pass
import random
files=["memo.txt","1.jpg","32.png","23.jpg","223.jpg"]
print(list(filter(lambda x: find(x),files)))

print(list(filter(lambda x: x.find(".jpg") > -1,files)))

student = [["강다영",1,2],["강동아",2,1],["권윤택",3,0],["김광희",4,14],["김기범",5,21],["김성희",6,12],["김수진",7,16],["김태익",8,0],["남윤호",9,0],
           ["박수진",10,13],["박창서",11,0],["선은빈",12,6],["송은이",13,10],["우지원",14,4],["윤현수",15,17],["윤호준",16,7],["이송재",17,15],["이한비",18,20],["조계철",19,0],
           ["최하은",20,18],["황호영",21,5],["조성혜",22,0]]
con = 0
new=[[],[],[],[],[],[],[],[],[],[],[]]

while len(student) !=0:
    a= random.randint(0,len(student)-1)
    b = random.randint(0,len(student)-1)
    if a != b:
        if student[a][1]==student[b][2]:
            #이전짝
            continue
        elif student[a][1]!=student[b][2] and a>b:
            new[con]=[student[a][0],student[b][0]]
            student.pop(b)
            student.pop(a-1)
            con += 1
        elif student[a][1]!=student[b][2] and b>a:
            new[con] = [student[a][0], student[b][0]]
            student.pop(a)
            student.pop(b-1)
            con += 1
    else:
        pass

print(new)

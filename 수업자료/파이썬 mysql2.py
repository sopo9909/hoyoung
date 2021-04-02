<<<<<<< HEAD
import pymysql
db = pymysql.connect(host='127.0.0.1', port=3306, user='Hoyoung', passwd='1234', db='w3schools', use_unicode=True, charset='utf8')
# cursor =db.cursor
# sql ="select * from customers"
# cursor.execute(sql)
# resultset = cursor.fetchall()
# print(resultset)

# cursor = db.cursor(pymysql.cursors.DictCursor)
# sql ="select * from customers where country =%s"
# cursor.execute(sql,'UK')
# rs = cursor.fetchall()
# print(rs)

# cursor = db.cursor(pymysql.cursors.DictCursor)
# sql ="select * from customers where country =%s"
# cursor.execute(sql,'UK')
# resultset = cursor.fetchone()
# print(resultset)

check=show table like 'scores1'
curs.execute(check)
result = curs.fetchall()
if len(result) ==1:
    sql="""
    DROP TABLE scores1
    """
    cursor=db.cursor()
    cursor.execute(sql)
    db.commit()
sql="""
CREATE TABLE scores1(
Id Int Not null auto_increment,
Name varchar(20) NOT NULL,
Math INT NULL,
Science INT NULL,
English INT NULL,
PRIMARY KEY (Id)
)
"""
cursor=db.cursor()
cursor.execute(sql)
db.commit()
while True:
    a= input("메뉴를 선택해주세요 1 - 입력, 2 - 조회, 3 - 삭제, 0 - 종료) : ")
    if a=='1':
        name = input("이름 : ")
        math = input("수학 : ")
        science = input("과학 : ")
        english = input("영어 : ")
        sql= "Insert into scores1 (Name,Math,Science,English) Values ('{}','{}','{}','{}')".format(name,math,science,english)
        cursor.execute(sql)
        db.commit()
    elif a =='2':
        sql="""
        Select * From scores1
        """
        cursor.execute(sql)
        re = cursor.fetchall()
        for row in re:
            print("[{}] 이름: {} 수학: {} 과학: {} 영어: {}".format(row[0],row[1],row[2],row[3],row[4]))
    elif a=='3':
        del1 = int(input("삭제할 인덱스을 불러주세요 : "))
        sql="DELETE FROM scores1 WHERE Id= {}".format(del1)
        cursor.execute(sql)
        db.commit()
    elif a=='0':
        print("종료되었습니다")
        break
    else:
=======
import pymysql
db = pymysql.connect(host='127.0.0.1', port=3306, user='Hoyoung', passwd='1234', db='w3schools', use_unicode=True, charset='utf8')
# cursor =db.cursor
# sql ="select * from customers"
# cursor.execute(sql)
# resultset = cursor.fetchall()
# print(resultset)

# cursor = db.cursor(pymysql.cursors.DictCursor)
# sql ="select * from customers where country =%s"
# cursor.execute(sql,'UK')
# rs = cursor.fetchall()
# print(rs)

# cursor = db.cursor(pymysql.cursors.DictCursor)
# sql ="select * from customers where country =%s"
# cursor.execute(sql,'UK')
# resultset = cursor.fetchone()
# print(resultset)

check=show table like 'scores1'
curs.execute(check)
result = curs.fetchall()
if len(result) ==1:
    sql="""
    DROP TABLE scores1
    """
    cursor=db.cursor()
    cursor.execute(sql)
    db.commit()
sql="""
CREATE TABLE scores1(
Id Int Not null auto_increment,
Name varchar(20) NOT NULL,
Math INT NULL,
Science INT NULL,
English INT NULL,
PRIMARY KEY (Id)
)
"""
cursor=db.cursor()
cursor.execute(sql)
db.commit()
while True:
    a= input("메뉴를 선택해주세요 1 - 입력, 2 - 조회, 3 - 삭제, 0 - 종료) : ")
    if a=='1':
        name = input("이름 : ")
        math = input("수학 : ")
        science = input("과학 : ")
        english = input("영어 : ")
        sql= "Insert into scores1 (Name,Math,Science,English) Values ('{}','{}','{}','{}')".format(name,math,science,english)
        cursor.execute(sql)
        db.commit()
    elif a =='2':
        sql="""
        Select * From scores1
        """
        cursor.execute(sql)
        re = cursor.fetchall()
        for row in re:
            print("[{}] 이름: {} 수학: {} 과학: {} 영어: {}".format(row[0],row[1],row[2],row[3],row[4]))
    elif a=='3':
        del1 = int(input("삭제할 인덱스을 불러주세요 : "))
        sql="DELETE FROM scores1 WHERE Id= {}".format(del1)
        cursor.execute(sql)
        db.commit()
    elif a=='0':
        print("종료되었습니다")
        break
    else:
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
        print("아니 이딴 걸 입력하냐???")
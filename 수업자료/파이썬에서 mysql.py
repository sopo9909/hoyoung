<<<<<<< HEAD
import pymysql
db = pymysql.connect(host='127.0.0.1', port=3306, user='Hoyoung', passwd='1234', db='classicmodels', use_unicode=True, charset='utf8')

cursor =db.cursor()
sql = """
    SELECT country , count(employeeNumber) from offices inner join employees on offices.officeCode = employees.officeCode group by country order by country  
"""
cursor.execute(sql)
resultset = cursor.fetchall()
for resultone in resultset:
=======
import pymysql
db = pymysql.connect(host='127.0.0.1', port=3306, user='Hoyoung', passwd='1234', db='classicmodels', use_unicode=True, charset='utf8')

cursor =db.cursor()
sql = """
    SELECT country , count(employeeNumber) from offices inner join employees on offices.officeCode = employees.officeCode group by country order by country  
"""
cursor.execute(sql)
resultset = cursor.fetchall()
for resultone in resultset:
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
    print("국가 : {} , 직원수 : {}".format(resultone[0],resultone[1]))
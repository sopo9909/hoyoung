import pymysql
import csv

conn =pymysql.connect(host='localhost',user='root',password='1234',db='hyundei',charset='utf8')
curs = conn.cursor()
sql = "insert into db (custid,date_time,store,product,corner,pc,part,imported,amount,discount,installment,gender,sector,sector_name,temp,Rain,vip,date,action) values (%d,%s,%s,%d,%s,%s,%s,%d,%d,%d,%d,%d,%d,%s,%f,%f,%s,%s,%d)"
f=open('final0209.csv','r',encoding='utf-8')
rd = csv.reader(f)
i =0
for line in rd:
    curs.execute(sql,(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18]))
    i +=1
    if i %100 ==0:
        print(i)
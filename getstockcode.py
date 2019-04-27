import numpy as np
import pandas as pd
import pymysql
import re

filename = 'e:\\download\\shenzhen.txt'
file = open(filename,mode='r',encoding='UTF-8')
text = file.read()
file.close()
print(re.split('\)',text))
mergekeyvalue = re.split('\)',text)
print('\n')
print(type(mergekeyvalue))
conn = pymysql.connect(user="root",password="123456",port=3306,db="mysql",host="localhost",charset="utf8")      #创建数据库连接
cursor = conn.cursor()

sql = "INSERT INTO stock (sname,scode) VALUES (%s,%s)"   #sql语句
templist = []
for verystock in mergekeyvalue:
    tempstock = re.split('\(',verystock)
    # print(tempstock)
    if len(tempstock) > 0 and tempstock[0] and tempstock[1]:
        print(tempstock[0] ,tempstock[1])
        tempturple = (tempstock[0] ,tempstock[1])
        templist.append(tempturple)
cursor.executemany('insert into stock (sname,scode) VALUES (%s,%s)',templist)
conn.commit()
cursor.close()
conn.close()
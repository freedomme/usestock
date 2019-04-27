from selenium import webdriver
import re
import pymysql

def createurl():
    filename = 'e:\\download\\merge.txt'
    file = open(filename,mode='r',encoding='UTF-8')
    text = file.read()
    file.close()
    url_list = []
    mergekeyvalue = re.split('\)',text)
    for verystock in mergekeyvalue:
        tempstock = re.split('\(',verystock)
        if len(tempstock) > 0 and tempstock[0] and tempstock[1]:
            url_list.append('http://aigaogao.com/tools/history.html?s='+tempstock[1])
    return url_list

def createurl_stockcode(stockcode = ''):
    conn = pymysql.connect(user="root", password="123456", port=3306, db="mysql", host="localhost",
                           charset="utf8")  # 创建数据库连接
    cursor = conn.cursor()
    leftStock = "select  scode   from  stock where scode not in(select stockcode from stockmost)  and (scode like '002%'  )  "
    cursor.execute(leftStock)
    resultSet = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    url_list = []
    for verystock in resultSet:
            url_list.append('http://aigaogao.com/tools/history.html?s='+verystock[0])
    # print(url_list)
    return url_list



def str_to_turple(str_content,stockcode):
    # print(str_content)
    str_spilt = str_content.split()
    # print(str_spilt)
    i = 0
    str_turple = []
    for item in str_spilt:
        item = item.replace(',','')
        if i == 1:
            str_turple.append(float(item))
        if i == 2:
            str_turple.append(item)
        if i == 4:
            str_turple.append(float(item))
        if i == 7:
            str_turple.append(float(item))
        if i == 9:
            str_turple.append(float(item))
        if i == 10:
            str_turple.append(item)
        if i == 16:
            str_turple.append(float(item)) #最大成交金额
        if i == 17:
            str_turple.append(item)
        if i == 27:
            str_turple.append(float(item))
        if i == 28:
            str_turple.append(item)
        if i == 33:
            str_turple.append(int(re.findall('\d+',item)[0]))
            if int(re.findall('\d+',item)[1]) > 1:
                str_turple.append("".join(str_spilt[34: 34 + 2*(int(re.findall('\d+',item)[1])) - 1]))
                for j in range(2*(int(re.findall('\d+',item)[1])) - 2):
                    del str_spilt[34]
                str_spilt[34] = ''
        if i == 34:
            if(len(item) == 10):
                str_turple.append(item)
        if i == 35:
            str_turple.append(int(re.findall('\d+',item)[0]))
            if int(re.findall('\d+', item)[1]) > 1:
                str_turple.append("".join(str_spilt[36: 36 + 2 * (int(re.findall('\d+', item)[1])) - 1]))
                for j in range(2 * (int(re.findall('\d+', item)[1])) - 2):
                    del str_spilt[36]
                str_spilt[36] = ''
        if i == 36:
            if (len(item) == 10):
                str_turple.append(item)
        i = i + 1
    # print(str_turple)
    str_turple.append(stockcode)
    return str_turple

def str_to_list(str_content  , stockcode):
    sql_list = []
    strlist = str_content.split('\n')
    del strlist[0]
    for item in strlist:
        temp_item = item.split()
        if int(stockcode) < 600000 and len(temp_item) == 15: # 深市股票
            del temp_item[14]
            del temp_item[12]
            del temp_item[11]
            del temp_item[9]

            # del temp_item[14]
            # del temp_item[13]
            # del temp_item[12]
            # del temp_item[9]
            temp_item[5] = temp_item[5].replace(',','')
            temp_item[6] = temp_item[6].replace(',', '')
            temp_item.append(stockcode)
            sql_list.append(temp_item)
        if int(stockcode) >= 600000 and len(temp_item) == 15: #上市股票
            del temp_item[14]
            del temp_item[13]
            del temp_item[12]
            del temp_item[9]
            temp_item[5] = temp_item[5].replace(',','')
            temp_item[6] = temp_item[6].replace(',', '')
            temp_item.append(stockcode)
            sql_list.append(temp_item)
        if int(stockcode) >= 600000 and len(temp_item) == 14: #上市股票
            del temp_item[13]
            del temp_item[12]
            del temp_item[11]
            temp_item[9] = 0
            temp_item[5] = temp_item[5].replace(',', '')
            temp_item[6] = temp_item[6].replace(',', '')
            temp_item[10] = float(temp_item[10])
            temp_item.append(stockcode)
            sql_list.append(temp_item)
            # print(temp_item)
    return sql_list



def insert_stock_most(sql_list):
    conn = pymysql.connect(user="root", password="123456", port=3306, db="mysql", host="localhost", charset="utf8")  # 创建数据库连接
    cursor = conn.cursor()
    # sqlstockmost = "INSERT INTO  stockmost (highest, highestday, avgupdowndiff, avgdealamount, lowest, lowestday, mostdealamount, mostdealamountday,  leastamount, leastday, mostupdayacount, mostupdayacountday, mostdowndayacount, mostdowndayacountday,stockcode ) \
    # VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s) "

    sqlstockmost = "INSERT INTO  stockmostadd (highest, highestday, avgupdowndiff, avgdealamount, lowest, lowestday, mostdealamount, mostdealamountday,  leastamount, leastday, mostupdayacount, mostupdayacountday, mostdowndayacount, mostdowndayacountday,stockcode ) \
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s) "

    cursor.execute(sqlstockmost,sql_list)
    conn.commit()
    cursor.close()
    conn.close()

def insert_stock_day(sql_list):
    print(sql_list)
    conn = pymysql.connect(user="root", password="123456", port=3306, db="mysql", host="localhost", charset="utf8")  # 创建数据库连接
    cursor = conn.cursor()
#     sqlstockday = "INSERT INTO stockday \
# (day, startbuy, highest, lowest,closebuy, dealvolum, dealamount,  updownamount, updownper, shrink, highlowdiff, stockcode) \
# VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

    sqlstockday = "INSERT INTO stockdayadd \
    (day, startbuy, highest, lowest,closebuy, dealvolum, dealamount,  updownamount, updownper, shrink, highlowdiff, stockcode) \
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

    cursor.executemany(sqlstockday,sql_list)
    conn.commit()
    cursor.close()
    conn.close()

driver = webdriver.Chrome()
driver.maximize_window()
geturl = createurl_stockcode()
for veryurl in geturl:
    # if int(veryurl[-6:]) < 203055 or (int(veryurl[-6:]) > 300760 and int(veryurl[-6:]) < 600000):
    #     continue
    # driver.get("http://aigaogao.com/tools/history.html?s=204003")
    driver.get(veryurl)
    driver.implicitly_wait(10)
    try:
        strout1 = driver.find_element_by_id('ctl16_summarydiv')
        most_list = str_to_turple(strout1.text,veryurl[-6:])
        insert_stock_most(most_list)
        # strout2 = driver.find_element_by_id('ctl16_contentdiv')
        # day_list = str_to_list(strout2.text,veryurl[-6:])
        # insert_stock_day(day_list)
    except:
        # traceback.print_exc()
        print('发生异常代号' + veryurl)

    # driver.close()

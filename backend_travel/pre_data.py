
import pymysql

def get_name():
    name_lis = []
    db = pymysql.connect("192.168.8.105","weibospider","wangwang","lab")
    cursor = db.cursor()
    sql = 'select name from national_museum'
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        name_lis.append(row[0])
    return name_lis

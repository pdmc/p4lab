
import pymysql

def get_name():
    name_lis = []
    #db = pymysql.connect("192.168.8.105","weibospider","wangjipeng","p4lab")
    db = pymysql.connect("101.236.16.93","pk4yo","f23kKF34Q3r9","p4lab",charset='utf8')
    cursor = db.cursor()
    sql = 'select name from national_museum'
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        name_lis.append(row[0])
    return name_lis

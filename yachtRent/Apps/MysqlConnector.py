import pymysql
import os
from Apps.models import response


def get_all(database, sql, args):
    conn = pymysql.connect(host='localhost', user='root', passwd='spln13spln', db=database, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return result_list


def get_one(database, sql, args):
    conn = pymysql.connect(host='localhost', user='root', passwd='spln13spln', db=database, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def modify(database, sql, args):
    conn = pymysql.connect(host='localhost', user='root', passwd='spln13spln', db=database, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()


def dump(request):
    key = "spln13spln"
    path = "/Users/linan/Code/database"
    os.system("mysqldump -uroot -p%s YachtClub > %s.sql" % (key, path))
    return response({"code": 1})

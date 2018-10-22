import pymysql
from consts import HOSTNAME, DATABASE, USERNAME, PASSWORD

con = pymysql.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)

with con as cur:
    cur.execute('drop table if exists users')
    cur.execute('create table users(Id INT PRIMARY KEY AUTO_INCREMENT, '
                'Name VARCHAR(25))')
    cur.execute("insert into users(Name) values('xiaoming')")
    cur.execute("insert into users(Name) values('wanglang')")
    cur.execute('select * from users')

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute('update users set Name=%s where Id=%s', ('ming',1))
    print('Number of rows updated:', cur.rowcount)

    cur = con.cursor(pymysql.cursors.DictCursor)
    cur.execute('select * from users')

    rows = cur.fetchall()
    for row in rows:
        print(row['Id'], row['Name'])
from sqlalchemy import create_engine
from consts import DB_URI

eng = create_engine(DB_URI)
with eng.connect() as conn:
    conn.execute('drop table if exists users')
    conn.execute('create table users(Id INT PRIMARY KEY AUTO_INCREMENT, '
                'Name VARCHAR(25))')
    conn.execute("insert into users(name) values('xiaoming')")
    conn.execute("insert into users(name) values('wanglang')")
    rs = conn.execute('select * from users')
    for row in rs:
        print(row)
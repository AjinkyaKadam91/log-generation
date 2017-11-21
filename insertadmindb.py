import sqlite3 as lite

conn=lite.connect('ADMIN.sqlite')

conn.execute("INSERT INTO ADMIN (ID,NAME,AGE,USERID,PASSWORD) \
      VALUES (2, 'Ajinkya', 23, '12345', 'password' )");

conn.commit()
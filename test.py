__author__ = '4j!nkya'

import sqlite3
database= 'ADMINISTRATOR.sqlite'
conn = sqlite3.connect(database)
print ("Opened database successfully");

conn.execute("INSERT INTO ADMINISTRATOR (ID,NAME,AGE,USERID,PASSWORD) \
      VALUES (1, 'Paul', 32, '12345', '12345' )");

#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#     VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print ("Records created successfully");
#conn.close()

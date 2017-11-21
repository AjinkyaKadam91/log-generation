import sqlite3 as lite

conn=lite.connect('ADMIN.sqlite')

conn.execute('''CREATE TABLE ADMIN (
		ID INT NOT NULL,
		NAME TEXT NOT NULL,
		AGE INT NOT NULL,
		USERID TEXT NOT NULL,
		PASSWORD TEXT NOT NULL);''')

conn.close()
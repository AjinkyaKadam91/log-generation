import sqlite3
import time
from time import sleep

DB1=sqlite3.connect('LOCOPILOT.sqlite')
DB2=sqlite3.connect('ADMINISTRATOR.sqlite')
DB3=sqlite3.connect('TRAIN.sqlite')
DB4=sqlite3.connect('DEPARTURE.sqlite')

DB1.execute('''CREATE TABLE LOCOPILOT(
		ID INT NOT NULL,
		NAME TEXT NOT NULL,
		AGE INT NOT NULL,
		USERID TEXT NOT NULL,
		PASSWORD TEXT NOT NULL );''')

DB1.close()
time.sleep(1)
print('table created...')
DB2.execute('''CREATE TABLE ADMINISTRATOR(
		ID INT NOT NULL,
		NAME TEXT NOT NULL,
		AGE INT NOT NULL,
		USERID TEXT NOT NULL,
		PASSWORD TEXT NOT NULL);''')

DB2.close()
time.sleep(1)
print('table created...')
DB3.execute('''CREATE TABLE TRAIN(
		ID INT NOT NULL,
		SOURCE TEXT NOT NULL ,
		DESTINATION TEXT NOT NULL,
		VIA TEXT NOT NULL);''')

DB3.close()
time.sleep(1)
print('table created...')
DB4.execute('''CREATE TABLE DEPARTURE(
		USERID TEXT NOT NULL,
		TRAINNO TEXT NOT NULL,
		SOURCE INT NOT NULL,
		DESTINATION TEXT NOT NULL);''')

DB4.close()
time.sleep(1)
print('table created...')

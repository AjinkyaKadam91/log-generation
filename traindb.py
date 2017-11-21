import sqlite3 as lite

conn=lite.connect('TRAIN.sqlite')

for i in range(10):
	a=input('id ')
	b=input('source ')
	c=input('destination ')
	d=input('via ')
	conn.execute("INSERT INTO TRAIN (ID,SOURCE,DESTINATION,VIA) \
    VALUES (?,?,?,?)",(a,b,c,d));
	print("inserted")

conn.commit()
import sqlite3

conn=sqlite3.connect("LOCOPILOT.sqlite")
cur=conn.cursor()
cur.execute("SELECT * FROM LOCOPILOT")

#rows=cur.fetchall()
while True:
	row=cur.fetchone()
	if row== None:
		break
	print(row[0],row[1],row[2],row[3],row[4])
conn.close()
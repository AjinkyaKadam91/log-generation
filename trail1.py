from tkinter import scrolledtext
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk,Image
from tkinter import messagebox as mBox
import datetime
import sys
import sqlite3
import time
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< GLOBAL >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

MAINFRAME=tk.Tk()
MAINFRAME.attributes('-fullscreen',True)

DB1=sqlite3.connect('LOCOPILOT.sqlite')
DB2=sqlite3.connect('ADMIN.sqlite')
DB3=sqlite3.connect('TRAIN.sqlite')
DB4=sqlite3.connect('DEPARTURE.sqlite')

CURSOR1=DB1.cursor()
CURSOR2=DB2.cursor()
CURSOR3=DB3.cursor()
CURSOR4=DB4.cursor()

f=open("log.text","a+")
#----------------------------------------------- functions ----------------------------------

def start():
	FRAME1.place(x=100, y=150)
	BUTTON2.grid(row=0, column=0)
	BUTTON3.grid(row=0, column=1)
	LABEL2.grid(row=1, column=0)
	LABEL3.grid(row=1, column=1)
	f.write("\nopened at "+datetime.datetime.now().strftime(" %H:%M:%S %Y-%m-%d")+'\n')

def login1():
	SUBFRAME=tk.Tk()
	SUBFRAME.title('LogIN Wimdow')
	#SUBFRAME.geometry(500x500)
	LABEL4=tk.Label(SUBFRAME, text='LOGIN ID:')
	LABEL5=tk.Label(SUBFRAME, text='PASSWORD:')
	LABEL4.config(font=('Bookman Old Style',15))
	LABEL5.config(font=('Bookman Old Style',15))
	ENTRY1=tk.Entry(SUBFRAME, width=20, textvariable=V1, bg='#80f0f0')
	ENTRY2=tk.Entry(SUBFRAME, width=20, textvariable=V2, bg='#80f0f0', show='*')
	def log():
		CURSOR2.execute("SELECT userid, password FROM ADMIN")
		record=CURSOR2.fetchall()
		if (ENTRY1.get(),ENTRY2.get()) in record:
			ADMINHOME()
			scr.insert(tk.INSERT, ENTRY1.get()+' logged in at '+time.ctime()+' \n')
			f.write('\n'+ENTRY1.get()+' logged in at '+time.ctime()+'\n')
			SUBFRAME.destroy()
			FRAME1.place_forget()

	BUTTON4=tk.Button(SUBFRAME, text='LogIN', width=10, height=2, bg='#fa8072', command=log)
	LABEL4.grid(row=0, column=0, padx=5, pady=5)
	LABEL5.grid(row=2, column=0, padx=5, pady=5)
	ENTRY1.grid(row=1, column=0, padx=5, pady=5)
	ENTRY2.grid(row=3, column=0, padx=5, pady=5)
	ENTRY1.config(font=('Bookman Old Style',15))
	ENTRY2.config(font=('Bookman Old Style',15))
	BUTTON4.grid(row=4, column=0, padx=5, pady=5)
	ENTRY1.focus()
	SUBFRAME.mainloop()

def login2():
	SUBFRAME=tk.Tk()
	SUBFRAME.title('LogIN Wimdow')
	#SUBFRAME.geometry(500x500)
	LABEL4=tk.Label(SUBFRAME, text='LOGIN ID:')
	LABEL5=tk.Label(SUBFRAME, text='PASSWORD:')
	LABEL4.config(font=('Bookman Old Style',15))
	LABEL5.config(font=('Bookman Old Style',15))
	ENTRY1=tk.Entry(SUBFRAME, width=20, textvariable=V1, bg='#80f0f0')
	ENTRY1.focus()
	ENTRY2=tk.Entry(SUBFRAME, width=20, textvariable=V2, bg='#80f0f0', show='*')
	def log():
		CURSOR1.execute("SELECT userid, password FROM LOCOPILOT")
		record=CURSOR1.fetchall()
		if (ENTRY1.get(),ENTRY2.get()) in record:
			scr.insert(tk.INSERT, ENTRY1.get()+' logged in at '+time.ctime()+' \n')
			f.write('\n'+ENTRY1.get()+' logged in at '+time.ctime()+'\n')
			insert2()
			SUBFRAME.destroy()

	BUTTON4=tk.Button(SUBFRAME, text='LogIN', width=10, height=2, bg='#fa8072', command=log)
	LABEL4.grid(row=0, column=0, padx=5, pady=5)
	LABEL5.grid(row=2, column=0, padx=5, pady=5)
	ENTRY1.grid(row=1, column=0, padx=5, pady=5)
	ENTRY2.grid(row=3, column=0, padx=5, pady=5)
	ENTRY1.config(font=('Bookman Old Style',15))
	ENTRY2.config(font=('Bookman Old Style',15))
	BUTTON4.grid(row=4, column=0, padx=5, pady=5)
	ENTRY1.focus()
	SUBFRAME.mainloop()	

def ADMINHOME():
	FRAME2.place(x=100, y=150)
	BUTTON5.grid(row=0, column=0)
	BUTTON6.grid(row=0, column=1)
	BUTTON10.grid(row=2, column=0)
	LABEL6.grid(row=1, column=0)
	LABEL7.grid(row=1, column=1)
	LABEL18.grid(row=3, column=0)

def insert1():
	FRAME3.place(x=100, y=150)
	ENTRY3.grid(row=1, column=0)
	ENTRY4.grid(row=1, column=1)
	ENTRY5.grid(row=3, column=0)
	ENTRY6.grid(row=3, column=1)
	ENTRY7.grid(row=5, column=0)
	LABEL8.grid(row=0, column=0)
	LABEL9.grid(row=0, column=1)
	LABEL10.grid(row=2, column=0)
	LABEL11.grid(row=2, column=1)
	LABEL12.grid(row=4, column=0)
	BUTTON7.grid(row=5, column=1, pady=5)
	FRAME1.place_forget()
	FRAME2.place_forget()
	

def insert2():
	FRAME3.place(x=100, y=150)
	ENTRY8.grid(row=1, column=0)
	ENTRY9.grid(row=1, column=1)
	ENTRY10.grid(row=3, column=0)
	ENTRY11.grid(row=3, column=1)
#	SPIN1.grid(row=1, column=1)
#	ENTRYBOX1.grid(row=3, column=0)
#	ENTRYBOX2.grid(row=3, column=1)
	LABEL13.grid(row=0, column=0)
	LABEL14.grid(row=0, column=1)
	LABEL15.grid(row=2, column=0)
	LABEL16.grid(row=2, column=1)
	BUTTON8.grid(row=4, columnspan=3, pady=8)
	FRAME1.place_forget()
	FRAME2.place_forget()
#	fetch()

def view1():
	scr.insert(tk.INSERT, ' <'+ENTRY3.get()+' '+ENTRY4.get()+' '+ENTRY5.get()+' '+ENTRY6.get()+' '+ENTRY7.get()+'>\ninserted into database...\n')
	f.write(' \n<'+ENTRY3.get()+' '+ENTRY4.get()+' '+ENTRY5.get()+' '+ENTRY6.get()+' '+ENTRY7.get()+'>\n')
	FRAME1.place(x=100, y=150)
	FRAME3.place_forget()
def view2():
	scr.insert(tk.INSERT, ' <'+ENTRY8.get()+' '+ENTRY9.get()+' '+ENTRY10.get()+' '+ENTRY11.get()+'>\ninserted into database...\n')	
	f.write(' \n<'+ENTRY8.get()+' '+ENTRY9.get()+' '+ENTRY10.get()+' '+ENTRY11.get()+'>\n')
	FRAME1.place(x=100, y=150)
	FRAME3.place_forget()
def loco():
	CURSOR1.execute("INSERT INTO LOCOPILOT VALUES(?,?,?,?,?)",(ENTRY3.get(),ENTRY4.get(),ENTRY5.get(),ENTRY6.get(),ENTRY7.get()))
	view1()
	

def train_detail():
	CURSOR4.execute("INSERT INTO DEPARTURE VALUES(?,?,?,?)",(ENTRY8.get(),ENTRY9.get(),ENTRY10.get(),ENTRY11.get()))
	view2()
	
def view3():
	f=open("log.text","r")
	f1=f.readlines()
	for x in f1:
		scr.insert(tk.INSERT, x)

def clock():
	time = datetime.datetime.now().strftime(" %H:%M:%S %Y-%m-%d ")
	LABEL17.config(text=time)
	LABEL17.place(x=1100, y=5)
	MAINFRAME.after(1000, clock)

def reset():
	FRAME1.place()
	FRAME2.place_forget()
	FRAME3.place_forget()

def _spin():
	print(var1,var2,var3)
	scr.insert(tk.INSERT, ' '+var1+' '+var2+' '+var3)
	
def exit():
	MAINFRAME.destroy()

def trainlist():
	CURSOR3.execute("select * from TRAIN")
	row=CURSOR3.fetchall()
	for i in row:
		print(i[0],i[1]+' to '+i[2]+' via '+ i[3])
		scr.insert(tk.INSERT, str(i[0])+' '+i[1]+' to '+i[2]+' via '+i[3]+'\n')

#def fetch():
#	CURSOR3.execute("SELECT id, source, destination  FROM TRAIN")
#	record=CURSOR1.fetchall()
#	if (var2, var3) in record and SPIN1.get()==record[0]:
#		ENTRYBOX1.insert(tk.INSERT, record[1])
#		ENTRYBOX2.insert(tk.INSERT, record[2])

path="train.jpg"
img=ImageTk.PhotoImage(Image.open(path))
panel=tk.Label(MAINFRAME, image=img)
panel.pack(side='bottom', fill='both', expand='yes')

FRAME1=tk.LabelFrame(MAINFRAME, fg='#80f0f0')
FRAME2=tk.LabelFrame(MAINFRAME, text='', fg='#80f0f0')
FRAME3=tk.LabelFrame(MAINFRAME, text='', bg='#80f0f0')


#________________________________________________ images _________________________________________

#cerating icon for admin
photoAdmin=PhotoImage(file='admin.png')

#creating icon for pilot
photoPilot=PhotoImage(file='driver1.png')

#creating icon for view records
photoView=PhotoImage(file='view.png')

#creating icon for insert records
photoInsert=PhotoImage(file='insert.png')

#creating icon for train details
photoTrain=PhotoImage(file='train1.png')
#------------------------------------------------- StringVariables ------------------------------
V1=tk.StringVar()
V2=tk.StringVar()

#_____________________________________________ Buttons ______________________________________

BUTTON1=tk.Button(MAINFRAME, text='RESET !', bg='#fa8072', relief=tk.GROOVE, command=reset)
BUTTON2=tk.Button(FRAME1, text='adminlogin', width=5, height=5, highlightthickness=0, relief=tk.GROOVE, command=login1)
BUTTON3=tk.Button(FRAME1, text='pilotlogin', width=10, height=5, highlightthickness=0, relief=tk.GROOVE, command=login2)
BUTTON5=tk.Button(FRAME2, text='insert', width=10, height=10, relief=tk.GROOVE, command=insert1)
BUTTON6=tk.Button(FRAME2, text='view', width=10, height=10, relief=tk.GROOVE, command=view3)
BUTTON7=tk.Button(FRAME3, text='SUBMIT', width=10, height=2, relief=tk.GROOVE, bg='#999999', fg='#000000', command=loco)
BUTTON8=tk.Button(FRAME3, text='SUBMIT', width=30, height=2, relief=tk.GROOVE, bg='#999999', fg='#000000', command=train_detail)
BUTTON9=tk.Button(MAINFRAME, text='EXIT!', relief=tk.GROOVE, bg='#fa8072', command=exit)
BUTTON10=tk.Button(FRAME2, text='TRAIN LIST', width=10, height=2, relief=tk.GROOVE, command=trainlist)
SPIN1=Spinbox(FRAME3,from_=1000, to=1010, width=10	, bd=8)
#values=(02731,19713, 17019, 11083, 12720, 17213, 11206, 51422, 17063, 19714, 17417, 18503,\
#17231, 18504, 11046, 17418, 07410, 07408, 57594, 16733, 11401, 16003, 17688, 11205, 16593, 17609)
ENTRYBOX1=tk.Entry(FRAME3, width=10)
ENTRYBOX2=tk.Entry(FRAME3, width=10)

#var1=SPIN1.get()
#var2=ENTRYBOX1.get()
#var3=ENTRYBOX2.get()
#______________________________________________ Labels _______________________________________

LABEL1=tk.Label(MAINFRAME, text='LOG ANALYSIS ON BIG DATA (TRAIN MANAGEMENT SYSTEM)', bg='#80f0f0', fg='#50afaf', relief=tk.GROOVE)
LABEL2=tk.Label(FRAME1, text='ADMIN', width=20, height=2, relief=tk.GROOVE, bg='#80f0f0')
LABEL3=tk.Label(FRAME1, text='LOCO PILOT', width=20, height=2, relief=tk.GROOVE, bg='#80f0f0')
LABEL6=tk.Label(FRAME2, text='INSERT', width=20, height=2, relief=tk.GROOVE, bg='#80f0f0')
LABEL7=tk.Label(FRAME2, text='VIEW', width=20, height=2, relief=tk.GROOVE, bg='#80f0f0')
LABEL8=tk.Label(FRAME3, text='ID', width=20, height=2, bg='#80f0f0')
LABEL9=tk.Label(FRAME3, text='NAME', width=20, height=2, bg='#80f0f0')
LABEL10=tk.Label(FRAME3, text='AGE', width=20, height=2, bg='#80f0f0')
LABEL11=tk.Label(FRAME3, text='EMAILID', width=20, height=2, bg='#80f0f0')
LABEL12=tk.Label(FRAME3, text='PASSWORD', width=20, height=2, bg='#80f0f0')
LABEL13=tk.Label(FRAME3, text='USERID', width=20, height=2, bg='#80f0f0')
LABEL14=tk.Label(FRAME3, text='TRAINNO', width=20, height=2, bg='#80f0f0')
LABEL15=tk.Label(FRAME3, text='SOURCE', width=20, height=2, bg='#80f0f0')
LABEL16=tk.Label(FRAME3, text='DESTINATION', width=20, height=2, bg='#80f0f0')
LABEL17=tk.Label(MAINFRAME, height=2, relief=tk.GROOVE, bg='#fa8072', fg='#80f0f0')
LABEL18=tk.Label(FRAME2, text='TRAIN LIST', width=20, relief=tk.GROOVE, height=2, bg='#80f0f0')
#______________________________________________ scrolled bar _________________________________

scrH=30
scrW=80
scr=scrolledtext.ScrolledText(MAINFRAME, width=scrW, height=scrH, wrap=tk.WORD, relief=tk.GROOVE, bg='#ffa07a')
#----------------------------------------------------------------------------------------------
scr.insert(tk.INSERT, ' trying to connect with databases.....\n')
scr.insert(tk.INSERT, ' connected\n')

# griding main label and button and scrolled bar
BUTTON1.place(x=10, y=10)
BUTTON9.place(x=200, y=10)
LABEL1.place(x=40, y=60)
scr.place(x=650, y=150)

# configure for main button and label
BUTTON1.config(font=('Bookman Old Style bold', 15))
LABEL1.config(font=('Bookman Old Style', 30))

BUTTON2.config(image=photoAdmin, width=220, height=220)
BUTTON3.config(image=photoPilot, width=220, height=220)
BUTTON5.config(image=photoInsert, width=220, height=220)
BUTTON6.config(image=photoView, width=220, height=220)
BUTTON10.config(image=photoTrain, width=220, height=220)
#________________________________________________ entries _______________________________________
ENTRY3=tk.Entry(FRAME3, width=20, bg='#fa8072')
ENTRY4=tk.Entry(FRAME3, width=20, bg='#fa8072')
ENTRY5=tk.Entry(FRAME3, width=20, bg='#fa8072')
ENTRY6=tk.Entry(FRAME3, width=20, bg='#fa8072')
ENTRY7=tk.Entry(FRAME3, width=20, bg='#fa8072')
ENTRY8=tk.Entry(FRAME3, width=20, bg='#fa8072')
ENTRY9=tk.Entry(FRAME3, width=20, bg='#fa8072')
ENTRY10=tk.Entry(FRAME3, width=20, bg='#fa8072')
ENTRY11=tk.Entry(FRAME3, width=20, bg='#fa8072')
#________________________________________________ configuring labels,buttons,entryboxes________________________________
#LABEL4.config(font=('Bookman Old Style',15))
#LABEL5.config(font=('Bookman Old Style',15))

BUTTON9.config(font=('Bookman Old Style bold', 15))
LABEL2.config(font=('Bookman Old Style bold', 15))
LABEL3.config(font=('Bookman Old Style bold', 15))
LABEL6.config(font=('Bookman Old Style bold' , 15))
LABEL7.config(font=('Bookman Old Style bold', 15))
LABEL6.config(font=('Bookman Old Style',15))
LABEL7.config(font=('Bookman Old Style',15))
LABEL8.config(font=('Bookman Old Style',15))
LABEL9.config(font=('Bookman Old Style',15))
LABEL10.config(font=('Bookman Old Style',15))
LABEL11.config(font=('Bookman Old Style',15))
LABEL12.config(font=('Bookman Old Style',15))
LABEL13.config(font=('Bookman Old Style',15))
LABEL14.config(font=('Bookman Old Style',15))
LABEL15.config(font=('Bookman Old Style',15))
LABEL16.config(font=('Bookman Old Style',15))
LABEL17.config(font=('Bookman Old Style bold',15))
LABEL18.config(font=('Bookman Old Style ',15))

ENTRY3.config(font=('Bookman Old Style',15))
ENTRY4.config(font=('Bookman Old Style',15))
ENTRY5.config(font=('Bookman Old Style',15))
ENTRY6.config(font=('Bookman Old Style',15))
ENTRY7.config(font=('Bookman Old Style',15))
ENTRY8.config(font=('Bookman Old Style',15))
ENTRY9.config(font=('Bookman Old Style',15))
ENTRY10.config(font=('Bookman Old Style',15))
ENTRY11.config(font=('Bookman Old Style',15))

BUTTON7.config(font=('Bookman Old Style',15))
#_______________________________________________________
projectCreater=tk.Label(MAINFRAME, text='Project Created By: Kadam Ajinkya M. & Kamthikar Rajat R.', bg='#F5DA81')
projectCreater.config(font=('Bookman Old Style',15))
projectCreater.place(x=850, y=735)
start()
clock()	

MAINFRAME.mainloop()
DB1.commit()
DB2.commit()
DB3.commit()
DB4.commit()
DB1.close()
DB2.close()
DB3.close()
DB4.close()
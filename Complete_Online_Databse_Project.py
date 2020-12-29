from tkinter import *
import pymysql
from tkinter import messagebox

x=Tk()
x.title("Employee Management System")

def add():
    t1,t2,t3,t4=str(e1.get()),str(e2.get()),str(e3.get()),str(e4.get())
    if t1=="" or t2=="" or t3=="" or t4=="":
        messagebox.showinfo("Alert!","All Fields Are Required")
    else:
        db=pymysql.connect("localhost","root","","databasetest")
        cur=db.cursor()
        cur.execute("INSERT INTO address(First_Name,Last_Name,Employee_Id,Country)VALUES('"+ t1 +"','"+ t2 +"','"+ t3 +"','"+ t4 +"')")
        db.commit()
        db.close()

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def show():
    db=pymysql.connect("localhost","root","","databasetest")
    cur=db.cursor()
    cur.execute("SELECT *FROM address")
    record=cur.fetchall()
    d=Toplevel()
    l5=Label(d,text=record)
    l5.grid(row=0,column=0,columnspan=2)
    db.commit()
    db.close()

def empdel():
    d=Toplevel()
    o=Label(d,text="Enter The Employee_Id To Delete")
    o.grid(row=0,column=0)
    global v
    v=Entry(d,width=20)
    v.grid(row=1,column=0)
    btn=Button(d,text="Submit",command=lambda:dele(str(v.get())))
    btn.grid(row=2,column=0,padx=10,pady=10)
    

def dele(val):
    v.delete(0,END)
    db=pymysql.connect("localhost","root","","databasetest")
    cur=db.cursor()
    cur.execute("DELETE FROM address WHERE Employee_Id="+str(val)+"")
    db.commit()
    db.close()


e1=Entry(x,width=20)
e1.grid(row=0,column=1)
e2=Entry(x,width=20)
e2.grid(row=1,column=1)
e3=Entry(x,width=20)
e3.grid(row=2,column=1)
e4=Entry(x,width=20)
e4.grid(row=3,column=1)

l1=Label(x,text="Enter The First Name")
l1.grid(row=0,column=0)
l2=Label(x,text="Enter The Last Name")
l2.grid(row=1,column=0)
l3=Label(x,text="Enter The Employee Id")
l3.grid(row=2,column=0)
l4=Label(x,text="Enter The Country")
l4.grid(row=3,column=0)

b1=Button(x,text="Add To Database",command=add)
b1.grid(row=4,column=0,columnspan=2,ipadx=90)

b2=Button(x,text="Show Database",command=show)
b2.grid(row=5,column=0,columnspan=2,ipadx=95)

b3=Button(x,text="Delete Database",command=empdel)
b3.grid(row=6,column=0,columnspan=2,ipadx=95)

x.mainloop()
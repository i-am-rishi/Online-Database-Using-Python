from tkinter import *
from tkinter import messagebox
import pymysql
import random

x=Tk()
x.title("Rock Paper Scissor Game")
icon=PhotoImage(file='MemeLogo.png')
x.iconphoto(False,icon)

global s,m
s,m=1,0

def comp(val):
    global s
    l9=Label(x,text="                                              ").grid(row=8,column=1)
    l10=Label(x,text="                ").grid(row=6,column=1,columnspan=1)
    l11=Label(x,text="                ").grid(row=7,column=1,columnspan=1)
    l17=Label(x,text="                ").grid(row=9,column=3,columnspan=1)

    c=['Rock','Paper','Scissor']
    l=random.randint(0,2)
    t=c[l]
    if val==t:
        l12=Label(x,text="Try Again It's a Tie").grid(row=8,column=1)
        l13=Label(x,text=val).grid(row=6,column=1,columnspan=1)
        l14=Label(x,text=t).grid(row=7,column=1,columnspan=1)

        l16=Label(x,text=str(int(100*(m/s)))+"%",fg='Brown')
        l16.config(font=("Courier",'15'))
        l16.grid(row=9,column=3,columnspan=1)

    else:
        score(val,t)
        s=s+1
        l13=Label(x,text=val).grid(row=6,column=1,columnspan=1)
        l14=Label(x,text=t).grid(row=7,column=1,columnspan=1)

def score(val,ch):
    global m
    if val=="Rock" and ch=="Scissor":
        m=m+1
        l15=Label(x,text=str(m)+"/"+str(s),fg='Brown')
        l15.config(font=("Courier",'20'))
        l15.grid(row=9,column=2,columnspan=1)

        l16=Label(x,text=str(int(100*(m/s)))+"%",fg='Brown')
        l16.config(font=("Courier",'15'))
        l16.grid(row=9,column=3,columnspan=1)


    elif val=="Rock" and ch=="Paper":
        l15=Label(x,text=str(m)+"/"+str(s),fg='Brown')
        l15.config(font=("Courier",'20'))
        l15.grid(row=9,column=2,columnspan=1)

        l16=Label(x,text=str(int(100*(m/s)))+"%",fg='Brown')
        l16.config(font=("Courier",'15'))
        l16.grid(row=9,column=3,columnspan=1)

    elif val=="Scissor" and ch=="Paper":
        m=m+1
        l15=Label(x,text=str(m)+"/"+str(s),fg='Brown')
        l15.config(font=("Courier",'20'))
        l15.grid(row=9,column=2,columnspan=1)

        l16=Label(x,text=str(int(100*(m/s)))+"%",fg='Brown')
        l16.config(font=("Courier",'15'))
        l16.grid(row=9,column=3,columnspan=1)

    elif val=="Scissor" and ch=="Rock":
        l15=Label(x,text=str(m)+"/"+str(s),fg='Brown')
        l15.config(font=("Courier",'20'))
        l15.grid(row=9,column=2,columnspan=1)

        l16=Label(x,text=str(int(100*(m/s)))+"%",fg='Brown')
        l16.config(font=("Courier",'15'))
        l16.grid(row=9,column=3,columnspan=1)

    elif val=="Paper" and ch=="Rock":
        m=m+1
        l15=Label(x,text=str(m)+"/"+str(s),fg='Brown')
        l15.config(font=("Courier",'20'))
        l15.grid(row=9,column=2,columnspan=1)

        l16=Label(x,text=str(int(100*(m/s)))+"%",fg='Brown')
        l16.config(font=("Courier",'15'))
        l16.grid(row=9,column=3,columnspan=1)

    elif val=="Paper" and ch=="Scissor":
        l15=Label(x,text=str(m)+"/"+str(s),fg='Brown')
        l15.config(font=("Courier",'20'))
        l15.grid(row=9,column=2,columnspan=1)

        l16=Label(x,text=str(int(100*(m/s)))+"%",fg='Brown')
        l16.config(font=("Courier",'15'))
        l16.grid(row=9,column=3,columnspan=1)




#Heading 1

l1=Label(x,text="This is a Rock Paper Scissor Game Using Python Tkinter")
l1.config(font=("Courier",'15'))
l1.grid(row=0,column=0,columnspan=6)

#Heading 2

l2=Label(x,text="Let's start the Game",fg='Green')
l2.config(font=("Times",'14'))
l2.grid(row=1,column=1,columnspan=1)


l3=Label(x,text="Your Options are : ",fg='Blue')
l3.config(font=("Times",'12'))
l3.grid(row=2,column=0)

l4=Label(x,text=" ").grid(row=3)

b1=Button(x,text="Rock",padx=12,pady=7,bg="Grey",command=lambda: comp("Rock")).grid(row=4,column=0,ipadx=10,columnspan=1)

b2=Button(x,text="Paper",padx=12,pady=7,bg="White",command=lambda: comp("Paper")).grid(row=4,column=1,ipadx=10,columnspan=1)

b3=Button(x,text="Scissor",padx=12,pady=7,bg="Red",command=lambda: comp("Scissor")).grid(row=4,column=2,ipadx=10,columnspan=1)

l5=Label(x,text="").grid(row=5,column=1,columnspan=1)

#Your Choice 

l6=Label(x,text="Your Choice : ")
l6.config(font=("Times",'12'))
l6.grid(row=6,column=0,columnspan=1)

#Computer's Choice

l7=Label(x,text="Computer's Choice : ")
l7.config(font=("Times",'12'))
l7.grid(row=7,column=0,columnspan=1)

l8=Label(x,text="Your Score : ",fg='Brown')
l8.config(font=("Courier",'20'))
l8.grid(row=9,column=1,columnspan=1)


x.mainloop()
#A GUI is creted to find sum of two numbers using tkinter 

import tkinter
from tkinter import *
from functools import partial

#Function to add two numbers
def sum(label,x1,x2):
	n1=(x1.get())
	n2=(x2.get())
	sum=int(n1)+int(n2)
	label.config(text="Sum : %d" %sum)
	return 

#Creating the window
win = Tk()

#Creating all the Labels in the window
l1=Label(win,text="Find Sum  ")
l1.grid(row=1,column=0)
l2=Label(win,text="Enter 1st no : ")
l2.grid(row=2,column=0)
l3=Label(win,text="Enter 2nd no : ")
l3.grid(row=3,column=0)
label=Label(win)
label.grid(row=5,column=1)

#x1 & x2 stores the user input
x1=StringVar()
x2=StringVar()

#Creating Entry attribute to enter the values
e1=Entry(win,textvariable=x1)
e1.grid(row=2,column=1)
e2=Entry(win,textvariable=x2)
e2.grid(row=3,column=1)

#A Partial function that calls sum with label,x1,x2 parameters
sum=partial(sum,label,x1,x2)

#Creating Button attribute 
b=Button(win,text="Calculate",command=sum)
b.grid(row=4,column=0)

win.mainloop()
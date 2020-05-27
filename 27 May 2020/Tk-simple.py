#Creating a simple GUI to print a label as Hellow world!!!

#importing Tkinter module
import tkinter
from tkinter import *

#Creating a window
win = Tk()

#Creating a Label in the window
label=Label(win , text = "Hello world!!!")
label.pack()
win.mainloop()
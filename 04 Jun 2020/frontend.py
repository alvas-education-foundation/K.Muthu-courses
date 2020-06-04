from tkinter import *
import backend

def get_selected_row(event):
	global selected_row
	index=list.curselection()[0]
	selected_row = list.get(index)
	e1.delete(0,END)
	e1.insert(END,selected_row[1])
	e2.delete(0,END)
	e2.insert(END,selected_row[2])
	e3.delete(0,END)
	e3.insert(END,selected_row[3])
	e4.delete(0,END)
	e4.insert(END,selected_row[4])
	e5.delete(0,END)
	e5.insert(END,selected_row[5])
	e6.delete(0,END)
	e6.insert(END,selected_row[6])
	
def delete_data():
	backend.delete(selected_row[0])

def view_all():
	list.delete(0,END)
	for row in backend.view():
		list.insert(END,row)
		
def search_data():
	list.delete(0,END)
	for row in backend.search(date_text.get(),saving_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get()):
		list.insert(END,row)
		
def add_data():
	backend.insert(date_text.get(),saving_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get())
	list.delete(0,END)
	list.insert(END,(date_text.get(),saving_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get()))
	

	

win = Tk()

win.wm_title('My Database')

l1=Label(win,text='Date : ')
l1.grid(row=0,column=0)
l2=Label(win,text='Savings : ')
l2.grid(row=0,column=2)
l3=Label(win,text='Exercise : ')
l3.grid(row=1,column=0)
l4=Label(win,text='Study : ')
l4.grid(row=1,column=2)
l5=Label(win,text='Diet : ')
l5.grid(row=2,column=0)
l6=Label(win,text='Python : ')
l6.grid(row=2,column=2)

date_text=StringVar()
e1=Entry(win,textvariable=date_text)
e1.grid(row=0,column=1)

saving_text=StringVar()
e2=Entry(win,textvariable=saving_text)
e2.grid(row=0,column=3)

exercise_text=StringVar()
e3=Entry(win,textvariable=exercise_text)
e3.grid(row=1,column=1)

study_text=StringVar()
e4=Entry(win,textvariable=study_text)
e4.grid(row=1,column=3)

diet_text=StringVar()
e5=Entry(win,textvariable=diet_text)
e5.grid(row=2,column=1)

python_text=StringVar()
e6=Entry(win,textvariable=python_text)
e6.grid(row=2,column=3)

list=Listbox(win,height=8,width=30)
list.grid(row=3,column=0,rowspan=8,columnspan=2)

list.bind('<<ListboxSelect>>',get_selected_row)

sb=Scrollbar(win)
sb.grid(row=3,column=2,rowspan=8)

b1=Button(win,text='ADD',command=add_data,width=8,pady=5)
b1.grid(row=3,column=3)
b2=Button(win,text='SEARCH',command=search_data,width=8,pady=5)
b2.grid(row=4,column=3)
b3=Button(win,text='DELETE',command=delete_data,width=8,pady=5)
b3.grid(row=5,column=3)
b4=Button(win,text='VIEW ALL',command=view_all,width=8,pady=5)
b4.grid(row=6,column=3)
b5=Button(win,text='CLOSE',command=win.destroy,width=8,pady=5)
b5.grid(row=7,column=3)


win.mainloop()
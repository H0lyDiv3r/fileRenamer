from tkinter import *
import backend

def add_command():
    backend.add(directory.get(),string.get())
    
def replace_command():
    backend.replace(word.get(),newword.get(),directory.get())

window=Tk()

l1=Label(window,text='Directory')
l1.grid(row=0,column=0)

directory=StringVar()
e1=Entry(window,width=50,textvariable=directory)
e1.grid(row=0,column=1,columnspan=4)

b1=Button(window,width=9,text="Add",command=add_command)
b1.grid(row=1,column=0)

string=StringVar()
e2=Entry(window,width=50,textvariable=string)
e2.grid(row=1,column=1,columnspan=4)

l2=Label(window,text='word to be\n replaced')
l2.grid(row=3,column=0)

word=StringVar()
e3=Entry(window,textvariable=word)
e3.grid(row=3,column=1)

l3=Label(window,text='new\nword')
l3.grid(row=3,column=2)

newword=StringVar()
e4=Entry(window,textvariable=newword)
e4.grid(row=3,column=3)

b2=Button(window,width=10,text='Replace',command=replace_command)
b2.grid(row=4,column=1,columnspan=4)

window.mainloop()
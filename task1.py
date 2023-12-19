"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""

import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.geometry("500x500")

eoutput = StringVar()


def clickFunction(event):

    print(event)

    answer = e1,e2,e3
   
    a_entry.insert(0,answer)


l1 = Label(win, text="name:")
e1 = Entry(win, width=20)

l2 = Label(win, text="student number:")
e2 = Entry(win, width=20)

l3 = Label(win, text="grade:")
e3 = Entry(win, width=20)

b1 = Button(win, text="click")
b1.bind("<Button>",clickFunction)

a_label = Label(win, text="information:")
a_entry = Entry(win, width=20, textvariable=eoutput)

l1.grid(row=1,column=1)
e1.grid(row=1,column=2)

l2.grid(row=2,column=1)
e2.grid(row=2,column=2)

l3.grid(row=3,column=1)
e3.grid(row=3,column=2)

b1.grid(row=4,column=2)

a_label.grid(row=5,column=1)
a_entry.grid(row=5,column=2)
win.mainloop()
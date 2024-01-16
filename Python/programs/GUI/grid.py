from tkinter import *

root=Tk()

# creating a label
label1= Label(root,text="Hello world!").grid(row=0,column=0)
label2= Label(root,text="My Name").grid(row=12,column=4)
label3= Label(root,text="             ")

# shoving it onto the screen

# the labels are relative even on specifications of column=4 the next label will be on the side, to resolve this use
label3.grid(row=0,column=1)
label3.grid(row=0,column=2)
label3.grid(row=0,column=3)


root.mainloop()
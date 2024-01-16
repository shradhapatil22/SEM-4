from tkinter import *

root=Tk()
root.title("Add frames")

frame=LabelFrame(root,text=" Frame 1....",padx=50,pady=50)
frame.pack(padx=10,pady=10)

b=Button(frame,text="don't")
b.pack()


root.mainloop()
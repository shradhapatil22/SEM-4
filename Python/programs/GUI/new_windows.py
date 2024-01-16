from tkinter import *



root=Tk()
root.title("Create new windows")
root.geometry("400x400")
def open():
    top=Toplevel()
    top.title("Second Window")
    label1=Label(top,text="Second Window").pack()
    btn1=Button(top,text="Close Window",command=top.destroy).pack()

btn=Button(root,text="Open Second Window",command=open).pack()



root.mainloop()
from tkinter import *

root=Tk()
root.geometry("400x400")
root.title("Calculator")

num1l=Label(root,text="Enter 1st number").grid(row=0,column=0)
num2l=Label(root,text="Enter 2nd number").grid(row=1,column=0)
resultl=Label(root,text="Result")

first=Entry(root,width=30,bg="black",fg="white").grid(row=0,column=1)
second=Entry(root,width=30,bg="black",fg="white").grid(row=1,column=1)
result=Entry(root,width=30,bg="black",fg="white").grid(row=3,column=1)

def add():
    firstNo=float(first.get())
    secondNo=float(second.get())
    result.set(firstNo + secondNo)

def sub():
    firstNo=float(first.get())
    secondNo=float(second.get())
    result.set(firstNo - secondNo)

def mul():
    firstNo=float(first.get())
    secondNo=float(second.get())
    result.set(firstNo * secondNo)

def div():
    firstNo=float(first.get())
    secondNo=float(second.get())
    result.set(firstNo / secondNo)


add=Button(root,text="Add ",command=add).grid(row=2,column=0)
sub=Button(root,text="Sub ",command=sub).grid(row=2,column=1)
mul=Button(root,text="Mul ",command=mul).grid(row=2,column=2)
div=Button(root,text="Div ",command=div).grid(row=2,column=3)

root.mainloop()
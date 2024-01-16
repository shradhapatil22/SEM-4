from tkinter import *

root=Tk()
root.title("Input Fields")
e=Entry(root,width=30,bg="black",fg="white")
e.pack()
e.insert(0,"Enter a name:")
def button_click():
    label1 = Label(root, text="Hello "+e.get())
    label1.pack()

# creating a button
button1=Button(root,text="Click here",padx=50,pady=10,command=button_click,fg="black",bg="blue")

# to make the button disabled   button1=Button(root,text="Click here",state=DISABLED)


# shoving it onto the screen
button1.pack()
# the labels are relative even on specifications of column=4 the next label will be on the side, to resolve this use



root.mainloop()
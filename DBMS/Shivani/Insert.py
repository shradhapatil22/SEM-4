from tkinter  import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import messagebox
from contextlib import closing
import PIL
from PIL import ImageTk
from PIL import Image 
flag=True
e1,e2,e3,e4,e5='','','','',''

def insert2():
    with closing(sqlite3.connect('clients.db'))as conn:
        with closing(conn.cursor()) as c:
            try:
                c.execute("create table if not exists client(cid integer primary key,fname text,lname text,addr text, ph_no int);")
            
            except:
                print("db table creation ERROR")
            cid=int(e1.get())
            phone=int(e5.get())
            try:
                c.execute("insert into client values(%d,'%s','%s','%s',%d)"%(cid,e2.get(),e3.get(),e4.get(),phone))   
                messagebox.showinfo("Info","INSERTION SUCCESSFUL ")

            except:
                 messagebox.showerror("ERROR","INSERTION UNSUCCESSFUL ")
            conn.commit()
            





def insert():
    root4= tk.Tk()
    root4.title("INSERT RECORDS")
    root4.geometry("300x400")
    global e1,e2,e3,e4,e5
    e1=ttk.Entry(root4,width=30)
    e2=ttk.Entry(root4,width=30)
    e3=ttk.Entry(root4,width=30)
    e4=tk.Entry(root4,width=30)
    e5=tk.Entry(root4,width=30)

    # E1=ttk.Entry(root4,width=25,textvariable=CID)

   
    tk.Label(root4,text="CID").grid(row=0,column=0)

    e1.grid(row=0,column=1)
  

    tk.Label(root4,text="FNAME").grid(row=1,column=0)
    # e2=ttk.entry(root4,width=25,textvariable=FNAMe)
    e2.grid(row=1,column=1)

    tk.Label(root4,text="LNAME").grid(row=2,column=0)
    # E3=ttk.Entry(root4,width=25,textvariable=LNAME)
    e3.grid(row=2,column=1)

    tk.Label(root4,text="ADDR").grid(row=3,column=0)
    # e4=tk.entry(root4,width=25,textvariable=ADD)
    e4.grid(row=3,column=1)

    tk.Label(root4,text="PHONE").grid(row=4,column=0)
    # e5=tk.entry(root4,width=25,textvariable=PHONE)
    e5.grid(row=4,column=1)
    for child in root4.winfo_children():
        child.grid_configure(padx=10,pady=10)


    tk.Button(root4,text='INSERT',command=insert2,bg="lightblue").grid(row=5,column=1)
   
    root4.mainloop()
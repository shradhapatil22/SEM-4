from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from Update import *
from Delete import *
from Insert import *
from tkinter import messagebox
from contextlib import closing
from turtle import width

flag=TRUE
file='pharmacy.db'

root1= Tk()
root1.title("Pharmacy Database")
root1.geometry("900x500")

Title_label=tk.Label(text="Pharmacy Database",width=100,height=2)
Title_label.pack(sid="top")

#===============frame for tree view===================
frame=tk.Frame(root1,bg="lightblue")
frame.place(relx=0.10,rely=0.3,relwidth=0.8,relheight=0.6)

#================treeview of the table==================
tr=ttk.Treeview(frame)
tr['columns']=('Name','Type','Barcode','Cost')
tr.column("#0",width=12,minwidth=20)
tr.column("Name",anchor=CENTER,width=20)
tr.column("Type",anchor=W,width=50)
tr.column("Barcode",anchor=W,width=50)
tr.column("Cost",anchor=W,width=80)

tr.heading("#0",text="No",anchor=W)
tr.heading("Name",text="Name",anchor=W)
tr.heading("Type",text="Type",anchor=W)
tr.heading("Barcode",text="Barcode",anchor=W)
tr.heading("Cost",text="Cost",anchor=W)


tr.place(relheight=1,relwidth=1)

#=======================retrieve function=======================
def retrieve():
    with closing(sqlite3.connect(file))as conn:
        with closing(conn.cursor()) as c:
            try:
                c.execute("create table if not exists client(Name text,Type text,Barcode text primary key,Cost int);")
            except:
                print("db table creation ERROR")
            query="select *from DRUG order by Name"
            c.execute(query)
            global count
            count=0
            for rec in c.fetchall():
                c=str(count+1)
                tr.insert(parent='',index='end',iid=count, text=c,values=(rec[0],rec[1],rec[2],rec[3],rec[4]))
                count+=1
            conn.commit()

retrieve()

def clearall():
    for item in tr.get_children():
        tr.delete(item)
    retrieve()

#============Main Page buttons=============
b1=tk.Button(root1 ,text="RETRIEVE",bg="lightblue",command=clearall)
b1.place(relx=0.75,rely=0.15,relwidth=0.15,relheight=0.05)

b2=tk.Button(root1 ,text="UPDATE",bg="lightblue")
b2.place(relx=0.10,rely=0.15,relwidth=0.15,relheight=0.05)

b3=tk.Button(root1 ,text="INSERT",bg="lightblue",command=insert)
b3.place(relx=0.33,rely=0.15,relwidth=0.15,relheight=0.05)

b4=tk.Button(root1 ,text="DELETE",bg="lightblue",command=delete)
b4.place(relx=0.55,rely=0.15,relwidth=0.15,relheight=0.05)


root1.mainloop()
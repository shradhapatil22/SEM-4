from tkinter  import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import messagebox
from contextlib import closing
from turtle import width
from Update import *
from Delete import *
# from Insert import *
# import PIL
# from PIL import ImageTk
# from PIL import Image
import tkinter .font as font


flag=True
file='clients.db'

root1= tk.Tk()
root1.title("CLIENT RECORDS")
root1.geometry("900x500")
# image1=tk.PhotoImage(file='dbmsbg.png')
# l1=tk.Label(root1,image=image1)
# l1.place(relx=0,rely=0)
f=font.Font(weight='bold')
l=tk.Label(text="WELCOME TO CLIENT DATABASE",width=100,height=2,bg="lightblue")
l.pack(sid="top")
l['font']=f
frame=tk.Frame(root1,bg="red")
frame.place(relx=0.02,rely=0.1,relwidth=0.7,relheight=0.6)

tr=ttk.Treeview(frame)
tr['columns']=("CID",'FNAME','LNAME','ADD','PHONE')
tr.column("#0",width=12,minwidth=20)
tr.column("CID",anchor=CENTER,width=20)
tr.column("FNAME",anchor=W,width=50)
tr.column("LNAME",anchor=W,width=50)
tr.column("ADD",anchor=W,width=80)
tr.column("PHONE",anchor=W,width=60)

tr.heading("#0",text="No",anchor=W)
tr.heading("CID",text="CID",anchor=W)
tr.heading("FNAME",text="FNAME",anchor=W)
tr.heading("LNAME",text="LNAME",anchor=W)
tr.heading("ADD",text="ADD",anchor=W)
tr.heading("PHONE",text="PHONE",anchor=W)

tr.place(relheight=1,relwidth=1)


# tr.tag_configure(tagname='se',background="red")

def retrieve():
    with closing(sqlite3.connect(file))as conn:
        with closing(conn.cursor()) as c:
            try:
                c.execute("create table if not exists client(cid integer primary key,fname text,lname text,addr text, ph_no int);")
            except:
                print("db table creation ERROR")
            query="select *from client order by cid"
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

b1=tk.Button(root1 ,text="RETRIEVE",bg="white",command=clearall)
b1.place(relx=0.75,rely=0.1,relwidth=0.2,relheight=0.05)

b2=tk.Button(root1 ,text="UPDATE",bg="white",command=update)
b2.place(relx=0.75,rely=0.2,relwidth=0.2,relheight=0.05)

b3=tk.Button(root1 ,text="INSERT",bg="white",command=insert)
b3.place(relx=0.75,rely=0.3,relwidth=0.2,relheight=0.05)

b4=tk.Button(root1 ,text="DELETE",bg="white",command=delete)
b4.place(relx=0.75,rely=0.4,relwidth=0.2,relheight=0.05)



root1.mainloop()


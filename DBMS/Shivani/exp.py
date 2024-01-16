from tkinter  import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from contextlib import closing
'''
E1=ttk.Entry(root2,width=25,textvariable=CID)
E2=ttk.Entry(root2,width=25,textvariable=FNAME)
E3=ttk.Entry(root2,width=25,textvariable=LNAME)
E4=tk.Entry(root2,width=25,textvariable=ADD)
E5=tk.Entry(root2,width=25,textvariable=PHONE)
'''
root2= tk.Tk()
root2.withdraw()
root3=tk.Tk()
root3.withdraw()

E1=ttk.Entry(root2,width=25)
E2=ttk.Entry(root2,width=25)
E3=ttk.Entry(root2,width=25)
E4=tk.Entry(root2,width=25)
E5=tk.Entry(root2,width=25)
E6=ttk.Entry(root3,width=25)



'''
CID= tk.StringVar(E1)
FNAME = tk.StringVar(E)
LNAME = tk.StringVar()
ADD = tk.StringVar()
PHONE = tk.StringVar()

'''
file='clients.db'

root1= tk.Tk()
root1.title("RECORDS")
root1.geometry("1000x1000")
frame=tk.Frame(root1,bg="red")
frame.place(relx=0.1,rely=0.1,relwidth=0.6,relheight=0.8)

tr=ttk.Treeview(frame)
tr['columns']=("CID",'FNAME','LNAME','ADD','PHONE')
tr.column("#0",width=12,minwidth=25)
tr.column("CID",anchor=CENTER,width=80)
tr.column("FNAME",anchor=W,width=50)
tr.column("LNAME",anchor=W,width=50)
tr.column("ADD",anchor=W,width=50)
tr.column("PHONE",anchor=W,width=50)

tr.heading("#0",text="No",anchor=W)
tr.heading("CID",text="CID",anchor=W)
tr.heading("FNAME",text="FNAME",anchor=W)
tr.heading("LNAME",text="LNAME",anchor=W)
tr.heading("ADD",text="ADD",anchor=W)
tr.heading("PHONE",text="PHONE",anchor=W)

tr.place(relheight=1,relwidth=1)


# tr.tag_configure(tagname='se',background="red")

with closing(sqlite3.connect(file))as conn:
    with closing(conn.cursor()) as c:
        try:
            c.execute("create table if not exists client(cid integer primary key,fname text,lname text, addr text, ph_no integer);")
        except:
            print("db table creation ERROr")
        conn.commit()
        query="select * from client order by cid"
        c.execute(query)
        count=0
        for rec in c.fetchall():
            print(rec)
            c=str(count+1)
            tr.insert(parent='',index='end',iid=count, text=c,values=(rec[0],rec[1],rec[2],rec[3],rec[4]))
            count+=1
        conn.commit()



def retrive():
    with closing(sqlite3.connect(file))as conn:
        with closing(conn.cursor()) as c:
            try:
                c.execute("create table if not exists client(cid integer primary key,fname text,lname text,addr text, ph_no int);")
            except:
                print("db table creation ERROr")
            query="select *from client order by cid"
            c.execute(query)
            count=0  
            for rec in c.fetchall():
                c=str(count+1)
                tr.insert(parent='',index='end',iid=count, text=c,values=(rec[0],rec[1],rec[2],rec[3],rec[4]))
                count+=1
            conn.commit()


def update2():
    with closing(sqlite3.connect(file))as conn:
        with closing(conn.cursor()) as c:
            try:
                c.execute("create table if not exists client(cid integer primary key,fname text,lname text,addr text, ph_no int);")
            except:
                print("db table creation ERROR")
            cid=int(E1.get())
            c.execute("""UPDATE CLIENT SET FNAME =:fname ,
            LNAME =:lname ,
            ADDR =:addr ,
            PH_NO =:phone  
            where CID =:cid """,
            {
                'fname':E2.get(),'lname':E3.get(),'addr':E4.get(),'phone':E5.get(), 'cid':cid
            }
)
            conn.commit()
            print("successs")

def search():
    with closing(sqlite3.connect(file))as conn:
        with closing(conn.cursor()) as c:
            try:
                c.execute("create table if not exists client(cid integer primary key,fname text,lname text, addr text, ph_no int);")
            except:
                print("db table creation ERROR")

            if E1.get()=='':
                cid=E6.get()
                print(cid)
            else:
                cid=E1.get()
                print(cid)
                
            query="select * from client where CID="+cid+";"
            c.execute(query)
            if len(c.fetchall())==0:
                print("record not found")
            else :
                print("record found")


def update():
    root2.deiconify()
    tk.Button(root2,text='search',command=search).grid(row=0,column=0)
    # E1=ttk.Entry(root2,width=25,textvariable=CID)
    E1.grid(row=0,column=1)

    tk.Label(root2,text="FNAME").grid(row=1,column=0)
    # E2=ttk.Entry(root2,width=25,textvariable=FNAME)
    E2.grid(row=1,column=1)

    tk.Label(root2,text="LNAME").grid(row=2,column=0)
    # E3=ttk.Entry(root2,width=25,textvariable=LNAME)
    E3.grid(row=2,column=1)

    tk.Label(root2,text="ADD").grid(row=3,column=0)
    # E4=tk.Entry(root2,width=25,textvariable=ADD)
    E4.grid(row=3,column=1)

    tk.Label(root2,text="PHONE").grid(row=4,column=0)
    # E5=tk.Entry(root2,width=25,textvariable=PHONE)
    E5.grid(row=4,column=1)

    tk.Button(root2,text='UPDATE',command=update2).grid(row=5,column=0)
    E1.delete(0,"end")
    E2.delete(0,"end")


    root2.mainloop()

def delete2():
    with closing(sqlite3.connect(file))as conn:
        with closing(conn.cursor()) as c:
            try:
                c.execute("create table if not exists client(cid integer primary key,fname text,lname text, addr text, ph_no int);")
            except:
                print("db table creation ERROR")
            cid=int(E6.get())
            query="delete from client where CID=:cid;"
            c.execute(query)
            conn.commit()
            print("record deleted")
            # root3.withdraw()


def delete():
    root3.deiconify()
    tk.Button(root3, text='search',command=search).grid(row=0,column=0)
    # E6=ttk.Entry(root3,width=25)
    E6.grid(row=0,column=1)

    tk.Button(root3,text='DELETE',command=delete2).grid(row=1,column=0)
    root3.mainloop()


b1=tk.Button(root1 ,text="retrive",bg="yellow",command=retrive)
b1.place(relx=0.75,rely=0.1,relwidth=0.2,relheight=0.05)

b2=tk.Button(root1 ,text="UPDATE",bg="red",command=update)
b2.place(relx=0.75,rely=0.2,relwidth=0.2,relheight=0.05)

b3=tk.Button(root1 ,text="DELETE",bg="red",command=delete)
b3.place(relx=0.75,rely=0.3,relwidth=0.2,relheight=0.05)
root1.mainloop()


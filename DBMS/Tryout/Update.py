from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import messagebox
from contextlib import closing


E1, E2, E3, E4, E5 = '', '', '', '', ''
flag = True


def update2():
    with closing(sqlite3.connect('pharmacy.db'))as conn:
        with closing(conn.cursor()) as c:
            try:
                c.execute(
                    "create table if not exists client(Name text,Type text,Barcode text primary key,Cost int);")
            except:
                print("db table creation ERROR")
            if flag:
                cid = int(E1.get())
                c.execute("""UPDATE CLIENT SET FNAME =:fname ,
                LNAME =:lname ,
                ADDR =:addr ,
                PH_NO =:phone  
                where CID =:cid """,
                          {
                              'fname': E2.get(), 'lname': E3.get(), 'addr': E4.get(), 'phone': E5.get(), 'cid': cid
                          }
                          )
                conn.commit()
                messagebox.showinfo("Info", "Updation Successful ")

            else:
                messagebox.showerror("ERROR", "  Invalid Updation ")


def search():
    global flag
    with closing(sqlite3.connect('clients.db'))as conn:
        with closing(conn.cursor()) as c:
            try:
                c.execute(
                    "create table if not exists client(cid integer primary key,fname text,lname text, addr text, ph_no int);")
            except:
                print("db table creation ERROR")
            cid = int(E1.get())
            print(cid)
            c.execute("select * from client where CID=:cid", {"cid": cid})
            if len(c.fetchall()) == 0:
                flag = False
                messagebox.showerror("ERROR", "RECORD NOT FOUND")
            else:
                flag = True
                messagebox.showinfo("Info", "RECORD FOUND")


def update():
    root2 = tk.Tk()
    root2.title("UPDATE RECORDS")
    root2.geometry("400x400")
    global E1, E2, E3, E4, E5
    E1 = ttk.Entry(root2, width=30)
    E2 = ttk.Entry(root2, width=30)
    E3 = ttk.Entry(root2, width=30)
    E4 = tk.Entry(root2, width=30)
    E5 = tk.Entry(root2, width=30)
    # E1=ttk.Entry(root2,width=25,textvariable=CID)
    tk.Label(root2, text="CID").grid(row=0, column=0)

    E1.grid(row=0, column=1)
    tk.Button(root2, text='SEARCH', command=search, bg="lightblue").grid(row=1, column=1)

    tk.Label(root2, text="FNAME").grid(row=2, column=0)
    # E2=ttk.Entry(root2,width=25,textvariable=FNAME)
    E2.grid(row=2, column=1)

    tk.Label(root2, text="LNAME").grid(row=3, column=0)
    # E3=ttk.Entry(root2,width=25,textvariable=LNAME)
    E3.grid(row=3, column=1)

    tk.Label(root2, text="ADDR").grid(row=4, column=0)
    # E4=tk.Entry(root2,width=25,textvariable=ADD)
    E4.grid(row=4, column=1)

    tk.Label(root2, text="PHONE").grid(row=5, column=0)
    # E5=tk.Entry(root2,width=25,textvariable=PHONE)
    E5.grid(row=5, column=1)
    for child in root2.winfo_children():
        child.grid_configure(padx=10, pady=10)

    tk.Button(root2, text='UPDATE', command=update2, bg="lightblue").grid(row=6, column=1)

    root2.mainloop()
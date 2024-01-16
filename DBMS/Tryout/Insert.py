from tkinter  import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import messagebox
from contextlib import closing

flag=True
e1,e2,e3,e4,e5='','','','',''

#============Data Insertion===========
def insert2():
    with closing(sqlite3.connect('pharmacy.db'))as conn:
        with closing(conn.cursor()) as c:
            try:
                c.execute(
                    "create table if not exists client(Name text,Type text,Barcode text primary key,Cost int);")

            except:
                print("db table creation ERROR")
            cost = int(e4.get())

            try:
                c.execute(
                    "insert into client values(%s,'%s','%s',%d)" % (e1.get(), e2.get(), e3.get(), cost))
                messagebox.showinfo("Info", "INSERTION SUCCESSFUL ")

            except:
                messagebox.showerror("ERROR", "INSERTION UNSUCCESSFUL ")
            conn.commit()


def insert():
    root4 = tk.Tk()
    root4.title("INSERT RECORDS")
    root4.geometry("300x400")
    global e1, e2, e3, e4, e5
    e1 = ttk.Entry(root4, width=30)
    e2 = ttk.Entry(root4, width=30)
    e3 = ttk.Entry(root4, width=30)
    e4 = tk.Entry(root4, width=30)


    #labels and tet fields

    tk.Label(root4, text="Name").grid(row=0, column=0)
    e1.grid(row=0, column=1)

    tk.Label(root4, text="Barcode").grid(row=1, column=0)
    e2.grid(row=1, column=1)

    tk.Label(root4, text="Type").grid(row=2, column=0)
    e3.grid(row=2, column=1)

    tk.Label(root4, text="Cost").grid(row=3, column=0)
    e4.grid(row=3, column=1)


    for child in root4.winfo_children():
        child.grid_configure(padx=10, pady=10)

    tk.Button(root4, text='INSERT', command=insert2, bg="lightblue").grid(row=5, column=1)

    root4.mainloop()
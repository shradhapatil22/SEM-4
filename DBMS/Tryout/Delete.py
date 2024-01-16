from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import messagebox
from contextlib import closing


flag = True
E1 = ''


def delete2():
    with closing(sqlite3.connect('pharmacy.db'))as conn:
        with closing(conn.cursor()) as c:
            try:
                c.execute(
                    "create table if not exists client(Name text,Type text,Barcode text primary key,Cost int);")
            except:
                print("db table creation ERROR")

            if flag:
                c.execute("delete from client where Name=:E1.get()", {"Name":E1.get()})
                conn.commit()
                messagebox.showinfo("Info", "Record Deleted")
            else:
                messagebox.showerror("ERROR", "Invalid Deletion")


def delete3():
    with closing(sqlite3.connect('pharmacy.db'))as conn:
        with closing(conn.cursor()) as c:
            try:
                c.execute(
                    "create table if not exists client(Name text,Type text,Barcode text primary key,Cost int);")
            except:
                print("db table creation ERROR")

            try:
                c.execute("delete from client ")
                conn.commit()
                messagebox.showinfo("Info", " All Records Deleted")
            except:
                messagebox.showerror("ERROR", "Invalid Deletion")


def search():
    global flag
    with closing(sqlite3.connect('pharmacy.db'))as conn:
        with closing(conn.cursor()) as c:
            try:
                c.execute(
                    "create table if not exists client(Name text,Type text,Barcode text primary key,Cost int);")
            except:
                print("db table creation ERROR")
            cid = int(E6.get())
            c.execute("select * from DRUG where Nmae=:E1.get()", {"Name":E1.get() })
            if len(c.fetchall()) == 0:
                flag = False
                messagebox.showerror("ERROR", "RECORD NOT FOUND")
            else:
                flag = True
                messagebox.showinfo("Info", "RECORD  FOUND")


def delete():
    root3 = tk.Tk()
    root3.title('DELETE RECORDS')
    root3.geometry('250x200')
    tk.Label(root3, text="Name").grid(row=0, column=0, pady=1)
    global E1
    E1 = ttk.Entry(root3, width=10)
    E1.grid(row=0, column=1, padx=2)

    tk.Button(root3, text='SEARCH', command=search, bg="lightblue").grid(row=1, column=1, pady=8)

    tk.Button(root3, text='DELETE ALL', command=delete3, bg="lightblue").grid(row=2, column=0, pady=6)

    tk.Button(root3, text='DELETE    ', command=delete2, bg="lightblue").grid(row=2, column=2, padx=2, pady=6)
    root3.mainloop()

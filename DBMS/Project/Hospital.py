import tkinter as tk
from tkinter import ttk
from contextlib import closing
import sqlite3
from patient import*
# from department import*
# from bill import*
# from doctor import*
# from hospital12 import*
# from payment import*
# from Medicine import*
from tkinter import PhotoImage
root=tk.Tk()
root.title("Hospital Database")
root.geometry("600x400")

ch=''
frame=ttk.Frame(root,padding="20 20 20 20")
frame.pack()

def choicetotable():
    if ch == 'Patient':
        pe.pcall()
    if ch == 'Department':
        de.dcall()
    if ch == 'Bill':
        be.bcall()
    if ch == 'Doctor':
        dte.dtcall()
    if ch == 'Hospital':
        he.hcall()
    if ch == 'Payment':
        pay.pcall()
    if ch == 'Medicine':
        Med.Mcall()
        
def delete():
    if ch == 'Patient':
        pe.pde()
    if ch == 'Department':
        de.dde()
    if ch == 'Bill':
        be.bde()
    if ch == 'Doctor':
        dte.ddte()
    if ch == 'Hospital':
        he.hte()
    if ch == 'Payment':
        pay.pyt()
    if ch == 'Medicine':
        Med.Mte()
                
def update():
    if ch == 'Patient':
        pUpdate()
    if ch == 'Department':
        departmentUpdate()
    if ch == 'Bill':
        BillUpdate()
    if ch == 'Doctor':
        dUpdate()
    if ch == 'Hospital':
        hUpdate()
    if ch == 'Payment':
        paUpdate()
    if ch == 'Medicine':
        MUpdate()
                
def display():
    if ch == 'Patient':
        pe.pdisplay()
    if ch == 'Department':
        de.ddisplay()
    if ch == 'Bill':
        be.bdisplay()
    if ch == 'Doctor':
        dte.dtdisplay()
    if ch == 'Hospital':
        he.hdisplay()
    if ch == 'Payment':
        pay.pdisplay()
    if ch == 'Medicine':
        Med.Mdisplay()



def insert(conn):
    try:
        query = "insert into Hospital values(1,20,'Belagavi','xyz')"
    except:
        print("DBinsert error")
    conn.commit()

def Dropdown():
    clicked = tk.StringVar()
    clicked.set("Select Table")

    def printme(choice):
        global ch
        choice = clicked.get()
        ch=choice
    drop = tk.OptionMenu(root, clicked, "Patient", "Nurse", "Hospital", "Medicine", "Department", "Doctor","Bill","Payment",command=printme)
    drop.pack()

    val=clicked.get()
    l=tk.Label(root,text=clicked.get())

def Home():
    ttk.Button(frame, text="INSERT",command=choicetotable).grid(row=2,column=0)
    ttk.Button(frame, text="DELETE",command=delete).grid(row=2,column=1)
    ttk.Button(frame, text="UPDATE",command=update).grid(row=2,column=2)
    ttk.Button(frame, text="DISPLAY",command=display).grid(row=2, column=3)
    Dropdown()
    root.mainloop()

if __name__=='__main__':
    Home()

from email import message
from logging import root
import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox

file = "C:\\Users\\Sanket Patil\\OneDrive\\Desktop\\Dhospital.sqlite"


def dbConnect(file):
    try:
        conn = sqlite3.connect(file)
        return conn
    except:
        print("DBconnect error")
        
        
def textvalues(patid, age, address, patname,nid,did,hid):
    global file
    con = dbConnect(file)
    patid=int(patid)
    age=int(age)
    nid=int(nid)
    did=int(did)
    hid=int(hid)
    cur = con.cursor()
    q = 'insert into PATIENT values(?,?,?,?,?,?,?)'
    try:
        cur.execute(q, (patid, age, address, patname,nid,did,hid))
    except:
        print("DBinsert error")
    con.commit()
    messagebox.showinfo("Insert","Record Added")
 
def dbDelete(pat):
    global file
    con = dbConnect(file)
    try:
        c = con.cursor()
        query = 'delete from PATIENT where patid=(?)'
        c.execute(query, (pat,))
        messagebox.showinfo("Successful", "Record deleted successfully")
    except:
        messagebox.showinfo("Unsuccessful", "Db delete error")
    con.commit()
    
def update(attribute,value,id):
    global file
    conn=dbConnect(file)
    command='Update PATIENT set '+(attribute)+'=(?) where patid=(?)'
    try:
        cur=conn.cursor()
        print(attribute,value,id)
        v=int(id)
        cur.execute(command,(value,v))        
    except:
        print("Update Error")  
    conn.commit()


class pe:
    def pde():
        root=tk.Tk()
        root.title("Hospital Database")
        root.geometry("600x400")
        
        ttk.Label(root, text="Enter pat_id to delete:").grid(row=0, column=0, sticky=tk.E)
        patid = tk.StringVar(root)
        ttk.Entry(root, width=25, textvariable=patid).grid(row=0, column=1)
        def gettex():
            pat=(patid.get())
            pat=int(pat)
            dbDelete(pat)
        
        ttk.Button(root, text="Delete Record", command=gettex).grid(row=5, column=1)
        
        for child in root.winfo_children():
            child.grid_configure(padx=10, pady=10)
        root.mainloop()  
    def pcall():
        root=tk.Tk()
        root.title("Hospital Database")
        root.geometry("600x400")
        
        
        ttk.Label(root, text="pat_id:").grid(row=0, column=0, sticky=tk.E)
        patid = tk.StringVar(root)
        ttk.Entry(root, width=25, textvariable=patid).grid(row=0, column=1)

        ttk.Label(root, text="age").grid(row=1, column=0, sticky=tk.E)
        age = tk.StringVar(root)
        ttk.Entry(root, width=25, textvariable=age).grid(row=1, column=1)

        ttk.Label(root, text="address").grid(row=2, column=0, sticky=tk.E)
        address = tk.StringVar(root)
        ttk.Entry(root, width=25, textvariable=address).grid(row=2, column=1)

        ttk.Label(root, text="pat_name").grid(row=3, column=0, sticky=tk.E)
        patname = tk.StringVar(root)
        ttk.Entry(root, width=25, textvariable=patname).grid(row=3, column=1)
        
        ttk.Label(root, text="n_id").grid(row=4, column=0, sticky=tk.E)
        nid = tk.StringVar(root)
        ttk.Entry(root, width=25, textvariable=nid).grid(row=4, column=1)
        
        ttk.Label(root, text="d_id").grid(row=5, column=0, sticky=tk.E)
        did = tk.StringVar(root)
        ttk.Entry(root, width=25, textvariable=did).grid(row=5, column=1)
        
        ttk.Label(root, text="hid").grid(row=6, column=0, sticky=tk.E)
        hid = tk.StringVar(root)
        ttk.Entry(root, width=25, textvariable=hid).grid(row=6, column=1)
        
        def gettex():
            textvalues(patid.get(), age.get(), address.get(), patname.get(),nid.get(),did.get(),hid.get())

        ttk.Button(root, text="Add Record", command=gettex).grid(row=7, column=1)
        
        for child in root.winfo_children():
            child.grid_configure(padx=10, pady=10)
        root.mainloop()
    def pdisplay():
        root=tk.Tk()
        root.title("Patient")
        root.geometry("1000x400")
        global file
        conn=dbConnect(file)
        cur=conn.cursor()
        def View():
            r_set=cur.execute('Select * from patient')
            for patient in r_set:
                tree.insert("", tk.END, values=patient) 
        
        tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4"), show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="PAT_ID")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="AGE")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="ADDRESS")
        tree.column("#4", anchor=tk.CENTER)
        tree.heading("#4", text="PAT_NAME")
        tree.pack()
        button1 = tk.Button(root,text="Display data", command=View)
        button1.pack(pady=10)

class pUpdate:
    
    def __init__(self):
        self.root=tk.Tk()
        self.calltk2()
        self.root.mainloop()
    def calltk2(self):
        root=self.root
        root.title("Display Patient")
        root.geometry("600x400")
        ttk.Label(root,text="Enter patid to Update:").pack(padx=3,pady=0)
        p_Id=tk.StringVar(root)
        ttk.Entry(root,width=25,textvariable=p_Id).pack(padx=5,pady=0)
        
        self.dropdown(p_Id)
                
    def dropdown(self,id):
        global file
        root=self.root
        menu=StringVar(root)
        menu.set("Select Attribute")
       
       
        drop_value=''
        def _setdropvalue(choice):
            global drop_value
            choice=menu.get()
            drop_value=choice
            
        drop=OptionMenu(root, menu,"patid","age","address","patname",command=_setdropvalue)
        drop.pack(pady=12)
        
        
        ttk.Label(self.root,text="Enter Value to Update:").pack(padx=3,pady=0)
        upd=tk.StringVar(self.root)
        ttk.Entry(self.root,width=25,textvariable=upd).pack(padx=5,pady=0) 
       
        def _updatefromuser():
            global drop_value
            update(drop_value,upd.get(),id.get())
         
        ttk.Button(root, text="Update",command=_updatefromuser).pack(padx=8,pady=20)
        val=menu.get()
        l=ttk.LabelFrame(root,text=menu.get())
        
def dbConnect(file):
    try:
        conn = sqlite3.connect(file)
        return conn
    except:
        print("DBconnect error")


def insert(conn):
    try:
        query = textvalues()
    except:
        print("DBinsert error")
    conn.commit()

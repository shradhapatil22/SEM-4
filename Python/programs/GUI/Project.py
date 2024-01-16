from tkinter import *
import sqlite3
from contextlib import closing

conn = sqlite3.connect("G:\\college\\SEM 4\\DBMS\\Project\\Pharmacy.db")

def dbConnecct(file):
    try:
        conn=sqlite3.connect(file)
        return conn
    except:
        print("dbConnecct error")



root=Tk()
Title_label= Label(root,text="Pharmacy Database ").grid(row=0,column=1)
root.geometry("400x400")

#new windows
def open_insert():
    conn = dbConnecct("G:\\college\\SEM 4\\DBMS\\Project\\Pharmacy.db")
    top = Tk()
    top.title("Insert")
    top.geometry("250x250")
    label = Label(top, text="Insert").pack()

    # Get Data
    label1 = Label(top, text="Enter drug name:").pack()
    Name = Entry(top, width=30)
    Name.pack()
    label2 = Label(top, text="Enter drug type:").pack()
    Type = Entry(top, width=30)
    Type.pack()
    label3 = Label(top, text="Enter drug cost:").pack()
    Cost = Entry(top, width=30)
    Cost.pack()

    # insert statements
    def insert_data(conn):
        with closing(conn.cursor()) as C:
            query = "insert into Drug values('{}','{}',{})"
            cost_int=int(Cost.get())
            try:
                C.execute(query, (Name.get(), Type.get(), cost_int))
                conn.commit()
            except:
                print("DbInsert error")






    insert=Button(top,text="Insert Data",command=insert_data).pack()
    btn1 = Button(top, text="Close Window", command=top.destroy).pack()




def open_delete(conn):
    top = Toplevel()
    top.title("Delete")
    top.geometry("250x250")
    label1 = Label(top, text="Delete").pack()
    btn1 = Button(top, text="Close Window", command=top.destroy).pack()

def open_Select(conn):
    top = Toplevel()
    top.title("Select")
    top.geometry("250x250")
    label1 = Label(top, text="Select").pack()
    btn1 = Button(top, text="Close Window", command=top.destroy).pack()

def open_update(conn):
    top = Toplevel()
    top.title("Update")
    top.geometry("250x250")
    label1 = Label(top, text="Update").pack()
    btn1 = Button(top, text="Close Window", command=top.destroy).pack()

#buttons
Insert_button=Button(root,text="Insert",padx=50,pady=10,fg="white",bg="black",comman=open_insert).grid(row=1,column=1)
Select_button=Button(root,text="Select",padx=50,pady=10,fg="white",bg="black",command=open_Select).grid(row=2,column=1)
Delete_button=Button(root,text="Delete",padx=50,pady=10,fg="white",bg="black",command=open_delete).grid(row=3,column=1)
Update_button=Button(root,text="Update",padx=50,pady=10,fg="white",bg="black",command=open_update).grid(row=4,column=1)


#main


# def main():
#
#
# if __name__=='__main__':
#     main()
# shoving it onto the screen
# Title_label.pack()
# Insert_button.pack()
# Delete_button.pack()
# Select_button.pack()
# Update_button.pack()
root.mainloop()
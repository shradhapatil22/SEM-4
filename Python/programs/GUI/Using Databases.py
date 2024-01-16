from tkinter import *
import sqlite3


root=Tk()
root.title("using databases")
root.geometry("400x400")


# #create tables
# c.execute("""CREATE TABLE addresses(
#         fname text,
#         lname text,
#         address text
#         )""")


#  submit function
def submit():
    # connect the database
    conn = sqlite3.connect('address_book.db')
    # cursor
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:Address)",
    {
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'Address': Address.get()
    })


    # Commit changes
    conn.commit()

    # close connection
    conn.close()
    f_name.delete(0, END)
    l_name.delete(0, END)
    Address.delete(0, END)



# text boxes and labels
label1= Label(root,text="Enter first name:").grid(row=0,column=0)
f_name=Entry(root,width=30).grid(row=1,column=0,padx=20)
label2= Label(root,text="Enter last name:").grid(row=2,column=0)
l_name=Entry(root,width=30).grid(row=3,column=0,padx=20)
label3=Label(root,text="Enter address:").grid(row=4,column=0)
Address=Entry(root,width=30).grid(row=5,column=0,padx=20)

# buttons
submit_btn=Button(root, text="Add record to database",command=submit).grid(row=6,column=0)



root.mainloop()
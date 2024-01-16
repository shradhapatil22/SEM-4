from tkinter import *
from tkinter import ttk


class PharmacyManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1530x1530")

        Title_label = Label(self.root, text="Pharmacy Management System",bd=15,relief=RIDGE,fg="white",bg="green",padx=2,pady=4)
        Title_label.pack(side=TOP,fill=X)

        #Data frame
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,text="Medicine Information",bd=10,relief=RIDGE)
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        DataFrameRight = LabelFrame(DataFrame, text="Medicine Add Department", bd=10, relief=RIDGE)
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        #Button frame
        ButtonDataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        ButtonDataFrame.place(x=0, y=520, width=1530, height=65)

        #Buttons
        btnAdd=Button(ButtonDataFrame,text="Add Medicine").grid(row=0,column=0)
        btnUpdate = Button(ButtonDataFrame, text="Update Medicine").grid(row=0, column=1)
        btnDelete = Button(ButtonDataFrame, text="Delete Medicine").grid(row=0, column=2)

        #search by
        btnSearch = Button(ButtonDataFrame, text="Search By").grid(row=0, column=3)
        search_combo=ttk.Combobox(ButtonDataFrame,width=12,state="read").grid(row=0,column=4)

        # options=["NAME","COST","TYPE","MANUFACTURING_DATE","MANUFACTURER_NAME","EXPIRY_DATE"]
        # clicked=StringVar()
        # clicked.set(options[0])
        # drop=OptionMenu(ButtonDataFrame,clicked,*options)
        # drop.pack(pady=20)

        # search_combo["values"]=("NAME","COST","TYPE","MANUFACTURING_DATE","MANUFACTURER_NAME","EXPIRY_DATE")
        # search_combo.current(0)
        btnSearchtxt = Button(ButtonDataFrame, text="").grid(row=0, column=7)
        btnSearch = Button(ButtonDataFrame, text="Search").grid(row=0, column=8)
        btnShowAll = Button(ButtonDataFrame, text="Show All").grid(row=0, column=9)

        #labels and entry
        labelName=Label(DataFrameLeft,text="Name of the drug",padx=2).grid(row=0,column=0)
        Name=Entry(DataFrameLeft,width=30,bg="black",fg="white").grid(row=0,column=1)

        labelCOST = Label(DataFrameLeft, text="COST", padx=2).grid(row=1, column=0)
        COST = Entry(DataFrameLeft, width=30, bg="black", fg="white").grid(row=1,column=1)

        labelTYPE = Label(DataFrameLeft, text="TYPE of the drug", padx=2).grid(row=2, column=0)
        TYPE = Entry(DataFrameLeft, width=30, bg="black", fg="white").grid(row=2,column=1)

        labelMANUFACTURING_DATE = Label(DataFrameLeft, text="MANUFACTURING DATE of the drug", padx=2).grid(row=3, column=0)
        MANUFACTURING_DATE = Entry(DataFrameLeft, width=30, bg="black", fg="white").grid(row=3,column=1)

        labelMANUFACTURER_NAME = Label(DataFrameLeft, text="MANUFACTURER_NAME of the drug", padx=2).grid(row=4, column=0)
        MANUFACTURER_NAME = Entry(DataFrameLeft, width=30, bg="black", fg="white").grid(row=4,column=1)

        labelEXPIRY_DATE = Label(DataFrameLeft, text="EXPIRY_DATE of the drug", padx=2).grid(row=5, column=0)
        EXPIRY_DATE = Entry(DataFrameLeft, width=30, bg="black", fg="white").grid(row=5,column=1)

        labelName = Label(DataFrameRight, text="Name of the drug", padx=2).place(x=0,y=80)
        Name = Entry(DataFrameLeft, width=30, bg="black", fg="white").place(x=135,y=80)

        labelCOST = Label(DataFrameRight, text="Name of the drug", padx=2).place(x=900, y=80)
        cost = Entry(DataFrameLeft, width=30, bg="black", fg="white").place(x=700, y=110)


        #Table frame
        Table_Frame=Frame(self.root,bd=15,relief=RIDGE)
        Table_Frame.place(x=0,y=1,width=1460,height=180)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=x)
        column = ("NAME", "COST", "TYPE", "MANUFACTURING_DATE", "MANUFACTURER_NAME", "EXPIRY_DATE")
def main():
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()

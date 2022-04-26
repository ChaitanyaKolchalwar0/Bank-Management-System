from email import message
import tkinter as tk
from tkinter import *
from tkcalendar import DateEntry
from datetime import date
from tkinter import messagebox
import re
import pypyodbc as odbc
import random
import os
from pandas import DataFrame
import pandas as pd


conn = odbc.connect('Driver={SQL Server};'

                        'Server=ZIL1197\MSSQLDEV2019;'

                        'Database=BankManagement;'

                        'Trusted_connection=yes;')

root=tk.Tk()
root.title('Bank Management System')
root.geometry("400x400")

frame=tk.Frame(root)
frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)





def Passbook():

    # root=Tk()
    # root.geometry("300x300")
    # root.title('Bank Management System')


    Label(root,text="Passbook", width=20,font=("bold",20)).grid(row=0,column=1)
    AccountNum=Label(root,text="Account No:", width=20,font=("bold",10))
    AccountNum.place(x=5,y=50)

    AccountNo=Entry(root)
    AccountNo.place(x=50,y=90)

    def getvalues():
        cursor = conn.cursor()
        cursor.execute('exec Passbook @AccountNum='+str(AccountNo.get()))
        # data = cursor.fetchall()
        
        data=[list(i) for i in cursor.fetchall()]
        print(data)
        df=pd.DataFrame(data,columns=["     Date     ","   Amount ","     Balance "])
        print(df)


        if not data :
            messagebox.showerror("","Account Number is Not Valid")


        else:
            

            label=Label(root, text="", font=('Calibri 12'))
            label.place(x=10,y=150)
            label.config(text=str(df))
            

    Button(root, text='Submit' , width=16,bg="black",fg='white',font=("bold",10),command= lambda : getvalues()).place(x=250,y=75)
    # root.mainloop()
Passbook()

root.mainloop()



    


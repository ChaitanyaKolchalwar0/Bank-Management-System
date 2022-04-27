import sys
import pypyodbc as odbc
import random
import datetime
from email import message
import tkinter as tk
from tkinter import *
from tkcalendar import DateEntry
from datetime import date
from tkinter import messagebox


now = datetime.datetime.now()

conn = odbc.connect('Driver={SQL Server};'

                        'Server=ZIL1173\MSSQLDEV2019;'

                        'Database=Bankmanagement;'

                        'Trusted_connection=yes;')

cursor = conn.cursor()



##########################################################################
from queue import PriorityQueue
from tkinter import *
from tkinter import messagebox

root = Tk() 
# root.title("Transaction")
root.geometry("400x400")

Label(root,text="TRANSACTIONS", width=20,font=("bold",25)).grid(row=0,column=1)
AccountNum=Label(root,text="Account No:", width=20,font=("bold",10))
AccountNum.place(x=30,y=80)

AccountNum=Entry(root)
AccountNum.place(x=170,y=80)



type_label=Label(root,text="Transaction Type:",width=20,font=("bold",10))
type_label.place(x=0,y=120)
type_of_Transaction=['Withdraw','Deposit']
typetran=StringVar()
droplist=OptionMenu(root,typetran, *type_of_Transaction)
droplist.config(width=15)
typetran.set('Transaction')
droplist.place(x=20,y=140)

amount = Label(root,text="Amount:", width=20,font=("bold",10))
amount.place(x=220,y=120)
Amount = Entry(root)
Amount.place(x=250,y=140)



# typetran = input('Enter withdraw and deposit: ')

def Transaction():
    TransactionID = 'BMS'+ str(random.randint(100, 10000))
    # AccountNum = input('Enter Account Number: ')
    # Amount = int(input('Enter Amount to Withdraw or Deposit: '))
    # Transaction_date = input('Enter Date: ')
    # print(typetran)
    print(typetran.get())
    cursor=conn.cursor()
    cursor.execute('select sum(Amount) from Transactions where AccountNum='+str(AccountNum.get()))
    myresult = cursor.fetchone()



    if typetran.get() == 'Withdraw':
        Balance = float(myresult[0])-float(Amount.get())
        if Balance < 0:
            messagebox.showinfo("",'Your Balance is insufficient to withdraw this amount')
        else:
            cursor.execute('insert into Transactions(TransactionID,AccountNum,Amount) values (?,?,?)',(TransactionID,AccountNum.get(), -float(Amount.get())))
            conn.commit()
            messagebox.showinfo("",'Amount Debited : '+str(Amount.get())+'Rs')
    elif typetran.get()=='Deposit':
        cursor.execute('insert into Transactions(TransactionID,AccountNum,Amount) values (?,?,?)',(TransactionID,AccountNum.get(),float(Amount.get())))
        conn.commit()
        messagebox.showinfo("",'Amount Credited : '+str(Amount.get())+'Rs')


    
Button(root, text='Submit' , width=20,bg="black",fg='white',font=("bold",10),command= lambda : Transaction()).place(x=110,y=220)
root.mainloop()




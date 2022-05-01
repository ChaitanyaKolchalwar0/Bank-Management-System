from modulefinder import Module
from queue import PriorityQueue
import sys
from turtle import width
import pypyodbc as odbc
from email import message
import tkinter as tk
from tkinter import *
from tkcalendar import DateEntry
from datetime import date
from tkinter import messagebox
import re 

conn = odbc.connect('Driver={SQL Server};'

                        'Server=ZIL1173\MSSQLDEV2019;'

                        'Database=Bankmanagement;'

                        'Trusted_connection=yes;')


root=tk.Tk()
root.title('Bank Management System')
root.geometry("500x600")
root.config(bg='light blue')
# frame=tk.Frame(root)
# frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)

Label(root,text="update Details", width=20,font=("bold",20)).grid(row=0,column=1)
AccountNo=Label(root,text="Account No:", width=20,bg='light blue',font=("bold",10))
AccountNo.place(x=80,y=60)
AccountNo=Entry(root,width=20)
AccountNo.place(x=210,y=60)

# Phone_number=Entry(root,width=20)
# Phone_number.place(x=0,y=80)

# Address1=Entry(root,width=20)
# Address1.place(x=60,y=100)

# Address2=Entry(root,width=20)
# Address2.place(x=60,y=100)

# Pincode=Entry(root,width=20)
# Pincode.place(x=60,y=100)
# # Account type
# Phone_number = int('Enter your new phone number: ')
# list_of_account_type=[ 'PhoneNumber' ,'Address1','Address2','Pincode']
# Actype=StringVar()
# droplist=OptionMenu(root,Actype, *list_of_account_type)
# droplist.config(width=15)
# Actype.set('Select')
# droplist.place(x=200,y=420)



def update_account():

    
    # root = Tk()
    # root.geometry("500x600")

    
    # root.title('Bank Management System')

    label_0 =Label(root,text="Update Account Details", width=33,bg='orange',font=("bold",20))
    label_0.place(x=0,y=0)


   
    ################################# Second Row #############################################

    phno =Label(root,text="Phone Number", width=20,bg='light blue',font=("bold",10))
    phno.place(x=15,y=130)
    phoneNo=Entry(root)
    phoneNo.place(x=50,y=160)

 
    # Email
    email =Label(root,text="E-mail", width=20,bg='light blue',font=("bold",10))
    email.place(x=300,y=130)
    Email=Entry(root)
    Email.place(x=350,y=160)

   

    ################################# Fourth Row #############################################

    # plot no
    plno =Label(root,text="Plot.No", width=20,bg='light blue',font=("bold",10))
    plno.place(x=0,y=220)
    Plno=Entry(root)
    Plno.place(x=50,y=250)

    # Address line 1
    line1 =Label(root,text="Address line 1", width=20,bg='light blue',font=("bold",10))
    line1.place(x=160,y=220)
    L1_Address=Entry(root)
    L1_Address.place(x=200,y=250)

    # Address line 2
    line2 =Label(root,text="Address line 2", width=20,bg='light blue',font=("bold",10))
    line2.place(x=310,y=220)
    L2_Address=Entry(root)
    L2_Address.place(x=350,y=250)

    ################################# Fifth Row ###############################################

    # Pincode
    pinCode =Label(root,text="PinCode", width=20,bg='light blue',font=("bold",10))
    pinCode.place(x=0,y=320)
    Pincode=Entry(root)
    Pincode.place(x=50,y=350)

    # City
    city =Label(root,text="City", width=20,bg='light blue',font=("bold",10))
    city.place(x=160,y=320)
    City=Entry(root)
    City.place(x=200,y=350)

    # State
    state_label =Label(root,text="State", width=20,bg='light blue',font=("bold",10))
    state_label.place(x=310,y=320)
    State=Entry(root)
    State.place(x=350,y=350)
    
      ##this creates 'Label' widget for country and uses place() method.
    label_5=Label(root,text="Nationality",width=20,bg='light blue',font=("bold",10))
    label_5.place(x=0,y=400)

    #this creates list of countries available in the dropdownlist.
    list_of_country=[ 'India' ,'US' , 'UK' ,'Germany' ,'Austria']

    #the variable 'c' mentioned here holds String Value, by default ""
    country=StringVar()
    droplist=OptionMenu(root,country, *list_of_country)
    droplist.config(width=15)
    country.set('Select your Country')
    droplist.place(x=50,y=420)

    # Account type
    type_label=Label(root,text="Account Type",width=20,bg='light blue',font=("bold",10))
    type_label.place(x=270,y=400)
    list_of_account_type=[ 'Savings Account' ,'Current Account']
    Actype=StringVar()
    droplist=OptionMenu(root,Actype, *list_of_account_type)
    droplist.config(width=15)
    Actype.set('Select Account Type')
    droplist.place(x=310,y=420)

    def get_data():


        # # Get the Full name
        # name = Fname.get() +' '+ Mname.get() +' '+ Lname.get()
        # if re.search('[1234567890!@#$%^&*()_+;:.,/?]',name):
        #     messagebox.showerror("","Enter a valid name")
            
        # else:
        #     Fname_final = Fname.get()
        #     Mname_final = Mname.get()
        #     Lname_final = Lname.get()
            
        # Get Phone Number 
        # print(phoneNo.get())
        if len(str(phoneNo.get())) == 10:
            phoneNo_final = int(phoneNo.get())
        
        else:
            messagebox.showerror("","Enter a Valid Number")

        # print(cal.get_date())
        # Date_Of_Birth = str(cal.get_date())
        # age = str(Date_Of_Birth).split("-") 
        # Age = today.year -  int(age[0])
        # Age_Final = Age
          
            
        check_email = re.search("[a-z0-9]+[@]+[a-z]+\.com", Email.get())
        if check_email:
            Email_final = Email.get()
        else:
            messagebox.showerror("","Enter a Valid Email Address")

            
        # Aadhaar_final = int(Aadhaar.get())
        # Balance = 0
        PinCode_final = int(Pincode.get())

        

        cursor = conn.cursor()
        cursor.execute( "EXEC Updateinfo @AccountNum=?,@PhoneNo=?,@Email=?,@Plot_Num=?,@L1_Address=?,@L2_Address=?,@Pincode=?,@City=?,@State=? ,@Nationality=?,@Account_type=?", (1,phoneNo_final,Email_final,Plno.get(),L1_Address.get(),L2_Address.get(),PinCode_final,City.get(),State.get(),country.get(),Actype.get()))
        conn.commit()
        cursor.execute('select * from Updateinfo')

        messagebox.showinfo("","Account updated")




    #this creates button for submitting the details provides by the user
    Button(root, text='Submit' , width=20,bg="orange",font=("bold",10),fg='light blue',command= lambda : get_data()).place(x=180,y=500)
    #this will run the mainloop.
    # root.mainloop()





    

    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='Menu', menu=filemenu)
    # filemenu.add_command(label='Create Account',command=create_account)
    # filemenu.add_separator()
    # filemenu.add_command(label='Delete Account',command=delete_account)
    # filemenu.add_separator()
    filemenu.add_command(label='Update Details',command=update_account)
    filemenu.add_separator()
    # filemenu.add_command(label='Exit', command=root.quit)







Button(root, text='Submit' , width=20,bg="light blue",font=("bold",10),fg='black',command= lambda : update_account()).place(x=180,y=500)
cursor = conn.cursor()
# cursor.execute('exec Updateinfo'+PhoneNo+' '+Email+' '+Plot_Num+' '+L1_Address+' '+L2_Address+' '+Pincode+' '+City+' '+State+' '+Nationality+' '+Account_type+')
                
conn.commit()
update_account()
root.mainloop()











# @AccountNum int,@PhoneNo bigint, @Email varchar(35),
# @Plot_Num varchar(15), @L1_Address varchar(255),@L2_Address varchar(255),@Pincode int,@City Varchar(25),
# @State Varchar(35),@Nationality varchar(25),@Account_type varchar(35)
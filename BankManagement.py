""" 
Authers: Arpita Gadekar,Chaitanya Kolchalwar, Piyush Lanjewar, Adarsh Gadge, Suveg Nimje
File Name: BankManagement.py
"""


import tkinter as tk
from tkinter import *
from tkcalendar import DateEntry
from datetime import date
from tkinter import messagebox
import re
import pypyodbc as odbc
import pandas as pd

""" Establishing Connection between the SSMS and Python Using PYODBC Module """


conn = odbc.connect('Driver={SQL Server};'

                        'Server=ZIL1225\MSSQLDEV2019;'

                        'Database=BankManagement;'

                        'Trusted_connection=yes;')

""" Initializing the Tkinter window  """

root=tk.Tk()
root.title('Bank Management System')
root.geometry("300x300")

frame=tk.Frame(root)
frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)

"""   
Function name: customer_details()

"""

def customer_details():
    root=Tk()
    root.geometry("500x600")
    root.title('Bank Management System')



    Label(root,text="Customer Details", width=20,font=("bold",20)).grid(row=0,column=1)
    AccountNo=Label(root,text="Account No:", width=20,font=("bold",10))
    AccountNo.place(x=0,y=60)

    AccountNo2=Entry(root,width=20)
    AccountNo2.place(x=60,y=100)

    label=Label(root, text="", font=('Calibri 12'))
    label.place(x=10,y=150)

    label1=Label(root, text="", font=('Calibri 12'))
    label1.place(x=10,y=170)

    label2=Label(root, text="", font=('Calibri 12'))
    label2.place(x=10,y=200)

    label3=Label(root, text="", font=('Calibri 12'))
    label3.place(x=10,y=220)
    
    label4=Label(root, text="", font=('Calibri 12'))
    label4.place(x=10,y=250)
    
    label5=Label(root, text="", font=('Calibri 12'))
    label5.place(x=10,y=270)
    
    label6=Label(root, text="", font=('Calibri 12'))
    label6.place(x=10,y=290)
    
    label7=Label(root, text="", font=('Calibri 12'))
    label7.place(x=10,y=310)
    
    label8=Label(root, text="", font=('Calibri 12'))
    label8.place(x=10,y=330)
    
    label9=Label(root, text="", font=('Calibri 12'))
    label9.place(x=10,y=360)
    
    label10=Label(root, text="", font=('Calibri 12'))
    label10.place(x=10,y=390)
    
    label11=Label(root, text="", font=('Calibri 12'))
    label11.place(x=10,y=420)
    


    def getvalues():
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Create_Account WHERE AccountNum ='+str(AccountNo2.get()))
        data = list(sum(cursor.fetchall(),()))
        print(data)
        

        if not data:
            messagebox.showerror("","Account not Available")
        
        else:

            label.config(text="Account Number   : "+ str(data[0]))
            label1.config(text="Name            : "+ data[1]+" "+data[2]+" "+data[3])
            label2.config(text="Mobile NO.       : "+ str(data[4]))
            label3.config(text="Email            : "+str(data[5]))
            label4.config(text="Gender           : " +str(data[6]))
            label5.config(text="Age              : "+str(data[7]))
            label6.config(text="Date of Birth    : "+str(data[18]))
            label7.config(text="Address          : "+str(data[8])+", "+data[9]+", "+data[10]+", "+ data[12]+"-"+str(data[11])+" "+data[13]+".")
            label8.config(text="Country          : "+ str(data[14]))
            label9.config(text="Account Type     : "+str(data[15]))
            label10.config(text="Aadhar Card No   : "+str(data[16]))
            label11.config(text="PAN Number       : "+str(data[17]))          

    Button(root, text='Submit' , width=16,bg="black",fg='white',font=("bold",10),command= lambda : getvalues()).place(x=200,y=95)
    root.mainloop()


def delete_account():
    root=Tk()
    root.geometry("300x300")
    root.title('Bank Management System')

    Label(root,text="Delete Account", width=20,font=("bold",20)).grid(row=0,column=1)
    AccountNo=Label(root,text="Account No:", width=20,font=("bold",10))
    AccountNo.place(x=0,y=60)

    AccountNo1=Entry(root)
    AccountNo1.place(x=100,y=100)

    def getvals():
        cursor = conn.cursor()
        cursor.execute('select AccountNum from Create_Account')
        data = cursor.fetchall()
        print(list(data))
       
        if not data :
            messagebox.showerror("","Account Number is Not Valid")
         
        else:
            sql="delete from Create_Account where AccountNum="+str(AccountNo1.get())
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            messagebox.showinfo("","Account Deleted")
            

    Button(root, text='Submit' , width=20,bg="black",fg='white',font=("bold",10),command= lambda : getvals()).place(x=100,y=200)
    root.mainloop()

def create_account():

    # def acnt():
    #     global x,y,AccountNO 
    #     x = random.randint(1,1000)
    #     y = 88887777 
        
    #     AccountNO = x+y

    # acnt()

    #Creating object 'root' of Tk()
    root = Tk()
    root.geometry("500x600")

    # bg = ImageTk.PhotoImage(Image.open(r"C:\Users\chaitanya.kolchalwar\Desktop\Python Training\BankManagement\testing.png")) 

    
    # # Create Canvas
    # canvas1 = Canvas( root, width = 500,
    #                  height = 500)
    
    # canvas1.pack(fill = "both", expand = True)
    
    # # Display image
    # canvas1.create_image( 0, 0, image = bg, 
    #                      anchor = "nw")
    
    root.title('Bank Management System')

    label_0 =Label(root,text="Create Account", width=20,font=("bold",20))
    label_0.place(x=60,y=0)

    ################################ First row #############################################

    fname =Label(root,text="FirstName", width=20,font=("bold",10))
    fname.place(x=0,y=50)
    Fname=Entry(root)
    Fname.place(x=50,y=80)


    mname =Label(root,text="MiddleName", width=20,font=("bold",10))
    mname.place(x=150,y=50)
    Mname=Entry(root)
    Mname.place(x=200,y=80)


    lname =Label(root,text="LastName", width=20,font=("bold",10))
    lname.place(x=300,y=50)
    Lname=Entry(root)
    Lname.place(x=350,y=80)

    ################################# Second Row #############################################

    phno =Label(root,text="Phone Number", width=20,font=("bold",10))
    phno.place(x=15,y=130)
    phoneNo=Entry(root)
    phoneNo.place(x=50,y=160)

    # Current Date
    today = date.today()
    year1 = today.year
    day1 = today.day
    mnth1 = today.month

    # Calendar 
    cal1 =Label(root,text="DOB", width=20,font=("bold",10))
    cal1.place(x=140,y=130)
    cal = DateEntry(root, width=12, year=year1, month=mnth1, day=day1, 
    background='darkblue', foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=160)

    # Email
    email =Label(root,text="E-mail", width=20,font=("bold",10))
    email.place(x=300,y=130)
    Email=Entry(root)
    Email.place(x=350,y=160)

    # ################################# Third Row #############################################

    Gender =Label(root,text="Gender:", width=20,font=("bold",10))
    Gender.place(x=0,y=200)
    var=IntVar()
    Radiobutton(root,text="Male",padx= 5, variable= var, value=1).place(x=40,y=220)
    Radiobutton(root,text="Female",padx= 20, variable= var, value=2).place(x=100,y=220)

    # Aadhar number
    adhar =Label(root,text="Aadhaar.No", width=20,font=("bold",10))
    adhar.place(x=150,y=200)
    Aadhaar=Entry(root)
    Aadhaar.place(x=200,y=230)



    # pancard number
    pancard =Label(root,text="PanCard", width=20,font=("bold",10))
    pancard.place(x=300,y=200)
    PanCard=Entry(root)
    PanCard.place(x=350,y=230)

    ################################# Fourth Row #############################################

    # plot no
    plno =Label(root,text="Plot.No", width=20,font=("bold",10))
    plno.place(x=0,y=260)
    Plno=Entry(root)
    Plno.place(x=50,y=290)

    # Address line 1
    line1 =Label(root,text="Address line 1", width=20,font=("bold",10))
    line1.place(x=160,y=260)
    L1_Address=Entry(root)
    L1_Address.place(x=200,y=290)

    # Address line 2
    line2 =Label(root,text="Address line 2", width=20,font=("bold",10))
    line2.place(x=310,y=260)
    L2_Address=Entry(root)
    L2_Address.place(x=350,y=290)

    ################################# Fifth Row ###############################################

    # Pincode
    PinCode =Label(root,text="PinCode", width=20,font=("bold",10))
    PinCode.place(x=0,y=320)
    Pincode=Entry(root)
    Pincode.place(x=50,y=350)

    # City
    city =Label(root,text="City", width=20,font=("bold",10))
    city.place(x=160,y=320)
    City=Entry(root)
    City.place(x=200,y=350)

    # State
    state_label =Label(root,text="State", width=20,font=("bold",10))
    state_label.place(x=310,y=320)
    State=Entry(root)
    State.place(x=350,y=350)

    ##this creates 'Label' widget for country and uses place() method.
    label_5=Label(root,text="Nationality",width=20,font=("bold",10))
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
    type_label=Label(root,text="Account Type",width=20,font=("bold",10))
    type_label.place(x=160,y=400)
    list_of_account_type=[ 'Savings Account' ,'Current Account']
    Actype=StringVar()
    droplist=OptionMenu(root,Actype, *list_of_account_type)
    droplist.config(width=15)
    Actype.set('Select Account Type')
    droplist.place(x=200,y=420)

    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='Menu', menu=filemenu)
    # filemenu.add_command(label='Create Account',command=create_account)
    # filemenu.add_separator()
    filemenu.add_command(label='Delete Account',command=delete_account)
    filemenu.add_separator()
    filemenu.add_command(label='Customer Details',command=customer_details)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=root.quit)


    def get_data():


        # Get the Full name
        name = Fname.get() +' '+ Mname.get() +' '+ Lname.get()
        if re.search('[1234567890!@#$%^&*()_+;:.,/?]',name):
            messagebox.showerror("","Enter a valid name")
            
        else:
            Fname_final = Fname.get()
            Mname_final = Mname.get()
            Lname_final = Lname.get()
            
        # Get Phone Number 
        # print(phoneNo.get())
        if len(str(phoneNo.get())) == 10:
            phoneNo_final = int(phoneNo.get())
        
        else:
            messagebox.showerror("","Enter a Valid Number")

        print(cal.get_date())
        Date_Of_Birth = str(cal.get_date())
        age = str(Date_Of_Birth).split("-") 
        Age = today.year -  int(age[0])
        Age_Final = Age
          
            
        check_email = re.search("[a-z0-9]+[@]+[a-z]+\.com", Email.get())
        if check_email:
            Email_final = Email.get()
        else:
            messagebox.showerror("","Enter a Valid Email Address")

            
        if var.get() == 1:
            Gender_final = 'Male'
        elif var.get() == 2:
            Gender_final = 'Female'

        Aadhaar_final = int(Aadhaar.get())
        Balance = 0
        PinCode_final = int(Pincode.get())
        

        cursor = conn.cursor()
        cursor.execute( "EXEC CREATEACCOUNT @First_name=?,@Middle_name=?,@Last_name=?,@PhoneNo=?,@Email=?,@Gender=?,@Age=?,@Plot_Num=?,@L1_Address=?,@L2_Address=?,@Pincode=?,@City=?,@State=? ,@Nationality=?,@Account_type=? ,@Aadhaar=? ,@PanCard=? ,@Date_of_Birth=? ,@Balance=?;", (Fname_final,Mname_final,Lname_final,phoneNo_final,Email_final,Gender_final,Age_Final,Plno.get(),L1_Address.get(),L2_Address.get(),PinCode_final,City.get(),State.get(),country.get(),Actype.get(),Aadhaar_final,PanCard.get(),Date_Of_Birth,Balance))
        conn.commit()
        cursor.execute('select * from Create_Account')
    

        table=[list(i) for i in cursor.fetchall()]
        df=pd.DataFrame(table,columns=["AccountNum","First_name","Middle_name","Last_name","PhoneNo","Email","Gender","Age","Plot_Num","L1_Address","L2_Address","Pincode","City","State","Nationality","Account_type","Aadhaar","PanCard","Date_of_Birth","Balance"])

        print(df)

        messagebox.showinfo("","Account Created")


    #this creates button for submitting the details provides by the user
    Button(root, text='Submit' , width=20,bg="black",font=("bold",10),fg='white',command= lambda : get_data()).place(x=180,y=500)
    #this will run the mainloop.
    # root.mainloop()



def login():
    def credential():

        uname = username.get()
        password = pswd.get()
        if(uname == "" and password == "") :
            messagebox.showerror("", "Both the field are required")

        elif(uname == "Perficient" and password == "1234"):
            messagebox.showinfo("","Login Successfull")
            root.destroy()
            create_account()
        
        elif(uname == "Admin" and password == "Admin"):
            messagebox.showinfo("","Login Successfull")
            root.destroy()
            create_account()
            
        else :
            messagebox.showerror("","Incorrent Username OR Password")


    Label(root, text="UserName*").place(x=35, y=20)
    Label(root, text="Password*").place(x=35, y=50)

    username = Entry(root)
    username.place(x=130, y=25)

    pswd = Entry(root)
    pswd.place(x=130, y=55)
    pswd.config(show="*")

    
    tk.Button(root, text="Login", command=credential ,height = 2, width = 15,bg='lightblue').place(x=100, y=120)
login()
root.mainloop()
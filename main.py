
from calendar import month
from tkinter import *
from tkcalendar import DateEntry
from datetime import date
from tkinter import messagebox
from PIL import ImageTk, Image

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

################################# Third Row #############################################
Gender =Label(root,text="Gender:", width=20,font=("bold",10))
Gender.place(x=0,y=200)
var=IntVar()
Radiobutton(root,text="Male",padx= 5, variable= var, value=1).place(x=40,y=220)
Radiobutton(root,text="Female",padx= 20, variable= var, value=2).place(x=100,y=220)

# Plot number
adhar =Label(root,text="Aadhaar.No", width=20,font=("bold",10))
adhar.place(x=150,y=200)
Aadhaar=Entry(root)
Aadhaar.place(x=200,y=230)


# Address line 1
pancard =Label(root,text="PanCard", width=20,font=("bold",10))
pancard.place(x=300,y=200)
PanCard=Entry(root)
PanCard.place(x=350,y=230)

################################# Fourth Row #############################################
# plot no
plno =Label(root,text="Plot.No", width=20,font=("bold",10))
plno.place(x=0,y=260)
plno=Entry(root)
plno.place(x=50,y=290)

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

################################# Fifth Row #############################################
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

# Address line 2
state_label =Label(root,text="State", width=20,font=("bold",10))
state_label.place(x=310,y=320)
state=Entry(root)
state.place(x=350,y=350)

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


def get_data():
    messagebox.showinfo("","Account Created")
    print(Fname.get())
    print(Mname.get())
    print(Lname.get())
  
    name  = Fname.get() + ' ' + Mname.get() + ' ' + Lname.get()
    print(name)
    print(phoneNo.get())
    print(cal.get_date())

    if var.get() == 1:
        print('Male')
    elif var.get() == 2:
        print('Female')



#this creates button for submitting the details provides by the user
Button(root, text='Submit' , width=20,bg="black",font=("bold",10),fg='white',command= lambda : get_data()).place(x=180,y=500)
#this will run the mainloop.
root.mainloop()
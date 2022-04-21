import pypyodbc as odbc
import pandas as pd

conn = odbc.connect('Driver={SQL Server};'

                        'Server=ZIL1184\MSSQLDEV2019;'

                        'Database=BankManagement;'

                        'Trusted_connection=yes;')

def displayAccountDetails():
    AccountNO = int(input("Enter your account number: "))

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Create_Account WHERE AccountNum = {}'.format(AccountNO))

    for i in cursor:
        pass
    print("Account Number   :", i[0])
    print("Name             : ", i[1]+" "+i[2]+" "+i[3])
    print("Mobile NO.       : ", i[4])
    print("Emial            : ", i[5])
    print("Gender           : ", i[6])
    print("Age              : ", i[7])
    print("Date of Birth    : ", i[18])
    print("Address          : ",str(i[8])+", "+i[9]+", "+i[10]+", "+ i[12]+"-"+str(i[11])+" "+i[13]+".")
    print("Country          : ", i[14])
    print("Account Type     : ", i[15])
    print("Aadhar Card No   : ", i[16])
    print("PAN Number       : ", i[17])
    # table=[list(i) for i in cursor.fetchall()]
    # df=pd.DataFrame(table,columns=["AccountNum","First_name","Middle_name","Last_name","PhoneNo","Email","Gender","Age","Plot_Num","L1_Address","L2_Address","Pincode","City","State","Nationality","Account_type","Aadhaar","PanCard","Date_of_Birth","Balance"])



    # print(df)
    
displayAccountDetails()
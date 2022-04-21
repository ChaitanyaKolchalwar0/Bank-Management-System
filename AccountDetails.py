import pypyodbc as odbc
conn = odbc.connect('Driver={SQL Server};'

                        'Server=ZIL1184\MSSQLDEV2019;'

                        'Database=BankManagement;'

                        'Trusted_connection=yes;')

def displayAccountDetails():
    AccountNO = int(input("Enter your account number: "))

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Create_Account WHERE AccountNum = {}'.format(AccountNO))

    for i in cursor:
        print(i)


displayAccountDetails()
# Bank-Management-System


## Abstract:

The Bank Account Management System is an application for maintaining a person's account in a bank. In this project we tried to show the working of a banking account system and cover the basic functionality of a Bank Account Management System. To develop a project for solving financial applications of a customer in banking environment to nurture the needs of an end banking user by providing various ways to perform banking tasks. Also, to enable the user’s workspace to have additional functionalities which are not provided under a conventional banking project.
Technologies Used: Python, SQL Server.

## 1.	Problem Statement:

The Bank management system is an application for maintaining a person’s account in a bank. The system provides an access to create an account, deposit/withdraw the cash from account. Also, to view all the account details and transactions.

## 2.	Introduction:

Bank Management System project is written in Python. it contains all the basic functions which include creating a new account, view account holders record, withdraws and deposit amount, balance inquiry, deleting an account and edit account details. 
Talking about the features of the Bank Management System, a user can create an account by providing the name of the account 

holder, number, selecting amount type (Saving account or Current account). Then the user can also deposit and withdraw money just by providing his/her account number and entering the amount. For certain purpose, he/she can also check for the balance inquiry which displays the account number and amount. Another feature is that he/she can modify their account detail and type if they want to.

## 3.	Module Description:

The Modules description of Bank Account Management System project. These modules will be developed in Python and SQL Server database.
1.	Login.
2.	Create Account.
3.	Transactions (Deposit/Withdraw).
4.	Customer Details.
5.	Passbook.
6.	Delete account.
7.	Modify Account Details.
8.	Interest Calculator.

## 4. Build With:

* Python
* SQL Server

## 5. Installation Steps:


### Clone this repository
```
$ git clone https://github.com/ChaitanyaKolchalwar0/Bank-Management-System.git
```
### Python Modules Installation
#### Pypyodbc:
```
$ pip install pypyodbc
```
#### Tkinter:
```
$ pip install tk
```
#### Pandas:
```
$ pip install pandas
```
#### Regex:
```
$ pip install regex
```
You can also refer requirements.txt.
## 6. Functions : 
* def login():
    This functions help us to login as admin.
    - Asking for username
	- Checks the conditional statement for validating username.
	- If username not found then throws the error to retype the username and password.
	- If username and password matches then, access the create account page.
		
* def create_account():
    This functions helps us to get the details from user while creating an account.
    - function to create a new user account
	- will ask the user for
		
		- First Name
		- Middle Name
		- Last Name
		- Gender
			- Male
			- Female
		- DOB(DD/MM/YYYY)
		- Address line1
		- Address line 2 
		- Pincode
		- Mobile No
			- validate the Mobile No
		- Email_Id
		- Nationality
		- Account_type
			- Saving
			- Current
						
    
* def Transaction():
    This function helps us to perform transactions like cash deposit and cash withdraw.
* def Passbook():
    This function helps us to print the transaction details which you have done till now.
* def customer_details():
    This funtion helps us to get the customer details.
* def delete_account():
    This function helps us to delete your exixting account.
* def update_account():
    This function helps us to update or modify the account details. 
* def Interest_Generate():
    This function helps us to generate interest for the respective customer.

    
  

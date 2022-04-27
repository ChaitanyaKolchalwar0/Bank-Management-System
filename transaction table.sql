--Creating Create Account Table (Customer Personal Data)

Create table Create_Account(AccountNum bigint PRIMARY KEY,
First_name Varchar(15),
Middle_name Varchar(15),
Last_name Varchar(15),
PhoneNo int,
Email varchar(35),
Gender char,
Age int,
Plot_Num varchar(15),
L1_Address varchar(255),
L2_Address varchar(255),
Pincode int,
City Varchar(25),
State Varchar(35),
Nationality varchar(25),
Account_type varchar(35),
Aadhaar bigint,
PanCard varchar(25),
Date_of_Birth date,
);

select * from Create_Account
select * from Transactions
order by Transaction_date

--Creating Transaction table
CREATE TABLE Transactions(
TransactionID VARCHAR(35) PRIMARY KEY, 
Transaction_date DATETIME DEFAULT(GETDATE()),
AccountNum bigint FOREIGN KEY REFERENCES Create_Account(AccountNum),
Amount FLOAT,
);

select sum(Amount) Amount from Transactions where AccountNum=1

insert into Transactions(TransactionID,AccountNum,Amount)
values ('BMS4456',1,4000)

--Creating a Passbook

select * from Transactions

create procedure Passbook(@AccountNum bigint)
as
begin
SELECT  Transaction_Date,
		Amount,
        SUM(isnull(Amount,0)) OVER (ORDER BY Transaction_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as Balance
FROM Transactions
where AccountNum=@AccountNum
order by Transaction_date
end


/*with cte as
(SELECT  Transaction_Date,Amount,SUM(isnull(Amount,0)) OVER (ORDER BY Transaction_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as Balance FROM Transactions
where AccountNum=1),*/

exec Passbook @AccountNum=1
select * from dbo.Passbook(@AccountNum)-- MM,YYYY

/*
IF MM = 9
STDT 1/4/YYYY
ENDT 30/MM/YYYY -30/9/YYYY
ELSE
STDT 
*/



--Creatung Interest Calculator Procedure

create procedure InterestCalculation(@AccountNum bigint)
as
begin
with cte0 as
(SELECT  AccountNum,Transaction_Date,Amount,SUM(isnull(Amount,0)) OVER (ORDER BY Transaction_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as Balance
FROM Transactions
where AccountNum=@AccountNum),
cte as
(select Transaction_date,Balance,ROW_NUMBER() OVER (PARTITION BY AccountNum order by Transaction_date) AS RowNum from cte0),
cte2 as 
(select Transaction_date,Balance,0 as Daydiff  From cte where RowNum=1
union all 
select a.Transaction_date,a.Balance,DATEDIFF(day,b.Transaction_date,a.Transaction_date) from cte a join cte b on a.RowNum=b.RowNum+1),
cte3 as 
(select Transaction_date,Balance,(case when daydiff=0 then 1 else daydiff end) Daydiff from cte2)
select sum(Balance*0.05*Daydiff/365.0) as Interest_Earned from cte3
end

/*
exec InterestCalculation @AccountNum=1

create procedure AddInterest
as
begin
exec Passbook @AccountNum=1

end
*/
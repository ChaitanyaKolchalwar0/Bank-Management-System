--CREATING CREATE ACCOUNT TABLE (CUSTOMER PERSONAL DATA)

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


-- CREATING TRANSACTION TABLE

CREATE TABLE Transactions(
TransactionID VARCHAR(35) PRIMARY KEY, 
Transaction_date DATETIME DEFAULT(GETDATE()),
AccountNum bigint FOREIGN KEY REFERENCES Create_Account(AccountNum),
Amount FLOAT,
);


-- PROCEDURE FOR PASSBOOK GENERATION

CREATE PROCEDURE Passbook(@AccountNum bigint, @Start_date date, @End_date date)
as
begin
SELECT Transaction_Date,
Amount,
SUM(isnull(Amount,0)) OVER (ORDER BY Transaction_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as Balance
FROM Transactions
where AccountNum=@AccountNum and Transaction_date between @Start_date and DATEADD(DAY, 1, @End_date)
order by Transaction_date
end;

--CREATING INTEREST CALCULATOR PROCEDURE

create procedure InterestCalculation @AccountNum bigint
as
begin
with cte0 as
(SELECT  AccountNum,Transaction_Date,Amount,SUM(isnull(Amount,0)) OVER (ORDER BY Transaction_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as Balance
FROM Transactions where AccountNum = @AccountNum),
cte as
(select Transaction_date,Balance,ROW_NUMBER() OVER (PARTITION BY AccountNum order by Transaction_date) AS RowNum from cte0),
cte2 as 
(select Transaction_date,Balance,0 as Daydiff  From cte where RowNum=1
union all
select a.Transaction_date,a.Balance,DATEDIFF(day,b.Transaction_date,a.Transaction_date) from cte a join cte b on a.RowNum=b.RowNum+1),
cte3 as
(select Transaction_date,Balance,(case when daydiff=0 then 1 else daydiff end) Daydiff from cte2)
select round(sum(Balance*0.05*Daydiff/365.0),2) as Interest_Earned from cte3
end

--exec InterestCalculation 2


--UPDATE CUSTOMER DETAILS

create procedure Updateinfo @AccountNum int,@PhoneNo bigint, @Email varchar(35),
@Plot_Num varchar(15), @L1_Address varchar(255),@L2_Address varchar(255),@Pincode int,@City Varchar(25),
@State Varchar(35),@Nationality varchar(25),@Account_type varchar(35)
as
begin
UPDATE Create_Account
SET PhoneNo=@PhoneNo,Email=@Email,Plot_Num=@Plot_Num,L1_Address=@L1_Address,L2_Address=@L2_Address,
Pincode=@Pincode,City=@City,State=@State,Nationality=@Nationality,Account_type=@Account_type
WHERE AccountNum=@AccountNum
end

-- CREATE ACCOUNT PROCEDURES

CREATE PROCEDURE CREATEACCOUNT (@First_name Varchar(15),@Middle_name Varchar(15),@Last_name Varchar(15),@PhoneNo bigint,@Email varchar(35),@Gender varchar(10),@Age int,@Plot_Num varchar(15),@L1_Address varchar(255),@L2_Address varchar(255),@Pincode int,@City Varchar(25),@State Varchar(35),@Nationality varchar(25),@Account_type varchar(35),@Aadhaar bigint,@PanCard varchar(25),@Date_of_Birth date,@Balance float)
AS
BEGIN
INSERT INTO Create_Account (First_name,Middle_name,Last_name,PhoneNo,Email,Gender,Age,Plot_Num,L1_Address,L2_Address,Pincode,City,State,Nationality,Account_type,Aadhaar,PanCard,Date_of_Birth,Balance)
values(@First_name,@Middle_name,@Last_name,@PhoneNo,@Email,@Gender,@Age,@Plot_Num,@L1_Address,@L2_Address,@Pincode,@City,@State ,@Nationality ,@Account_type ,@Aadhaar ,@PanCard ,@Date_of_Birth ,@Balance)
END;
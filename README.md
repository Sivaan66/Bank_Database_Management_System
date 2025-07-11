# Bank_Database_Management_System
This project includes taking bank realted data like customer's username, password, name, account number, phone number, age, city fromm users and inserting the detailes into a table into a created database using python by signing in or signing up. This project also includes banking falicities like checking balance, withdraw money, depositing money, fund transfering. All the transaction related data like username, account number, transaction amount, transaction date and time will get stored in a different table named with user's username.  

## Features -
### SignUP():
- Takes username, account number, password, name, age, city as inputs.
- Create a datatable in the database.
- Inserting all the data into the table using **mysql.connector.connect**
- After signup ask to signin.
### SignIN():
- Takes user's username, password as input.
- checks either username exists or not if exists checks the password matching.
- after successfull signin takes to the facility section.
## Facilities:


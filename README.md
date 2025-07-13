# Bank_Database_Management_System
This project includes taking bank realted data like customer's username, password, name, account number, phone number, age, city fromm users and inserting the detailes into a table into a created database using python by signing in or signing up. This project also includes banking falicities like checking balance, withdraw money, depositing money, fund transfering. All the transaction related data like username, account number, transaction amount, transaction date and time will get stored in a different table named with user's username.  

## Implementations:
- Username Validation
- Password validation
- Creating accountnumber
- Building Database
- Creating tables
- Updating tables
- Running SQL queries
- OOPs implementation
  
## Features :
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
### Checkbalance :
- Fetch balance according to the user's username and password.
- Get called under the class **Bank**.
  
  ```py
  def checkbalance(self) :
        balance = db_query(f" select Balance from customer where user_name = '{self.__user_name}'")
        print("Your Balance : ", balance [0][0])
  ```
### Deposite:
- Takes an integer as amount.
- Checks if user entered an integer or not.
- Then update the database.
  
  ```py
  def deposite(self):
        while True :
            try :
                amount = input("Enter the amount to be deposited :")
                if not amount.isdigit():
                    raise ValueError("Enter Digits only")
                acc_number = int(self.__acc_number)
                amount_int = int (amount)
                db_query(f"""insert into {self.__user_name}_HISTORY (user_name, acc_number, amount, transaction_time, remark) 
                         values('{self.__user_name}',{acc_number}, {amount_int}, '{datetime.datetime.now().strftime('%y-%m-%d,%H:%M:%S')}', 'Deposited')""") 
                balance = db_query(f" select Balance from customer where user_name = '{self.__user_name}'")
                new_balance = int(balance[0][0]) + int(amount)
                
                db_query(f"update customer set Balance = '{new_balance}' where user_name = '{self.__user_name}'")
                print(f"Your new Balance is :", new_balance)
                break

            except ValueError as e :
                print("Invalid Input :", e)
  ```
### Withdraw:
- Takes an integer as amount.
- Checks if user has enough balance or not.
- Checks if user entered a valid input like integer or not.
- Then updates the database.
  
  ```py
  def withdraw(self):
        while True :
            try :
                amount = input("Enter the amount to be deposited :")
                if not amount.isdigit():
                    raise ValueError("Enter Digits only")
                
                balance = db_query(f" select Balance from customer where user_name = '{self.__user_name}'")

                if int(balance[0][0]) < int(amount) :
                    raise ValueError("Not enough money. Deposite!")
                
                acc_number = int(self.__acc_number)
                amount_int = int (amount)
                db_query(f"""insert into {self.__user_name}_HISTORY (user_name, acc_number, amount, transaction_time, remark) 
                         values('{self.__user_name}',{acc_number}, {amount_int}, '{datetime.datetime.now().strftime('%y-%m-%d,%H:%M:%S')}', 'Withdrawn')""") 
                
                new_balance = int(balance[0][0]) - int(amount)
                
                db_query(f"update customer set Balance = '{new_balance}' where user_name = '{self.__user_name}'")
                print(f"Your new Balance is :", new_balance)
                break

            except ValueError as e :
                print("Invalid Input :", e)
  ```
### Fund transfer:
- Asks for sender's username and password.
- Checks if sender input is valid or not.
- Checks if The password is valid and matching to the database.
- Asks reviever's username and account number.
- checks if sender has enough money to send or not.
- Then updates the database.
  
  ```py
  def fundtransfer(self):
        while True:
            print(" You will need other person's username and acount number to transer money.")
            user_name = input("Enter your username :")
            temp_user = db_query(f"select user_name from customer where user_name = '{user_name}'")
            if temp_user:
                password = input("Enter your password :")
                temp_pass = db_query(f"select password from customer where user_name = '{user_name}'")
                if temp_pass[0][0] == password:
                    try:
                        amount = input("Enter the amount to transfer:")

                        if not amount.isdigit():
                            raise ValueError("Only numbers are valid.")
                        
                        user2 = input("Enter the other person's username :")
                        temp_user2 = db_query(f"select password from customer where user_name = '{user2}'")
                        if temp_user2:
                            try: 
                                acc2 = input("Enter their account number :")
                                temp_acc2 = db_query(f"select acc_number from customer where user_name = '{user2}'")

                                if temp_acc2[0][0] == acc2:
                                    balance = db_query(f"select balance from customer where user_name = '{user_name}'")
                                    try:
                                        if int(balance[0][0]) < int(amount):
                                            raise ValueError("You need more", int(amount)-int(balance[0][0]),"Rs. to proceed")
                                        
                                        user_balance = int(balance[0][0]) - int(amount)
                                        db_query(f"update customer set balance = '{user_balance}' where user_name = '{user_name}'")

                                        print("Your balance:", balance[0][0])

                                    except ValueError as e :
                                        print("Not enough balance to transfer.",e)

                                    balance2 = db_query(f"select balance from customer where user_name = '{user2}'")
                                    user_balance2 = int(balance2[0][0]) + int(amount)
                                    db_query(f"update customer set balance = '{user_balance2}' where user_name = '{user2}'")

                                else:
                                    raise ValueError ("Account number not matched")
                                
                            except ValueError as e :
                                print("Error :", e)

                    except ValueError as e :
                        print("Invalid Input! ", e)
  ```
### Delete acount:
- Asks Useif He/She wants to delete their account.
- If **'yes'** then removed all of their data from database including their transaction history.
- If **'No'** then continue with the facilities.
  ``` py
  def dlt_acc(self) :
        input_user = input("Do you really want to DELETE your account?\n"
                           "YES OR NO" )
        if input_user == "yes":
            db_query(f"delete from customer where user_name = '{self.__user_name}'")
            db_query(f"drop table {self.__user_name}")
            print("Account deleted !"
  ```



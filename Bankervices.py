from database import *
import datetime
class bank:
    def __init__(self, user_name, acc_number):
        self.__user_name = user_name
        self.__acc_number = acc_number

    def Transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__user_name}_HISTORY "
                 f"( user_name VARCHAR(50),"
                 f"acc_number INTEGER,"
                 f"amount INTEGER,"
                 f"transaction_time DATETIME,"
                 f"remark varchar(20) )")
        
    def checkbalance(self) :
        balance = db_query(f" select Balance from customer where user_name = '{self.__user_name}'")
        print("Your Balance : ", balance [0][0])

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

    def dlt_acc(self) :
        input_user = input("Do you really want to DELETE your account?\n"
                           "YES OR NO" )
        if input_user == "yes":
            db_query(f"delete from customer where user_name = '{self.__user_name}'")
            db_query(f"drop table {self.__user_name}")
            print("Account deleted !")



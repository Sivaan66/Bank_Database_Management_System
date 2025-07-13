from database import *
from customer import *
from Bankervices import *
import random

def signup():
    user_name = input("Enter an username:")
    temp = db_query(f"select user_name from customer where user_name ='{user_name}' ")
    if temp:
        print("Username already exists")
        signup()
    else:
        password = str(input("Enter a password:"))
        name = str(input("Enter a name as registered as your addhar number or during account opening:"))

        while True:
            try :
                phn_number = input("Enter your phone number:")
                if not phn_number.isdigit():
                    raise ValueError("Phone number should only contain digits")
                if len(phn_number) != 10:
                    raise ValueError("Your phone number must be of 10 digits only!")
                break
            except ValueError as e:
                print("Invalid input :", e)

        age = input(str("Enter a age:"))
        city = input(str("Enter your city:"))

        while True:
            acc_number = random.randint(a=10000000,b=99999999)
            temp= db_query(f"select acc_number from customer where acc_number ='{acc_number}'")
            if temp:
                continue
            else:
                print(f"your account number is : {acc_number}")
                break
    cobj= customers(user_name, password, name, phn_number,acc_number, age, city)
    cobj.createuser()
    bankobj = bank(user_name, acc_number)
    bankobj.Transaction_table()
    signin()

def signin():
    user_name = input("Enter your Username :")
    temp = db_query(f"select user_name from customer where user_name ='{user_name}' ")
    if temp :
        while True:
            password = input('Enter your Password :')
            temp = db_query(f"select password from customer where user_name ='{user_name}' ")
            if temp [0][0]== password :
                print("SignIn Successfull.")
                while True:
                       temp1 = db_query(f"select user_name, acc_number from customer where user_name ='{user_name}' ")
                       user = temp1 [0][0]
                       acc_number = temp1[0][1]
                       try :
                            facilities = int(input("1. Check Balance\n"
                                             "2. Deposite\n"
                                             "3. Withdraw\n"
                                             "4. Fund Transfer\n"
                                             "5. Delete Account"))
                            
                            if facilities < int(1) or facilities > int(5) :
                                raise ValueError("Enter a valid number between 1 to 5")
                            
                            if facilities==1:
                                b = bank(user, acc_number)
                                b.checkbalance()
                                break
                            if facilities==2:
                                b = bank(user, acc_number)
                                b.deposite()
                                break
                            if facilities==3:
                                b = bank(user, acc_number)
                                b.withdraw()
                                break
                            if facilities==4:
                                b = bank(user, acc_number)
                                b.fundtransfer()
                                break
                            if facilities==5:
                                delete_acc()
                                break
                       except ValueError as e :
                            print("Invalid Input :", e)
            else :
                print("Password Missmatched")
                continue
    else :
        print("Username doesn't exist. Enter your Username!")

    

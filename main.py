from registration import *
status = False
while True:
    try:
        register = int(input("1. SignUp\n"
                             "2. SignIn"))
        if register == 1 or register == 2:
            if register == 1:
                signup()
            if register == 2:
                signin()
                break
        else:
            print("Please Enter Valid Input From Options")

    except ValueError:
        print("Invalid Input Try Again with Numbers")

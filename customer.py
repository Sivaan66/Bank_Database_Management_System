from database import*
class customers:
    def __init__(self, user_name, password, name, phn_number,acc_number, age, city):
        self.__user_name = user_name
        self.__password = password
        self.__name = name
        self.__phn_number = phn_number
        self.__acc_number = acc_number
        self.__age = age
        self.__city = city

    def  createuser(self):
        db_query(f"insert into customer values ('{self.__user_name}', '{self.__password}', '{self.__name}', '{self.__phn_number}','{self.__acc_number}', '{self.__age}', '{self.__city}',0, 1)")
        mydb.commit()
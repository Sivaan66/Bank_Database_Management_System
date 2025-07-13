import mysql.connector as msq
mydb = msq.connect(
    host = "localhost",
    user = "root",
    passwd = "Sivaan@31320",
    database = "bank_database"
)


cursor = mydb.cursor()

def db_query(query):
    cursor.execute(query)
    if query.strip().lower().startswith("select"):
        return cursor.fetchall()
    else:
        mydb.commit()
        return None


def customertable ():
    cursor.execute(''' create table if not exists customer
                   (user_name varchar(20),
                   password varchar(20),
                   name varchar(20),
                   phn_number VARCHAR(20),
                   acc_number BIGINT(20),
                   age INT(20),
                   city varchar(20),
                   Balance integer(20),
                   status TINYINT(1))''')
    mydb.commit()
if __name__ == "__main__" :
    customertable()

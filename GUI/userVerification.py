import sqlite3
import time
from shutil import copyfile


conn = sqlite3.connect('userDataBase.db')
c = conn.cursor()

def verdict(status):
    if status[0]:
        print("There is such a user")
        if status[1]:
            print("Correct password")
        else:
            print("Wrong password")
    else:
        print("There is NO such a user")


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS userDataBase(unix REAL, username TEXT, password TEXT)")



def createNewUser(user_name, user_password):
    unix = float(time.time())

    c.execute("INSERT INTO userDataBase (unix, username, password) VALUES (?, ?, ?)",
              (unix, user_name, user_password))

    conn.commit()


def read_from_db():
    c.execute('SELECT * FROM userDataBase')
    data = c.fetchall()
    #print(data)
    for row in data:
        print(row)
    print("###")

def checkUser(newUserName, password):
    #check if the user exists
    c.execute("SELECT * FROM userDataBase WHERE username='{}'".format(newUserName))
    data = c.fetchall()
    # for row in data:
    #     print(row)
    if len(data)==1:
        if data[0][2] == password:
            return (True, True)
        else:
            return (True, False)
    return (False, False)



def filling_func():
    for i in range(10):
        createNewUser('u' + str(i*2 * int(time.time()) % 25), 'p' + str(i * int(time.time()) % 15))
        time.sleep(1)

def doBackUp():
    copyfile("userDataBase.db", "userDataBaseCOPY.db")

#create_table()
#filling_func()
#doBackUp()
#read_from_db()
#print(checkUser("u12", "33", c))
#test()

# c.close
# conn.close()







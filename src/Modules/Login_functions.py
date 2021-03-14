from Modules.Login import *

conn = sqlite3.connect("../assets/Database.db")
cursor = conn.cursor()


def add_medications(username, name, quantity, time):
    command = (
        'INSERT INTO {} (NAME,QUANTITY,TIME) VALUES("'.format(username)
        + name
        + '","'
        + quantity
        + '","'
        + time
        + '");'
    )
    conn.execute(command)
    conn.commit()


def check_medications(username, name):
    command = 'SELECT NAME from {} where NAME = "'.format(username) + name + '"'
    cursor.execute(command)
    data = cursor.fetchall()
    if len(data) == 0:
        return False
    else:
        return True


def delete_medications(username, name):
    command = 'DELETE from {} where NAME = "'.format(username) + name + '"'
    conn.execute(command)
    conn.commit()
    green("\n" + name + " details have been deleted from the database successfully.\n")


def display(username):
    command = "SELECT NAME,QUANTITY,TIME from {}".format(username)
    cursor.execute(command)
    data = cursor.fetchall()
    for name, quantity, time in data:
        print("Name : " + name + " | Quantity : " + quantity + " | Time : " + time)

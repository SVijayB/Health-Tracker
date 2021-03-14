from Health_tracker import *
from Modules.Colours import *

conn = sqlite3.connect("../assets/Database.db")
cursor = conn.cursor()


def get_password(username):
    command = 'SELECT PASSWORD from DETAILS WHERE USERNAME = "' + username + '"'
    cursor = conn.execute(command)
    for row in cursor:
        password = row[0]
    return password


def add_account(username, password):
    command = (
        'INSERT INTO DETAILS (USERNAME,PASSWORD) VALUES("'
        + username
        + '","'
        + password
        + '");'
    )
    conn.execute(command)
    conn.commit()


def update_password(username, password):
    command = (
        'UPDATE DETAILS set PASSWORD = "'
        + password
        + '" where USERNAME = "'
        + username
        + '"'
    )
    conn.execute(command)
    conn.commit()
    green("\npassword has been updated successfully.\n")


def delete_account(username):
    command = 'DELETE from DETAILS where USERNAME = "' + username + '"'
    conn.execute(command)
    conn.commit()
    green(
        "\n" + username + " details have been deleted from the database successfully.\n"
    )


def check_details(username):
    cursor.execute("SELECT USERNAME from DETAILS where USERNAME = ?", (username,))
    data = cursor.fetchall()
    if len(data) == 0:
        return False
    else:
        return True

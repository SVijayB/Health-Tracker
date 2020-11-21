import os
import sys
import sqlite3
from getpass import getpass
from Modules.Colours import *
from Modules.Functions import *

if __name__ == "__main__":

    conn = sqlite3.connect('assets/Database.db')
    cursor = conn.cursor()

    try:
        conn.execute('''CREATE TABLE DETAILS 
            (USERNAME TEXT NOT NULL, 
            PASSWORD TEXT NOT NULL)''')
    except:
        pass

    os.system('cls')
    logo = open("assets/logo.txt","r")
    output = "".join(logo.readlines())
    print(output)

    cyan("-" * 15)
    print("""What would you like to do?
    1) Login
    2) Add an account
    3) Update Password
    4) Delete an account
    5) Exit""")
    choice = int(input("> "))
    cyan("-" * 15)

    if(choice==1):
        username = input("Enter your Username \n> ")
        flag = check_details(username)
        if flag:
            password = getpass("Enter password \n> ")
            if(get_password(username)==password):
                green("Logged in successfully")
            else:
                red("Your password does not seem to match...")
        else:
            red("Incorrect username")

    elif(choice==2):
        username = input("Enter your new Username \n> ")
        cursor.execute("SELECT USERNAME from DETAILS where USERNAME = ?", (username,))
        data = cursor.fetchall()
        username = username.capitalize()
        flag = check_details(username)
        if flag:
            red("\nUsername {} already exists.\n".format(username))
        else:
            password = getpass("Enter password \n> ")
            add_account(username, password)
            green("\n" + username + " account has been successfully created\n")
        
    elif (choice == 3):
        username = input("Enter the username for which you want to update the password for \n> ").capitalize()
        flag = check_details(username)
        if flag:
            old_password = getpass("Enter old password :\n> ")
            if(get_password(username)==old_password):
                new_password = getpass("Enter new password :\n> ")
                update_password(username, new_password)
            else:
                red("Your password does not seem to match...")
        else:
            red("\nThere are no details for %s" % username + "\n")

    elif (choice == 4):
        username = input("Enter the username for the account you want to delete \n> ").capitalize()
        flag = check_details(username)
        if flag:
            old_password = getpass("Enter password :\n> ")
            if(get_password(username)==old_password):
                delete_account(username)
            else:
                red("Your password does not seem to match...")
        else:
            red("\nThere are no details for %s" % username + "\n")

    elif(choice == 5):
        green("\n-----x Thanks for using Health tracker x-----")
        grey("Press enter to exit...")
        input()
        conn.close()

    else:
        red("\nERROR : Invalid choice\n")
import os
import sqlite3
from Modules.Colours import *

def login(username):
    os.system('cls')

    logo = open("assets/logo.txt","r")
    output = "".join(logo.readlines())
    print(output)

    conn = sqlite3.connect('assets/Database.db')
    cursor = conn.cursor()

    try:
        command = ('''CREATE TABLE IF NOT EXISTS {} 
        (NAME TEXT NOT NULL, 
        QUANTITY TEXT NOT NULL,
        TIME TEXT NOT NULL)''').format(username)
        conn.execute(command)
    except:
        pass

    cyan("-" * 15)
    print("""What would you like to do?
    1) Add perscriptions
    2) Modify perscriptions
    3) Delete perscriptions
    4) Set reminders for appointments
    5) Exit""")
    choice = int(input("> "))
    cyan("-" * 15)

    if(choice==1):
        medication = input("Enter the name of your medicine \n> ").capitalize()
        quantity = input("How many pills do you take at once? \n> ").capitalize()
        temp = 0
        print("""Time at which you are prescribed to take medications?
        (Type in the numbers and hit enter. Once done, enter 5)
        1) Morning
        2) Afternoon
        3) Night
        4) Exit""")
        time = ""
        while (temp!=4):
            temp = int(input("> "))
            if(temp == 1):
                if("Morning" in time):
                    print("You have already added morning!")
                else:
                    time = time + " Morning "
            elif(temp == 2):
                if("Afternoon" in time):
                    print("You have already added afternoon!")
                else:
                    time = time + " Afternoon "
            elif(temp == 3):
                if("Night" in time):
                    print("You have already added Night!")
                else:
                    time = time + " Night "
            elif(temp == 4):
                print("You will be reminded to take your pills in the" + time)
            else:
                print("Type in numbers from 1 to 4 only")
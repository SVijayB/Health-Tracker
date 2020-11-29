from Modules.Login import *
import schedule
import time
import pygame

conn = sqlite3.connect('assets/Database.db')
cursor = conn.cursor()

def add_medications(username, name, quantity, time):
    command = 'INSERT INTO {} (NAME,QUANTITY,TIME) VALUES("'.format(username)+name+'","'+quantity+'","'+time+'");'
    conn.execute(command)
    conn.commit()

def check_medications(username, name):
    command = ('SELECT NAME from {} where NAME = "'.format(username) + name + '"')
    cursor.execute(command)
    data = cursor.fetchall()
    if len(data) == 0:
        return False
    else:
        return True

def delete_medications(username, name):
    command = ('DELETE from {} where NAME = "'.format(username) + name + '"')
    conn.execute(command)
    conn.commit()
    green("\n" + name + " details have been deleted from the database successfully.\n")

def schedule():
    print("""Select the interval range between each appointments
    1) Days
    2) Weeks""")
    choice = int(input("> "))
    if(choice == 1):
        days = input("What is the interval range in days between each of the appointment?")
        time = input("Enter the time at which you want to be reminded (HH:MM 24 hour clock).")
        schedule.every(days).day.at(time).do(appointment_reminder)
    elif(chouce == 2):
        weeks = input("What is the interval range in weeks between each of the appointment?")
        time = input("Enter the time at which you want to be reminded (HH:MM 24 hour clock).")
        schedule.every(days).day.at(weeks).do(appointment_reminder)

def appointment_reminder():
    print("REMINDER: Doctor's appointment")
    pygame.mixer.init()
    sound = pygame.mixer.Sound('assets/ringtone.mp3')
    sound.play()
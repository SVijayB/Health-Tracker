import time
from pygame import mixer
from Modules.Login import *


def scheduler(username):
    morning = []
    afternoon = []
    night = []
    command = "SELECT NAME,TIME from {}".format(username)
    cursor.execute(command)
    data = cursor.fetchall()
    for name, timevar in data:
        if "Morning" in timevar:
            morning.append(name)
        if "Afternoon" in timevar:
            afternoon.append(name)
        if "Night" in timevar:
            night.append(name)

    print("Program running in the background in order to provide reminders")

    while True:
        t = time.localtime()
        current_time = time.strftime("%H:%M", t)

        if current_time == "08:30":
            print("Time for you to take : ")
            for i in morning:
                print("> " + i)
            reminder()
            time.sleep(60)
        elif current_time == "12:30":
            print("Time for you to take : ")
            for i in afternoon:
                print("> " + i)
            reminder()
            time.sleep(60)
        elif current_time == "20:30":
            print("Time for you to take : ")
            for i in night:
                print("> " + i)
            reminder()
            time.sleep(60)
        time.sleep(1)


def reminder():
    green("Time to take your meds")
    mixer.init()
    mixer.music.load("../assets/ringtone.mp3")
    mixer.music.play()

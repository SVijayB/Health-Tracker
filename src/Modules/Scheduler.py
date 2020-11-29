import schedule
import time
from pygame import mixer
import datetime

def scheduler():
    

def reminder():
    print("REMINDER: Doctor's appointment")
    mixer.init()
    mixer.music.load('assets/ringtone.mp3')
    mixer.music.play()

def loop():
    print("Program running in the background in order to provide reminders")
    while True:
        schedule.run_pending()
        time.sleep(1)
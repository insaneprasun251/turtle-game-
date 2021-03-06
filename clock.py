#*Welcome to DataFlair Alarm Clock*


#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
from pydub import AudioSegment
from pydub.playback import play
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("set date :",date)
        print(now)
        if now == set_alarm_timer:
            print("hey dude! mom gonna come and kick your ass wake up!!")
            song = AudioSegment.from_wav("sound.wav")
            play(song)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("DataFlair Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = " Rise at !",fg="black",relief = "solid",font=("TimesNew Roman",7,"bold")).place(x=0, y=29)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "white",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "white",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "white",width = 15).place(x=200,y=30)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="green",width = 10,command = actual_time).place(x =110,y=70)

clock.mainloop()
#Execution of the window.




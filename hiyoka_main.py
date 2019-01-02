#Main project
#Guining Pertin - Otoshuki

#Import libraries
import os
import nltk
import random
import numpy as np
import time
import datetime
from playsound import playsound as ps
import serial

#Import files
import wake_word
import watson_generator as watgen

#Global variables
sleeping = 0

#Triggers
triggers = ['./triggers/yoka_san_linux.ppn','./triggers/good_night_linux.ppn']

#Phrases
commons = ("good morning", "good night", "who are you", "how are you")
exits = ('exit', 'shut down')

#Replies
greets = {"Good Morning":'./sounds/good_morning',"Good Night":'./sounds/good_night'}
who_are_you = {"I am your friend Hiyoka!":'./sounds/friend_hiyoka',
                "I am your personal assistant, Hiyoka!":'./sounds/assistant_hiyoka'}

#Set up serial port
#arduino = serial.Serial('/dev/ttyACM0', 115200)

#Functions
def exit_hiyoka():
    print("Thank You!")
    ps('./sounds/yes')
    ps('./sounds/shutting_down_systems')

#Sleep Mode for Hiyoka
def sleep_hiyoka():
    global sleeping
    reply = list(greets.keys())[1]
    print(reply)
    ps(greets[reply])
    ps('./sounds/entering_sleep_mode')
    sleeping = 1

#Wake Up Hiyoka
def wake_hiyoka():
    global sleeping
    ps('./sounds/good_morning')
    ps('./sounds/starting_systems')
    sleeping = 0

if __name__ == '__main__':
    while True:
        #If system is sleeping
        if sleeping == 1:
            print("Sleep Mode")
            word = wake_word.trigger_detect(['./triggers/good_morning_linux.ppn'])
            wake_hiyoka()
        #Detect wake wake_word if not sleeping
        elif sleeping == 0:
            print("Main trigger")
            word = wake_word.trigger_detect(triggers)

            #Wake up trigger
            if word == 0:
                print("Next trigger")
                ps('./sounds/yes')

                #Use Google Speech Recognition
                input = watgen.recog()
                print(input)
                #Detect common phrases
                if input.startswith(commons):
                    print("Common Phrases")
                    if input == commons[0]:
                        reply = list(greets.keys())[0]
                        print(reply)
                        ps(greets[reply])
                    if input == commons[1]:
                        sleep_hiyoka()
                    if input == commons[2]:
                        reply = np.random.choice(list(who_are_you.keys()))
                        print(reply)
                        ps(who_are_you[reply])
                    if input == commons[3]:
                        reply = 'I am fine'
                        print(reply)
                        #ps()
                #Exit in command
                elif input.startswith(exits):
                    exit_hiyoka()
                    break
                #Date
                if 'date' in input:
                    now = datetime.datetime.now()
                    date = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
                    print("Date : ",date)
                    ps('./sounds/todays_date_is')
                    ps(watgen.translate(date,True))
                #Control lights
                #Turn Lights1 on and off
                if ('turn' in input) and ('on' in input) and ('lights' in input):
                    #arduino.write('1')
                    print('Lights1 ON')
                if ('turn' in input) and ('off' in input) and ('lights' in input):
                    #arduino.write('5')
                    print('Lights1 OFF')
                
            #Sleep trigger
            elif word == 1:
                sleep_hiyoka()

#Play Music

#Control extension cord

#Say a joke

#Say a story

#Weather

#Scheduling

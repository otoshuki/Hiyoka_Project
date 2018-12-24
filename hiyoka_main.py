#Main project
#Guining Pertin - Otoshuki

#Import libraries
import os
import nltk
import random
import numpy as np
import time
from playsound import playsound as ps

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
# #Good morning trigger
# gm_trigger = './triggers/good_morning_linux.ppn'
# #Good night trigger
# gn_trigger = './triggers/good_night_linux.ppn'

#Functions
def exit_hiyoka():
    print("Thank You!")
    ps('./sounds/yes')
    ps('./sounds/shutting_down_systems')

def sleep_hiyoka():
    global sleeping
    reply = list(greets.keys())[1]
    print(reply)
    ps(greets[reply])
    ps('./sounds/entering_sleep_mode')
    sleeping = 1

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
                #Date and time
            
            #Sleep trigger
            elif word == 1:
                sleep_hiyoka()

#Perform command

#Play Music

#Control lights

#Control extension cord

#Say a joke

#Say a story

#Weather

#Scheduling

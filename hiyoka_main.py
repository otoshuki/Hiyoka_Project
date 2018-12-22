#Main project
#Guining Pertin - Otoshuki

#Import libraries
import os
import wake_word
import watson_generator
import nltk
import random
import numpy as np
import time
from playsound import playsound as ps

#Triggers
#Main wake word
main_trigger = './Triggers/yoka_san_linux.ppn'
#Good morning trigger
gm_trigger = './Triggers/good_morning_linux.ppn'
#Good night trigger
gn_trigger = './Triggers/good_night_linux.ppn'

keywords = [gm_trigger,gn_trigger]
while True:
    #Detect wake wake_word
    print("Main trigger")
    word = wake_word.trigger_detect([main_trigger])
    #Wake up word
    if word:
        print("Next trigger")
        ps('./sounds/yes')
        work = wake_word.trigger_detect(keywords)
        #Detect good morning
        if work == 0:
            print("Good Morning")
            ps('./sounds/good_morning')
        #Detect good night
        elif work == 1:
            print("Good Night")
            ps('./sounds/good_night')

#Wait for command
#Speak

#Perform command

#Play Music

#Control lights

#Control extension cord

#Say a joke

#Say a story

#Weather

#Scheduling

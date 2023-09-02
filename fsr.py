#start by importing all neccessary libraries

import RPi.GPIO as GPIO
import time
from pygame import mixer
mixer.init()
mixer.music.load('elephant.mp3')
mixer.music.set_volume(.7)
#set the GPIO to BCM Mode
GPIO.setmode(GPIO.BCM)

#set Pin4 to be our Sniffer Pin, We want this to be an input so we set it as such
GPIO.setup(4, GPIO.IN)
# This variable will be used to determine if pressure is being applied or not
prev_input =0
# create a loop that will be used to determine if pressure is being applied or not
while True:
    #take a reading
    input = GPIO.input(4)
    print(input)
    #if the last reading was low and this one is high, alert us
    if ((not prev_input) and input):
        print("Pressure Detected")
        mixer.music.play()
    elif((prev_input) and input):
        print("Not under Pressure")
    #update previous input
    prev_input = input
    #slight pause to debounce
    time.sleep(0.10)
#!/usr/bin/python3
import time
import os
from ev3dev2.motor import Motor, OUTPUT_A
from ev3dev2.button import Button

os.system("setfont Lat15-TerminusBold14")

# button handler
btn = Button()

# moteur sur le port A
moteur = Motor(OUTPUT_A)

# time controller
t = 0

while True:
    # handle motor stop
    if t <= 0:
        moteur.on(0)

    if btn.up:
        moteur.on(0)
        t=0
        exit()

    elif btn.left:
        moteur.on(30)
        t = 2

    
    elif btn.right:
        moteur.on(-30)
        t = 2

    t -= .01
    time.sleep(.01)



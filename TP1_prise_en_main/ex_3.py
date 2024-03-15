#!/usr/bin/env python3
from sys import stderr
from time import sleep

from ev3dev2.motor import Motor, OUTPUT_A

moteur = Motor(OUTPUT_A)

def afficher(message):
    print("\r" + message, file=stderr, end="\r")
    print("\r" + message, end="\r")

for i in range(9):
    power = 10 * i 
    moteur.on(power)
    afficher("Puissance : " + str(power))
    sleep(1)
    
moteur.on(0)
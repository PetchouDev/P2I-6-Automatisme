#!/usr/bin/python3
from sys import stderr

from ev3dev2.motor import Motor, OUTPUT_A
from ev3dev2.sensor import INPUT_1, Sensor

moteur = Motor(OUTPUT_A)

capteur = Sensor(INPUT_1)
capteur.mode = 'RGB-RAW'

while True:
    # if black
    if capteur.value(0) < 20 and capteur.value(1) < 20 and capteur.value(2) < 20:
        moteur.on(0)
    else:
        moteur.on(30)
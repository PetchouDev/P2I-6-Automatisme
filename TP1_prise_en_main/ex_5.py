#!/usr/bin/env python3
from sys import stderr

from ev3dev2.motor import Motor, OUTPUT_A
from ev3dev2.sensor import INPUT_1, Sensor

moteur = Motor(OUTPUT_A)

capteur = Sensor(INPUT_1)
capteur.mode = "TOUCH"

while True:
    if capteur.value() == 1:
        i = moteur.position
        while moteur.position - i < 360:
            moteur.on(30)
        moteur.on(0)
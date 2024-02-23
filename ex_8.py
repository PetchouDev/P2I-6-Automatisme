#!/usr/bin/python3
from sys import stderr

from ev3dev2.sensor import Sensor, INPUT_1
from ev3dev2.motor import Motor, OUTPUT_A

moteur=Motor(OUTPUT_A)

sensor=Sensor(INPUT_1)
sensor.mode='ANGLE'
sensor.command='RESET'


print('Ready', file=stderr)

while True :
    v = sensor.value()
    moteur.on(min(100, max(-100, v)))

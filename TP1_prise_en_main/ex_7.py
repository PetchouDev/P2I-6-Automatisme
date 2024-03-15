#!/usr/bin/env python3
from ev3dev2.sensor import Sensor, INPUT_1
from ev3dev2.motor import Motor, OUTPUT_A

moteur=Motor(OUTPUT_A)
sensor=Sensor(INPUT_1)

sensor.mode='US-DIST-CM'

while True :
    v = sensor.value()
    if 200 < v < 400:
        moteur.on(30)
    else:
        moteur.on(0)
        
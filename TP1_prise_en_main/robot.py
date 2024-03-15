#!/usr/bin/python3
from sys import stderr

import time

from ev3dev2.sensor import Sensor, INPUT_2
from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B

left=Motor(OUTPUT_A)
right=Motor(OUTPUT_B)

sensor=Sensor(INPUT_2)
sensor.mode='US-DIST-CM'

while True:
    if sensor.value() > 250:
        left.on(50)
        right.on(50)
    else:
        # stop
        left.on(0)
        right.on(0)

        # tourner à droite
        left.on(50)
        right.on(-50)
        time.sleep(1)
        left.on(0)
        right.on(0)
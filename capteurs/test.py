#!/usr/bin/python3
from time import sleep, time
import datetime
from sys import stderr
from ev3dev2.led import Leds
from ev3dev2.sensor import INPUT_1, INPUT_3, Sensor
import os

leds=Leds()
leds.all_off()

FILE = "results_" + datetime.datetime.now().strftime('%Y_%m_%d_%H:%M:%S') + ".txt"

dist_sensor = Sensor(INPUT_1)
dist_sensor.mode = "US-DIST-CM"

touch_sensor = Sensor(INPUT_3)
touch_sensor.mode = "TOUCH"

print('Let''s blink LEDS')

leds.set_color('LEFT','YELLOW')
leds.set_color('RIGHT','YELLOW')

mesured_distances = []

while (True): 
    if touch_sensor.value(0) == 1: 
        dist = dist_sensor.value(0) / 10
        mesured_distances.append(dist)
        print('Distance: ', dist, ' cm')
        os.system('echo ' + str(dist) + ' >> ' + FILE)
    sleep(0.5)

leds.all_off()


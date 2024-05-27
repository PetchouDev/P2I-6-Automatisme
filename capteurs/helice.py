#!/usr/bin/python3
from time import sleep, time
import datetime
from sys import stderr
from ev3dev2.led import Leds
from ev3dev2.motor import Motor, OUTPUT_A
from ev3dev2.sensor import INPUT_1, INPUT_3, Sensor
import os
import json

leds=Leds()
leds.all_off()

FILE = "results_" + datetime.datetime.now().strftime('%Y_%m_%d_%H:%M:%S') + ".txt"

dist_sensor = Sensor(INPUT_1)
dist_sensor.mode = "US-DIST-CM"

# touch sensor
touch_sensor = Sensor(INPUT_3)
touch_sensor.mode = "TOUCH"

nb_pales = 1

print('Let''s blink LEDS')

leds.set_color('LEFT','YELLOW')
leds.set_color('RIGHT','YELLOW')

mesured_distances = []

# lancer le moteur
m = Motor(OUTPUT_A)

# reset encoder
m.reset()



theta = 0
t0 = time()

# lancer le moteur
m.on(50, 5)

mesures = {
    "temps": [0],
    "angle": [0],
    "motor": [0]
}
found = False
running = True
while (running): 
    if time() - t0 > 10:
        running = False
        
    dist = dist_sensor.value(0) / 10
    if dist < 200 and not found:
        # passager d'une pale de l'hélice
        mesures["temps"].append(time() - t0)
        theta += 360
        mesures["angle"].append(theta)
        mesures["motor"].append(abs(m.position))
        found = True
    else:
        found = False

open("out.json", "w").write(json.dumps(mesures, indent=4))

leds.all_off()


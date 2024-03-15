#!/usr/bin/python3
from time import sleep
from ev3dev2.led import Leds
from ev3dev2.sensor import INPUT_1, Sensor

capteur=Sensor(INPUT_1)
leds=Leds()
leds.all_off()

capteur.mode="TOUCH"

print('Let''s blink LEDS')
while (capteur.value()==0):
    leds.set_color('LEFT','YELLOW')
    leds.set_color('RIGHT','YELLOW')


while (True): 
    if(capteur.value()==1) :
        leds.set_color('LEFT','RED')
        leds.set_color('RIGHT','GREEN')
        sleep(0.2)
        leds.set_color('LEFT','GREEN')
        leds.set_color('RIGHT','RED')
        sleep(0.2)
    leds.all_off()


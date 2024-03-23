#!/usr/bin/python3
from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_D

from ev3dev2.sensor import Sensor, INPUT_1, INPUT_3, INPUT_4

from ev3dev2.led import Leds
from time import sleep

moy=50
consigne=50
# Déclaration des moteurs
moteur_d= Motor(OUTPUT_D)
moteur_g= Motor(OUTPUT_A)   

# Déclaration des capteurs
sensor= Sensor(INPUT_4)
touche_sensor = Sensor(INPUT_3)

# Configuration des capteurs de couleur pour détecter le noir
sensor.mode = 'COL-REFLECT'
while not touche_sensor.value():
    pass

sleep(2)


Kp = 0.4



while not touche_sensor.value():
    erreur= consigne-sensor.value()
    moteur_d.on(moy - Kp * erreur)
    moteur_g.on(moy + Kp * erreur)

moteur_d.off()
moteur_g.off()
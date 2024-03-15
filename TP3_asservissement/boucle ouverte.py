#!/usr/bin/python3
from math import pi

from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import Sensor, INPUT_1

# Déclaration des moteurs
droite = Motor(OUTPUT_A)
gauche = Motor(OUTPUT_B)
droite.reset()

# Déclaration du capteur
capteur = Sensor(INPUT_1)
capteur.mode = 'US-DIST-CM'

dist = 0

# Boucle ouverte
while dist < 80 :
    droite.on(100)
    gauche.on(100)
    dist = droite.position * 2 * pi * 3.25 / 360

droite.off()
gauche.off()


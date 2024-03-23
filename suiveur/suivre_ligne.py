#!/usr/bin/python3
from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_D

from ev3dev2.sensor import Sensor, INPUT_1, INPUT_3, INPUT_4

from ev3dev2.led import Leds

from time import sleep

# Déclaration des moteurs
moteur_gauche = Motor(OUTPUT_A)
moteur_droit = Motor(OUTPUT_D)

# Déclaration des capteurs
capteur_gauche = Sensor(INPUT_1)
capteur_droit = Sensor(INPUT_4)
touch_sensor = Sensor(INPUT_3)

# Configuration des capteurs de couleur pour détecter le noir
capteur_gauche.mode = 'COL-REFLECT'
capteur_droit.mode = 'COL-REFLECT'

# Déclaration des leds
leds = Leds()

# Configuration du capteur de toucher
touch_sensor.mode = 'TOUCH'

# Constantes
SLOW = -20
FAST = 100

# allumage des leds
leds.set_color('LEFT', 'YELLOW')
leds.set_color('RIGHT', 'YELLOW')

# Tant que le capteur de toucher n'est pas activé
while not touch_sensor.value():
    pass

# Allumage des leds en vert
leds.set_color('LEFT', 'GREEN')
leds.set_color('RIGHT', 'GREEN')

# Attente de 2 secondes
sleep(2)

while not touch_sensor.value():

    # Si les deux capteurs détectent du blanc => sortie du circuit => Reculer
    if capteur_gauche.value() > 80 and capteur_droit.value() > 80:
        moteur_gauche.on(SLOW)
        moteur_droit.on(SLOW)

    else:
        # tant que le capteur de gauche ne détecte pas le noir
        if capteur_gauche.value() > 30:
            moteur_gauche.on(FAST)
            moteur_droit.on(SLOW)

        # tant que le capteur de droit ne détecte pas le noir
        if capteur_droit.value() > 30:
            moteur_gauche.on(SLOW)
            moteur_droit.on(FAST)

        # si les deux capteurs détectent le noir
        if capteur_gauche.value() < 30 and capteur_droit.value() < 30:
            moteur_gauche.on(FAST)
            moteur_droit.on(FAST)
    
# Arrêt des leds
leds.all_off()

# Arrêt des moteurs
moteur_gauche.off()
moteur_droit.off()
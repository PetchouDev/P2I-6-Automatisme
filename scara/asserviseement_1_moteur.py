#!/usr/bin/python3
from time import time
import json 

from ev3dev2.motor import Motor, OUTPUT_D #OUTPUT_B
from ev3dev2.led import Leds

# Moteurs
moteur_d = Motor(OUTPUT_D)
# moteur_g = Motor(OUTPUT_B)




# leds
leds = Leds()


# Variables
Kp=.7
#Ki=0
#Kd=0.05


# initialisation de la consigne 
consigne = 30
moteur_d.position=0

print('Ready')
# allumer les leds en vert
leds.set_color("LEFT", "GREEN")
leds.set_color("RIGHT", "GREEN")



while True :

    # lire l'erreur
    erreur = consigne-moteur_d.position

    # calculer la puissance
    power =  min(100, max(-100, Kp*erreur ))
    
    # appliquer la puissance
    moteur_d.on(power)
    #moteur_g.on(power)


# Fin du programme => eteindre les moteurs
moteur_d.off()
#moteur_g.off()




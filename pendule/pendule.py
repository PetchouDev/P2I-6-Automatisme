#!/usr/bin/python3
from time import time
import json 

from ev3dev2.motor import Motor, OUTPUT_D, OUTPUT_B

from ev3dev2.sensor import Sensor, INPUT_4, INPUT_1

from ev3dev2.led import Leds

# Moteurs
moteur_d = Motor(OUTPUT_D)
moteur_g = Motor(OUTPUT_B)



# Capteur d'angle
capteur= Sensor(INPUT_4)
capteur.mode = 'ANGLE-ACC'
capteur.command = 'RESET'

# leds
leds = Leds()

touch = Sensor(INPUT_1)
touch.mode = 'TOUCH'

# Variables
Kp=.7
Ki=0
Kd=0.05

erreurs=[capteur.value()]
integral=0
times = []
positions = [capteur.value()]
CONSIGNE=0

print('Ready')

# allumer toutes les leds en jaune
leds.set_color("LEFT", "YELLOW")
leds.set_color("RIGHT", "YELLOW")

# attendre qu'on appuie sur le bouton pour lancer la boucle
while not touch.value():
    pass

# allumer les leds en vert
leds.set_color("LEFT", "GREEN")
leds.set_color("RIGHT", "GREEN")

# initialiser le temps
t0 = time()
times.append(0)

while not touch.value() or time()-t0<2:
    # acquerir le temps
    dt = time()-t0

    # lire l'erreur
    erreur = CONSIGNE-capteur.value()

    # calcul de l'integrale et de la derivee
    integral += erreur*dt
    derivee = (erreur-erreurs[-1])/(dt - times[-1])

    # calculer la puissance
    power = - min(100, max(-100, Kp*erreur + Ki*integral + Kd*derivee))
    
    # appliquer la puissance
    moteur_d.on(power)
    moteur_g.on(power)

    # stocker les erreurs et les temps

    erreurs.append(erreur)
    times.append(dt)
    positions.append(capteur.value())

# Fin du programme => eteindre les moteurs
moteur_d.off()
moteur_g.off()

# eteindre les leds
leds.all_off()

# sauvegarder les données
with open("data.json", "w") as f:
    json.dump({"erreurs": erreurs, "times": times, "positions": positions}, f, indent=4)

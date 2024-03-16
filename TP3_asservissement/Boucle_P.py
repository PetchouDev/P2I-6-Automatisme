#!/usr/bin/python3
from math import pi
from time import time
import json

from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import Sensor, INPUT_1

# Déclaration des moteurs
droite = Motor(OUTPUT_A)
gauche = Motor(OUTPUT_B)
droite.reset()

# Déclaration du capteur
capteur = Sensor(INPUT_1)
capteur.mode = 'US-DIST-CM'

# Coef 
ERROR = 3
KP_avant = 0.5
KP_arriere = 2

dist = capteur.value()

# erreur 
consigne=[                      ]
erreur = lambda d: (d - 20) * 100 / 20

data = {
    "position": [],
    "erreur": [],
    "puissance": [],
    "temps": []
}
t0 = time()
tf = t0 + 10

# Boucle ouverte
while time() < tf:
    dist = capteur.value() / 10
    err = erreur(dist)

    dt = time() - t0
    data["position"].append(dist)
    data["erreur"].append(err)
    data["temps"].append(dt)

    
    if  0 < err :
        power = max(-100, min(100, KP_avant * err))
        data["puissance"].append(power)
        droite.on(power)
        gauche.on(power)

    elif err < 0:
        power = max(-100, min(100, KP_arriere * err))
        data["puissance"].append(power)
        droite.on(power)
        gauche.on(power)


droite.off()
gauche.off()

with open("data.json", "w") as f:
    json.dump(data, f)


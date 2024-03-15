#!/usr/bin/python3
from math import pi
import json
from time import time
from sys import stderr

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
KP_avant = 1
KP_arriere = 2

KI_avant = 0.001
KI_arriere = 0.002

dist = capteur.value()

# erreur 
erreur = lambda d: (d - 20) * 100 / 20

integral = 0
t0 = time()
t_precedent = t0

tf = t0 + 10

data = {
    "position": [],
    "erreur": [],
    "puissance": [],
    "integral": [],
    "temps": []
}

# Boucle ouverte
while time() < tf:
    dist = capteur.value() / 10
    err = erreur(dist)

    dt = time() - t_precedent
    integral += err * dt
    t0 = time()

    data["position"].append(dist)
    data["erreur"].append(err)
    data["integral"].append(integral)
    data["temps"].append(t0)

    print("Erreur: ", err, file=stderr)
    print("Integral: ", integral, file=stderr)
    print("#################", file=stderr)

    
    if  err > 2:
        power = max(-100, min(100, KP_avant * err + KI_avant * integral))
        data["puissance"].append(power)
        droite.on(power)
        gauche.on(power)

    elif err < 2:
        power = max(-100, min(100, KP_arriere * err + KI_arriere * integral))
        data["puissance"].append(power)
        droite.on(power)
        gauche.on(power)
    

droite.off()
gauche.off()

with open("data_PI.json", "w") as f:
    json.dump(data, f)
        



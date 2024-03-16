#!/usr/bin/python3
from math import pi
import json
from time import time
from sys import stderr

from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import Sensor, INPUT_1
from ev3dev2.button import Button


# Déclaration des moteurs
droite = Motor(OUTPUT_A)
gauche = Motor(OUTPUT_B)
droite.reset()

# Déclaration du capteur
capteur = Sensor(INPUT_1)
capteur.mode = 'US-DIST-CM'

# declare button
btn = Button()


# Coef 
KP_avant = .6
KP_arriere = 1

KD_avant = KP_avant / 30
KD_arriere = KP_arriere / 30

KI_avant = KP_avant / 2000
KI_arriere = KP_arriere / 2000



dist = capteur.value()

# erreur 
erreur = lambda d: (d - 20) * 100 / 20

integral = 0
t0 = time()
t_precedent = t0

tf = t0 + 10

e_prev = erreur(capteur.value() / 10)  # erreur precedente

data = {
    "position": [],
    "erreur": [],
    "puissance": [],
    "integral": [],
    "temps": []
}
run = True
# Boucle ouverte
while run:
    dist = capteur.value() / 10
    err = erreur(dist)

    dt = time() - t_precedent
    integral += err * dt
    t0 = time()

    data["position"].append(dist)
    data["erreur"].append(err)
    data["integral"].append(integral)
    data["temps"].append(t0)

    de = (err - e_prev) / dt
    e_prev = err

    print("Erreur: ", err, file=stderr)
    print("Integral: ", integral, file=stderr)
    print("#################", file=stderr)

    
    if  err > 2:
        power = max(-100, min(100, KP_avant * err + KI_avant))
        data["puissance"].append(power)
        droite.on(power)
        gauche.on(power)

    elif err < 2:
        power = max(-100, min(100, KP_arriere * err + KI_arriere * integral))
        data["puissance"].append(power)
        droite.on(power)
        gauche.on(power)

    # si appui sur 1 bouton, on arrete la boucle
    if btn.any():
        run = False
    

droite.off()
gauche.off()

with open("data_PI.json", "w") as f:
    json.dump(data, f)
        



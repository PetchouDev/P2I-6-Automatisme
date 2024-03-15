#!/usr/bin/python3
from time import time
import json

from ev3dev2.motor import OUTPUT_A, Motor

# QUESTIONS 1 à 3
motor = Motor(OUTPUT_A)
motor.reset()

t0 = time()
temps = 0

donnees = {
    "temps": [],
    "position": []
}

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

while time() - t0 < 5:
    # calcul du temps écoulé
    temps = time() - t0
    motor.on(30)

    # Enregistrement des données
    donnees["position"].append(motor.position)
    donnees["temps"].append(temps)


# Arret du moteur
motor.off()

# Sauvegarde des données dans un fichier
save_data(donnees, "data.txt")
#!/usr/bin/env python3
import json
from time import sleep, time
from threading import Thread

from ev3dev2.motor import Motor, OUTPUT_A
from ev3dev2.sensor import INPUT_1, Sensor

motor = Motor(OUTPUT_A)
motor.reset()
motor.position = 0

sensor = Sensor()
sensor.mode = 'TOUCH'

class timer(Thread):
    def __init__(self, moteur):
        Thread.__init__(self)
        self.moteur = moteur
        self.running = True

    def run(self):
        i = 0
        while self.running and i < 4:
            self.moteur.on(20 * (i + 1))
            sleep(2)
            i += 1
        self.moteur.on(0)
        self.running = False

    def stop(self):
        self.running = False
        self.moteur.on(0)
        self.join()
        exit()


# Création d'une instance de la classe timer
task = timer(motor)
t0 = time()

# Stocker les mesures
donnees = {
    "temps": [],
    "position": []
}

# Lancement de la tâche
task.start()

while task.running:
    if sensor.value() == 1:
        task.stop()
        
    dt = time() - t0
    donnees["temps"].append(dt)
    donnees["position"].append(motor.position)
    sleep(0.05)

# Sauvegarde des mesures
with open("mesures.json", "w") as f:
    json.dump(donnees, f)



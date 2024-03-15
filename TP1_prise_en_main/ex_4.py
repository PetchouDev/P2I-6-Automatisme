#!/usr/bin/env python3
from sys import stderr

from ev3dev2.motor import Motor, OUTPUT_A

moteur = Motor(OUTPUT_A)
moteur.position = 0

moteur.on_for_rotations(30, 3)

print("Position: ", moteur.position, file=stderr)
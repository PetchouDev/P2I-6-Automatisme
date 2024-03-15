import os
import json

from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__)) 

# Lecture des mesures
with open("mesures.json", "r") as f:
    donnees = json.load(f)

positions = donnees["position"]
temps = donnees["temps"]

# calcul de la vitesse de rotation
vitesse = [0]
for i in range(1, len(positions)):
    vitesse.append((positions[i] - positions[i - 1]) / (temps[i] - temps[i - 1]))

# Vitesse théorique (en °/s)
vitesse_theorique = [0.20 * 1050 if t < 2 else 0.40 * 1050 if t < 4 else 0.60 * 1050 if t < 6 else 0.80 * 1050 for t in temps]

# affichage des dt
dt = [temps[i] - temps[i - 1] for i in range(1, len(temps))]
print("dt min = ", min(dt))
print("dt max = ", max(dt))
print("dt moyen = ", sum(dt) / len(dt))

# Affichage de la vitesse
plt.plot(temps, vitesse)
plt.plot(temps, vitesse_theorique)
plt.xlabel("temps (s)")
plt.ylabel("vitesse (°/s)")
plt.legend(["vitesse mesurée", "vitesse théorique"])
plt.show()



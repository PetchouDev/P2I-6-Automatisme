import os
import json

from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))

# Récupération des données
with open("data.txt", "r") as file:
    donnees = json.load(file)

with open("data.txt", "w") as file:
    json.dump(donnees, file, indent=4)

# vitesse moyenne
vitesse_moyenne = (donnees["position"][-1] - donnees["position"][0]) / (donnees["temps"][-1] - donnees["temps"][0])
print("Vitesse moyenne:", vitesse_moyenne)

equart_relatif = abs(vitesse_moyenne - .3*1050) / (.3*1050)
print("Ecart relatif:", equart_relatif)
if equart_relatif < 0.1:
    print("La vitesse mesurée est cohérente avec la vitesse attendue")

dt = [donnees["temps"][i+1] - donnees["temps"][i] for i in range(len(donnees["temps"])-1)]
print("dt moyen:", sum(dt)/len(dt))
print("dt max:", max(dt))
print("dt min:", min(dt))

# Affichage des données
plt.plot(donnees["temps"], donnees["position"])
plt.xlabel("Temps (s)")
plt.ylabel("Position (degrés)")
plt.title("Position du moteur en fonction du temps")
plt.show()
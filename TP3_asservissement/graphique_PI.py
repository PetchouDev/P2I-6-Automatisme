import json

from matplotlib import pyplot as plt

with open("data_PI.json", "r") as f:
    data = json.load(f)

plt.plot(data["temps"], data["position"], label="Position")
plt.plot(data["temps"], data["erreur"], label="Erreur")
#plt.plot(data["temps"], data["integral"], label="Integral")
plt.plot(data["temps"], data["puissance"], label="Puissance")
plt.legend()
plt.show()
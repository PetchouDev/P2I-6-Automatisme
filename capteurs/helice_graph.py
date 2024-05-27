from matplotlib import pyplot as plt

import json

data = json.load(open("out.json"))

plt.plot(data["temps"], data["angle"], 'ro', label='Angle mesuré', markersize=1)
plt.plot(data["temps"], data["motor"], 'g-', linewidth=1, label='Angle moteur')
plt.ylabel('Angle (°)')
plt.xlabel('Temps (s)')
plt.legend()
plt.show()

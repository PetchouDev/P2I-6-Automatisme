from matplotlib import pyplot as plt
 
import json


with open('data.json') as f:
    data = json.load(f)

plt.plot(data['times'], data['erreurs'])
plt.plot(data['times'], data['positions'])
plt.xlabel('temps (s)')
plt.ylabel('erreur')

plt.show()

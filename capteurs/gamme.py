from matplotlib import pyplot as plt

def read_file() :
    with open("gamme.txt", "r") as f:
        data = f.readlines()
    return [float(x.strip()) for x in data]


data = read_file()

points = list(range(2, 21)) + list(range(25, 55, 5)) + list(range(225, 311, 5))

ecart = [abs(data[i] - points[i])*100/points[i] for i in range(len(points))]

plt.plot(points, data, 'ro', label='Distance mesurée', markersize=1)
plt.plot(points, points, 'g-', linewidth=1, label='Distance réelle')
plt.ylabel('Distance mesurée (cm)')
plt.xlabel('Distance réelle (cm)')
plt.legend()

# ecarts relatifs sur un diagramme batons
plt.figure()
plt.bar(points, ecart)
plt.ylabel('Ecart relatif (%)')
plt.xlabel('Distance réelle (cm)')
plt.title('Ecart relatif entre la distance réelle et la distance mesurée')


plt.show()
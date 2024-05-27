from math import pi

# Variables
L1 = 6.5
L2 = 5.5

Kp=.7

# découpagez de la trajectoire en x points
def traj(depart, arrivee, nb_points="auto"):
    points = []
    x1, y1 = depart
    x2, y2 = arrivee

    if nb_points == "auto":
        nb_points = int(((x2 - x1)**2 + (y2 - y1)**2) ** .5)

    # vecteur directeur
    vect = ((x2 - x1), (y2 - y1))

    for i in range(nb_points):
        points.append((x1 + i * vect[0] / nb_points, y1 + i * vect[1] / nb_points))

    points.append(arrivee)

    print(points)
    return points

def deg(x):
    return x * 180 / pi

def rad(x):
    return x * pi / 180
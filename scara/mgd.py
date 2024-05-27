from math import pi, cos, sin

from data import L1, L2

def mgd(phi1, phi2):
    x = cos(phi1) * (L1 + L2 * cos(phi2)) - sin(phi1) * L2 * sin(phi2)
    y = cos(phi1) * L2 * sin(phi2) + sin(phi1) * (L1 + L2 * cos(phi2))

    return x, y

if __name__ == "__main__":
    phi1 = pi/2
    phi2 = 0
    result = mgd(phi1, phi2)
    print(result)
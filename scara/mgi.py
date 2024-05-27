from math import cos, sin, atan2

from data import L1, L2, deg

def mgi(x, y, position_actuelle):
    # determiner phi2
    cos_2 = (x**2 + y**2 - L1**2 - L2**2) / (2*L1*L2)
    sin_2 = (1 - cos_2**2) ** .5

    phi2_pos = atan2(sin_2, cos_2)
    phi2_neg = atan2(-sin_2, cos_2)

    if abs(position_actuelle - phi2_pos) > abs(position_actuelle - phi2_neg):
        phi_2 = phi2_neg
    else:
        phi_2 = phi2_pos

    # determiner phi1
    cos_1 = ((L1 + L2*cos(phi_2))*x + L2 * sin(phi_2) * y) / (x**2 + y**2)
    sin_1 = (-L2*sin(phi_2)*x + (L1 + L2*cos(phi_2))*y) / (x**2 + y**2)

    phi_1 = atan2(sin_1, cos_1)
    phi_2 = phi_2

    return deg(phi_1), deg(phi_2)

if __name__ == "__main__":
    x = 6
    y = 5
    result = mgi(x, y)
    print(result)


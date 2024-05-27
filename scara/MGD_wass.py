#!/usr/bin/python3
from ev3dev2.motor import Motor , OUTPUT_A, OUTPUT_B
from threading import Timer 
import math 

from data import L1 as l1, L2 as l2

class MonTimer() :
    def __init__(self,delai,fonction):
        self.delai=delai
        self.fonction=fonction
        self.timer = Timer(delai,self.run)
    def start(self):
        self.timer.start()
    def run(self):
        self.timer = Timer(self.delai,self.run)
        self.timer.start()
        self.fonction()
    def cancel(self):
        self.timer.cancel()


i=0
j=0

def changer():
    if i<len(x) :
        global i 
        i+=1
def changer2():
    if j<len(y):
        global j 
        j+=1

kp=.7


moteur_1 = Motor(OUTPUT_A)
moteur_2 = Motor(OUTPUT_B)

consigne = []
x_cons=24
y_cons=12

x = []
y = []
for k in range(x_cons) :
    x.append(k)
for b in range(y_cons):
    y.append(b)

def f_phi2(i,x,y,j):
    cos_phi2= (x[i]**2+y[j]**2-l1**2-l2**2)/(2*l1*l2)
    sin_phi2= math.sqrt(1-cos_phi2**2)
    phi2=math.atan2(sin_phi2/cos_phi2)
    return phi2,cos_phi2,sin_phi2

def f_phi1(i,x,y,j,cos_phi,sin_phi):
    cos_phi1 = ((l1+l2*cos_phi2)x[i]+l2*sin_phi*y[j])/(x[i]**2+y[j]**2)
    sin_phi1 = ((l1+l2*cos_phi2)y[j]-l2*sin_phi*x[i])/(x[i]**2+y[j]**2)
    phi= math.atan2(sin_phi1/cos_phi1)
    return phi1,cos_phi1,sin_phi1





delta_t = [0.1]
tache_1=MonTimer(delta_t[j],changer)
tache_2=MonTimer(delta_t[j],changer2)

tache_1.start()
tache_2.start()


while True :
    phi2,cos_phi2,sin_phi2 = f_phi2(i,x,y,j)
    phi1,cos_phi1,sin_phi1 = f_phi1(i,x,y,j,cos_phi2,sin_phi2)

    erreur1=phi1-moteur_1.position
    erreur2=phi2-moteur_2.position

    moteur_1.on(max(-100,min(100,kp*erreur1)))
    moteur_2.on(max(-100,min(100,kp*erreur2)))


moteur_1.on(0)
moteur_2.on(0)
tache_1.cancel()
tache_2.cancel()










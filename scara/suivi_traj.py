#!/usr/bin/python3
from ev3dev2.motor import Motor , OUTPUT_A, OUTPUT_B
from threading import Timer 
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
    global i
    i+=1
def changer2():
    global j
    j+=1

kp=.7



moteur_1 = Motor(OUTPUT_A)
moteur_2 = Motor(OUTPUT_B)
consigne = []
for k in range(45) :
    consigne.append(k*2)
for b in range(1,10):
    consigne.append(90-b*5)

delta_t = [0.1,0.5]
tache_1=MonTimer(delta_t[j],changer)
tache_2=MonTimer(4.5,changer2)

tache_1.start()
tache_2.start()
while i<len(consigne)-1 :
    erreur=consigne[i]-moteur_1.position
    moteur_1.on(kp*erreur)


moteur_1.on(0)
tache_1.cancel()
tache_2.cancel()










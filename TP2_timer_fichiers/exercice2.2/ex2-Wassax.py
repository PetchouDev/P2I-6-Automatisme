#!/usr/bin/env python3
# question 1
import csv 
from time import time 
from ev3dev2.sensor import Sensor, INPUT_1
from ev3dev2.motor import Motor, OUTPUT_A
from threading import Timer
from time import sleep

moteur=Motor(OUTPUT_A)
t0= time()
temps = 0
donnee0=[]
donnee=[]   
moteur.position=0

# Définition de la classe MonTimer
class MonTimer:
    # Le cosntructeur avec comme arguments délai (la période de répétition) et fonction (la méthode à répéter)
    def __init__(self,delai, fonction):
        self.delai=delai
        self.fonction = fonction
        self.timer = Timer(delai,self.run) # Création du timer

    # La méthode au démarage qui lance le Timer
    def start(self):
        self.timer.start()

    # Lors de son exécution, un nouveau Timer est créé pour de nouveau lancer la méthode à répéter
    def run(self):
        self.timer =Timer(self.delai, self.run)
        self.timer.start()
        self.fonction()

    # Lors de l'arrêt de cette tâche, le Timer s'arrête et s'annule
    def cancel(self):
        self.timer.cancel()

    

def tourner(i):
        moteur.on(20*(i+1))

def recup():
    donnee0.append((moteur.position,time()-t0))


i=0
while i<4 :

    MonTimer(2,tourner(i)).start()
    MonTimer(0.05,recup).start()
    i+=1






moteur.on(0)



# Enrgistrement des données dans un fichier csv
with open('data.csv','w',encoding='utf-8') as fichier :
    writer = csv.writer(fichier, delimiter=';')
    writer.writerows(donnee)


"""# Création des listes initiales
data_x=[] # Pour stocker les données X
data_y=[] # Pour stocker les données Y
data_z=[] # Pour stocker les données Z
# Remplissage des listes à partir du fichier texte
with open('data.csv','r' ,encoding='utf-8' ) as fichier :
    reader = csv.reader(fichier,delimiter=';')
    for row in reader:
        data_x.append(float(row[0]))
        data_y.append(float(row[1]))


# Figure y = f(x) et z=f(x)
plt.figure()
plt.plot(data_x,data_y,"r--")
plt.title("y=f(x)")
plt.xlabel("x [unit]")
plt.ylabel("y [unit]")
plt.legend(['y=f(x)'])
plt.show()"""
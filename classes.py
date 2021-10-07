"""
entrainement sur les classes
"""
from random import *

choix = int(input("Nombre de dés à lancer : "))


def lancer():
    liste = []
    compteur = 0
    while compteur != choix:
        resultat = randint(0, 6)
        #print(resultat)
        compteur += 1
        liste.append(resultat) 
    piupiu = liste.count(1)   
    print("Nombre de 1 : ",piupiu)
    piupiu2 = liste.count(2)   
    print("Nombre de 2 : ",piupiu2)
    piupiu3 = liste.count(3)   
    print("Nombre de 3 : ",piupiu3)
    piupiu4 = liste.count(4)   
    print("Nombre de 4 : ",piupiu4)
    piupiu5 = liste.count(5)   
    print("Nombre de 5 : ",piupiu5)
    piupiu6 = liste.count(6)   
    print("Nombre de 6 : ",piupiu6)
    print("")
    print("Nombre de 4+ : ", piupiu4+piupiu5+piupiu6)
    

lancer()
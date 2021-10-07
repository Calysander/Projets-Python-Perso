"""
Cedi est un programme de simulation de jets de dés
"""
from random import *

ss = True



def lance(): 
    selec = int(input("choisissez le nombre de dés a lancer : "))  
    nombre = 0
    while nombre != selec:
        de = randint(1, 6)
        nombre += 1
        print(de)

while ss:
    lance()
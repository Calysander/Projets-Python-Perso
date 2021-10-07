#coding:utf-8

choix = input ("choisissez une opération a effectuer \n\t1 -  Addition\n\t2 - Soustraction\n\t3 - Multiplication\n\t4 - Division\n >>> ")
choix = int (choix)
if choix == 1:
    chiffreAdd1 = input("entrez le premier chiffre : ")
    chiffreAdd1 = int(chiffreAdd1)
    chiffreAdd2 = input ("entrez le deuxieme chiffre : ")
    chiffreAdd2 = int(chiffreAdd2)
    resultatAddition = chiffreAdd1 + chiffreAdd2
    print("resultat = ",resultatAddition)
elif choix == 2:
    chiffreSous1 = input ("entrez le premier chiffre : ")
    chiffreSous1 = int(chiffreSous1)
    chiffreSous2 = input ("entrez le deuxieme chiffre : ")
    chiffreSous2 = int(chiffreSous2)
    resultatSous = chiffreSous1 - chiffreSous2
    print("resultat de la soustraction", chiffreSous1, " - ", chiffreSous2, " = ", resultatSous)
elif choix == 3:
    #faire une multiplication
    pass
elif choix == 4:
    #faire une division
    pass
else:
    print("Nous n'avons pas compris votre choix")
    choix = input ("choisissez une opération a effectuer \n\t1 -  Addition\n\t2 - Soustraction\n\t3 - Multiplication\n\t4 - Division\n >>> ")
    choix = int (choix)




"""continuer = input("voulez vous continuer les multiplications, Y / N ?")
if continuer == "y" or continuer == "Y" :
    choix = True
elif continuer == "n" or continuer == "N":
        choix = False
else:
    choix = False
    print ("nous n'avons pas compris votre réponse")

while choix == True:
    choix_table = input("choisissez une table de multiplication : ")
    choix_table = int(choix_table)
    compteur = 1
    while compteur <=10 :
        print (compteur, "multiplié par :", choix_table, "=", compteur * choix_table)
        compteur +=1

print("merci!!")"""

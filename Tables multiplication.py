#coding:utf-8


continuer = input("voulez vous continuer les multiplications, Y / N ?")
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

print("merci!!")


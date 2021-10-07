#coding:utf-8



def multiplication(multiple):	
	compteur = 1
	while compteur <= 10:
		print (multiple, " x ", compteur, " = ", multiple * compteur)
		compteur += 1

def addition(nmbre1, nmbre2):
	print (nmbre1, " + ", nmbre2, " = ", nmbre1 + nmbre2)


programme = True
while programme == True:
	choix = input("Entrez le chiffre a multiplier : ")
	choix = int(choix)
	if 1<=choix<=99  :		
		multiplication(choix)
	else:
		programme == False
		print("Au revoir et merci !")
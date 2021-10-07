# -*- coding: utf8 -*-
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')

user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')


def get_random_quote(bleu):
    if user_answer == "b":
        pass
    elif user_answer == "c":
        print('petite merde ingrate')
    else:
        pass
    bleu[0]
    print(bleu)

print (get_random_quote(quotes))
   

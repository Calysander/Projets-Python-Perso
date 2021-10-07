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

def get_random_item_in(my_list):
    # TODO: get a random item
    blabla = my_list[0]
    return blabla

user_answer = input("tappe toi les couilles")

while user_answer != "b":
    print(get_random_item_in(quotes))
    user_answer = "b"
    
print(get_random_item_in(quotes))

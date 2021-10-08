"""
Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7, en
signalant au passage (à l’aide d’une astérisque) ceux qui sont des multiples de 3.
Exemple : 7 14 21 * 28 35 42 * 49 ...
"""

multi = 1
while multi <= 20 :
    result = multi * 7
    if result%3 == 0 :
        print(result, "*")
    else :
        print(result)
    multi += 1
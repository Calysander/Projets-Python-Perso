"""
Écrivez un programme qui calcule les 50 premiers termes de la table de multiplication par 13,
mais n’affiche que ceux qui sont des multiples de 7.
"""

multi = 1
while multi <= 50 :
    result = multi * 13
    if result%7 == 0 :
        print(result)
    else :
        pass
    multi += 1
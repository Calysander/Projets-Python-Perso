"""
Écrivez un programme qui affiche une table de conversion de sommes d’argent exprimées en
euros, en dollars canadiens. La progression des sommes de la table sera « géométrique »,
comme dans l’exemple ci-dessous :
1 euro(s) = 1.65 dollar(s)
2 euro(s) = 3.30 dollar(s)
4 euro(s) = 6.60 dollar(s)
8 euro(s) = 13.20 dollar(s)
etc. (S’arrêter à 16384 euros.)
"""


euro = 1
dollar = 1.65
while euro < 16384 :
    print(euro, "euro(s) = ", dollar*euro, "dollars(s)")
    euro *= 2
    

"""
entrainement sur les classes
"""

class Personne :
    def __init__(self, c_nom, c_prenom):
        self.nom = c_nom
        self.prenom = c_prenom
        print(c_nom, c_prenom)

h1 = Personne("dupond", "robert")
h2 = Personne("françois","claude")
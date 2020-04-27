class Point(object):
    _nom = "Dupont"
    _solde = 1000
    def __init__(self, nom, solde):
        self._nom = nom
        self._solde = solde

    def depot(self, nb):
        self._solde += nb

    def retrait(self, nb):
        self._solde -= nb
    
    def affichage(self):
        print("le solde du compte de " + self._nom + " est de ")
        print(self._solde)

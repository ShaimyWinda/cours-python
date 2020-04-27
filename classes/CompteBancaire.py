class CompteBancaire(object):
    def __init__(self, nom = "Dupont", solde = 1000):
        self._nom = nom
        self._solde = solde

    def depot(self, nb):
        self._solde += nb

    def retrait(self, nb):
        self._solde -= nb
    
    def affichage(self):
        print("le solde du compte de " + self._nom + " est de ")
        print(self._solde)

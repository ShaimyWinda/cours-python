from Personne import Personne

class Employe(Personne):
    def __init__(self, nom, prenom, dateNaissance, salaire):
        Personne.__init__(self, nom, prenom, dateNaissance)
        self._salaire = salaire

    def afficher(self):
        print("Nom : " + self._nom)
        print("Prenom : " + self._prenom)
        print("Date de naissance : " + self._dateNaissance)
        print("Salaire : " + str(self._salaire))

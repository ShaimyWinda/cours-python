class Personne():
    def __init__(self, nom, prenom, dateNaissance):
        self._nom = nom
        self._prenom = prenom
        self._dateNaissance = dateNaissance

    def afficher(self):
        print("Nom : " + self._nom)
        print("Prenom : " + self._prenom)
        print("Date de naissance : " + self._dateNaissance)

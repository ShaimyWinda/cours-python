from DateDeNaissance import DateDeNaissance

class Personne(DateDeNaissance):
    def __init__(self, nom, prenom, DateDeNaissance):
        self._nom = nom
        self._prenom = prenom

    def afficher(self):
        dateNaissance = DateDeNaissance.toString()
        print("Nom : " + nom)
        print("Prenom : " + prenom)
        print("Date de naissance : " + dateNaissance)

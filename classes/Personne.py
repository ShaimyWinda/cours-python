from DateDeNaissance import DateDeNaissance

class Personne(DateDeNaissance):
    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom
        DateDeNaissance.__init__(self, jour, mois, annee)

    def afficher(self):
        dateNaissance = DateDeNaissance.toString()
        print("Nom : " + nom)
        print("Prenom : " + prenom)
        print("Date de naissance : " + dateNaissance)

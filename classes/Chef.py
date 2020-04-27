from Employe import Employe

class Chef(Employe):
    def __init__(self, nom, prenom, dateNaissance, salaire, service):
        Employe.__init__(self, nom, prenom, dateNaissance, salaire)
        self._service = service

    def afficher(self):
        print("Nom : " + self._nom)
        print("Prenom : " + self._prenom)
        print("Date de naissance : " + self._dateNaissance)
        print("Salaire : " + str(self._salaire))
        print("Service : " + self._service)

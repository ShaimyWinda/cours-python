class DateDeNaissance(object):
    def __init__(self, jour, mois, annee):
        self._jour = jour
        self._mois = mois
        self._annee = annee

    def toString(self):
        jour = str(self._jour)
        mois = str(self._mois)
        annee = str(self._annee)
        return jour + " / " + mois + " / " + annee
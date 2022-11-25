class Personne:
    AGE_MAJORITE = 18

    def __init__(self, naissance, nom):
        self.naissance = naissance
        self.nom = nom

    def est_majeur(self):
        return (2022 - self.naissance) > self.AGE_MAJORITE

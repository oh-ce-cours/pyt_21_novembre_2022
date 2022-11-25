class Personne:
    def __init__(self, naissance, nom):
        self.naissance = naissance
        self.nom = nom
        self.AGE_MAJORITE = 10

    def est_majeur(self):
        return (2022 - self.naissance) > self.AGE_MAJORITE


p1 = Personne(1990, "Matthieu")
p2 = Personne(1991, "Matthieu")
p3 = Personne(1993, "Matthieu")

print(id(p1.AGE_MAJORITE), id(p2.AGE_MAJORITE), id(p3.AGE_MAJORITE))
Personne.AGE_MAJORITE = 10
print(id(p1.AGE_MAJORITE), id(p2.AGE_MAJORITE), id(p3.AGE_MAJORITE))

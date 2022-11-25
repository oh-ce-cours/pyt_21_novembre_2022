class France:
    def __init__(self):
        self.age_majorite = 18


class Personne:
    def __init__(self, naissance, nom):
        self.naissance = naissance
        self.nom = nom

    def est_majeur(self):
        return (2022 - self.naissance) > Personne.AGE_MAJORITE


p1 = Personne(1990, "Matthieu")
p2 = Personne(1991, "Matthieu")
p3 = Personne(1993, "Matthieu")

print(id(p1.AGE_MAJORITE), id(p2.AGE_MAJORITE), id(p3.AGE_MAJORITE))
Personne.AGE_MAJORITE = 10
p2.AGE_MAJORITE = 343
print(dir(p1))
print(id(p1.AGE_MAJORITE), id(p2.AGE_MAJORITE), id(p3.AGE_MAJORITE))

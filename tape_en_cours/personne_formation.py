class Pays:
    pass


class France(Pays):
    def __init__(self):
        self.age_majorite = 18


class USA(Pays):
    def __init__(self):
        self.age_majorite = 21


pays = {"USA": 21, "France": 18}


class Personne(Pays):
    def __init__(self, naissance, nom, nationalite):
        self.naissance = naissance
        self.nom = nom
        self.nationalite = nationalite

    def est_majeur(self):
        return (2022 - self.naissance) > pays[self.nationalite]


# france = France()
# usa = USA()
p1 = Personne(1990, "Matthieu", nationalite="France")
p2 = Personne(1991, "Matthieu")
p3 = Personne(1993, "Matthieu")

print(id(p1.AGE_MAJORITE), id(p2.AGE_MAJORITE), id(p3.AGE_MAJORITE))
Personne.AGE_MAJORITE = 10
p2.AGE_MAJORITE = 343
print(dir(p1))
print(id(p1.AGE_MAJORITE), id(p2.AGE_MAJORITE), id(p3.AGE_MAJORITE))

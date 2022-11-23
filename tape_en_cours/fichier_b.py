from fichier_a import f

print("f original", id(f))


def f():
    pass


print("f copie", id(f))
from fichier_a import f

print("f unknown", id(f))

# print("dans fichier b", f"{__name__=}")
# fichier_a.f()

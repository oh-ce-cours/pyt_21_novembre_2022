from fichier_a import f
print("f original", id(f))

def f():
    pass



print("dans fichier b", f"{__name__=}")
fichier_a.f()

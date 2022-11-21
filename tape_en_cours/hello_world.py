"""
La doc du module
"""
a = "salut les gens"
2 + "2"
print(a, a, sep="\\")

mon_message = "yo"


def factorielle(n):
    """Factorielle recursive"""
    if n < 2:
        return 1
    return n * factorielle(n - 1)


factorielle("toto")

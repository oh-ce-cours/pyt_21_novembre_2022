"""
La doc du module
"""
a = "salut les gens"
print(a, a, sep="\\")


mon_message = "yo"


def factorielle(n: int) -> int:
    """Factorielle recursive"""
    if n < 2:
        return 1
    return n * factorielle(n - 1)


factorielle("toto")
factorielle(3)
factorielle(3.4)


def f(a: int) -> str:
    return a * "-"


f("a")

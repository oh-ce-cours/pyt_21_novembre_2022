"""
La doc du module
"""
a = "salut les gens"
2 + "2"
print(a, a, sep="\\")

mon_message = "yo"


def factorielle(n):
    if n < 2:
        return 1
    else:
        return n * factorielle(n - 1)

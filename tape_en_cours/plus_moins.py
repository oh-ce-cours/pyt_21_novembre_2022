"""
Un jeu super !
"""
import random
from typing import Optional

NOMBRE_A_TROUVER = random.randint(0, 100)


def mon_input() -> int:
    while True:
        try:
            return int(input("Entrez un nombre : "))
        except ValueError:
            print("On a dit un nombre, svp")
            continue


while True:
    mon_entree = mon_input()
    if NOMBRE_A_TROUVER > mon_entree:
        print("c'est plus")
    elif NOMBRE_A_TROUVER < mon_entree:
        print("c'est moins")
    else:
        print("c'est ça")
        break


print("Gagné")

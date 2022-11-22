"""
Un jeu super !
"""
NOMBRE_A_TROUVER = 10
mon_entree = int(input("Entrez un nombre : "))

while True:
    if NOMBRE_A_TROUVER > mon_entree:
        print("c'est plus")
    elif NOMBRE_A_TROUVER < mon_entree:
        print("c'est moins")
    elif NOMBRE_A_TROUVER < mon_entree:
        print("c'est ça")
        break
    else:
    mon_entree = int(input("Entrez un nombre : "))
print("Gagné")

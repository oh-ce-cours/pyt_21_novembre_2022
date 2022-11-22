"""
Un jeu super !
"""
NOMBRE_A_TROUVER = 10
mon_entree = int(input("Entrez un nombre : "))

while NOMBRE_A_TROUVER != mon_entree:
    if NOMBRE_A_TROUVER > mon_entree:
        print("c'est moins")
    elif NOMBRE_A_TROUVER < mon_entree:
        print("c'est plus")
    else:
        print("c'est ça")
    mon_entree = int(input("Entrez un nombre : "))

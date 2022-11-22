"""
Un jeu super !
"""
NOMBRE_A_TROUVER = 10

while mon_entree := int(input("Entrez un nombre : ")):

    if NOMBRE_A_TROUVER > mon_entree:
        print("c'est plus")
    elif NOMBRE_A_TROUVER < mon_entree:
        print("c'est moins")
    else:
        print("c'est ça")
        break
print("Gagné")

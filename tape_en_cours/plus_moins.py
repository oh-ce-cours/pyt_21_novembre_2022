"""
Un jeu super !
"""
nombre_a_trouver = 10
mon_entree = input("Entrez un nombre : ")

while nombre_a_trouver != mon_entree:
    if nombre_a_trouver > mon_entree:
        print("c'est moins")
    elif nombre_a_trouver < mon_entree:
        print("c'est plus")
    else:
        print("c'est ça")
    mon_entree = input("Entrez un nombre : ")

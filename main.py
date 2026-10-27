# Programme principal

# Fonctions du programme

def display_menu() -> None:
    """Affiche le menu permettant de choisir une opération à effectuer sur une chaîne de caractères."""

    for i in range(1, 7):
        if i == 1:
            print(f"{i} - Afficher le texte normalisé")

        elif i == 2:
            print(f"{i} - Afficher les statistiques générales")

        elif i == 3:
            print(f"{i} - Compter une lettre")

        elif i == 4:
            print(f"{i} - Compter les voyelles")
        
        elif i == 5:
            print(f"{i} - Inverser le texte")

        elif i == 6:
            print(f"{i} - Tester si le mot est un palyndrome")

    print("0 - Quitter")



# Demander une chaîne de caractères initiale à l'utilisateur
chaine = input("Saisissez un texte : ")

display_menu()

option = int(input("Choisissez l'une des options ci-dessus en saisissant son numéro : "))

while option not in range(1, 7) and option != 0:
    print("Option invalide")
    option = int(input("Choisissez l'une des options ci-dessus en saisissant son numéro : "))
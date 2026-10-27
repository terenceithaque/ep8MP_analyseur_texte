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



def normalize_text(text:str) -> str:
    """Normalise le texte passé en paramètre et renvoie la chaîne de caractères correspondante.
    - Supprime les espaces au début et à la fin du texte
    - Convertit le texte en minuscule
    - Remplace les doubles espaces par des espaces simples"""

    texte_final = text.strip().lower() # Supprimer les espaces au début et à la fin du texte et convertir le texte en minuscules

    # Remplacer les espaces doubles par des espaces simples
    texte_final = texte_final.replace("  ", " ")

    return texte_final


def count_letter(text:str, letter:str) -> int:
    """Compte le nombre d'occurences de la lettre letter dans la chaîne de caractères text."""

    nb_occ = 0

    for i in range(len(text)):
        if text[i] == letter:
            nb_occ += 1

    return nb_occ


def count_vowels(text:str) -> int:
    """Renvoie le nombre de voyelles trouvées dans le texte passé en paramètre."""

    nb_vow = 0

    for lettre in text:
        if lettre in "aàâäeéèêëiîïoôöuùûüy":
            nb_vow += 1

    return nb_vow


def count_words(text:str) -> int:
    """Renvoie le nombre de mots trouvés dans le texte passé en paramètre."""

    normalized_text = normalize_text(text) # Normaliser le texte

    if len(normalized_text) == 0:
        return 0

    else:
        # Le nombre de mots correspond au nombre d'espaces trouvés auquel on ajoute 1
        return count_letter(text, " ") + 1


def reverse_text(text:str) -> str:
    """Renvoie le texte avec les lettres inversées par rapport à celui donné en paramètre."""

    texte_inverse = ""

    for i in range(len(text) -1, -1, -1):
        texte_inverse += text[i]

    return texte_inverse


def is_palindrome(text:str) -> bool:
    """Renvoie True si le texte donné en paramètre est un palindrome (se lit de la même manière dans les deux sens de lecture), False sinon."""

    # Normaliser le texte
    normalized_text = normalize_text(text)
    reversed_text = reverse_text(normalized_text)

    return normalized_text == reversed_text


def display_statistics(text:str) -> None:
    """Affiche les statistiques générales du texte passé en paramètre.
    - Nombre total de caractères
    - Nombre total de caractères sans compter les espaces
    - Nombre de mots
    - Nombre de voyelles
    - Nombre d'occurences de la lettre 'a'"""

    nb_cars = len(text)
    print(f"Nombre de caractères : {nb_cars}")

    # Compter le nombre de caractères en excluant les espaces
    nb_cars_sans_espaces = 0

    for car in text:
        if car != " ":
            nb_cars_sans_espaces += 1

    print(f"Nombre de caractères (espaces exclus) : {nb_cars_sans_espaces}")

    # Compter le nombre de mots
    nb_mots = count_words(text)
    print(f"Nombre de mots dans le texte : {nb_mots}")

    # Compter le nombre d'occurrences de la lettre 'a'
    nb_occurences_a = count_letter(text, "a")
    print(f"Nombre d'occurrences de la lettre a : {nb_occurences_a}")


# Demander une chaîne de caractères initiale à l'utilisateur
chaine = input("Saisissez un texte : ")

display_menu()

option = int(input("Choisissez l'une des options ci-dessus en saisissant son numéro : "))

while option not in range(1, 7) and option != 0:
    print("Option invalide")
    option = int(input("Choisissez l'une des options ci-dessus en saisissant son numéro : "))


# Effectuer l'opération choisie par l'utilisateur

if option == 1:
    resultat = normalize_text(chaine)
    print(resultat)

elif option == 2:
    display_statistics(chaine)

elif option == 3:
    lettre = input("Saisissez la lettre à compter dans le texte : ")
    resultat = count_letter(chaine, lettre)
    print(f"La lettre {lettre} a été trouvée {resultat} fois.")

elif option == 4:
    resultat = count_vowels(chaine)
    print(f"Il y a {resultat} voyelles dans {chaine}.")

elif option == 5:
    resultat = reverse_text(chaine)
    print(resultat)

elif option == 6:
    resultat = is_palindrome(chaine)

    if resultat:
        print(f"Le mot {chaine} est un palyndrome.")

    else:
        print(f"Le mot {chaine} n'est pas un palyndrome.")
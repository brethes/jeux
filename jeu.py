import random

# Générer un nombre secret entre 1 et 100
nombre_secret = random.randint(1, 100)

print("Trouvez un nombre entre 1 et 100")

# Initialisation du compteur d'essais
essais = 0
limite_essais = 10  # Nombre maximum d'essais

while essais < limite_essais:
    try:
        proposition = int(input(f"Essai {essais + 1}/{limite_essais} - Entre ta proposition : "))
        essais += 1

        if proposition < nombre_secret:
            print("C'est plus grand !")
        elif proposition > nombre_secret:
            print("C'est plus petit !")
        else:
            print(f"Bravo, tu as trouvé en {essais} essais !")
            break  # Sortir de la boucle une fois trouvé

    except ValueError:
        print("Veuillez entrer un nombre valide.")

if essais == limite_essais and proposition != nombre_secret:
    print(f"Dommage ! Le nombre secret était {nombre_secret}. Réessaie une prochaine fois !")


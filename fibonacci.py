def fibonacci_sequence(n):
    """
    Génère la suite de Fibonacci jusqu'à 'n' termes.
    :param n: Nombre total de termes de la suite.
    :return: Liste contenant la suite de Fibonacci.
    """
    # Étape 1 : Vérifier si 'n' est valide (au moins 1 terme)
    if n <= 0:
        print("Le nombre de termes doit être supérieur à 0.")
        return []
    
    # Étape 2 : Initialiser la liste de Fibonacci avec les deux premiers termes
    fibonacci = [0, 1]  # Les deux premiers termes standards
    
    # Étape 3 : Générer les termes suivants
    for i in range(2, n):  # Boucle de la 3ème position jusqu'à 'n'
        # Le terme suivant est la somme des deux précédents
        next_term = fibonacci[-1] + fibonacci[-2]
        # Ajouter le terme suivant à la liste
        fibonacci.append(next_term)
    
    # Étape 4 : Retourner la suite (tronquée si 'n' <= 2)
    return fibonacci[:n]

# Étape 5 : Demander à l'utilisateur le nombre de termes
try:
    n_terms = int(input("Combien de termes souhaitez-vous dans la suite de Fibonacci ? "))
    # Étape 6 : Appeler la fonction et afficher le résultat
    result = fibonacci_sequence(n_terms)
    if result:  # Si la suite est générée
        print(f"Suite de Fibonacci ({n_terms} termes) : {result}")
except ValueError:
    print("Veuillez entrer un nombre entier valide.")
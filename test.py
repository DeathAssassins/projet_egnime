from constraint import Problem, AllDifferentConstraint

# Créer un problème
problem = Problem()

# Les maisons sont numérotées de 1 à 5
houses = [1, 2, 3, 4, 5]

# Attributs de chaque maison
nationalities = ["Britannique", "Suédois", "Danois", "Norvégien", "Allemand"]
colors = ["Rouge", "Verte", "Blanche", "Jaune", "Bleue"]
drinks = ["Thé", "Café", "Lait", "Bière", "Eau"]
cigarettes = ["Pall Mall", "Dunhill", "Blend", "Bluemaster", "Prince"]
pets = ["Chiens", "Oiseaux", "Chats", "Cheval", "Poisson"]

# Ajouter les variables et leur domaine
problem.addVariables(nationalities, houses)
problem.addVariables(colors, houses)
problem.addVariables(drinks, houses)
problem.addVariables(cigarettes, houses)
problem.addVariables(pets, houses)

# Contraintes d'unicité
problem.addConstraint(AllDifferentConstraint(), nationalities)
problem.addConstraint(AllDifferentConstraint(), colors)
problem.addConstraint(AllDifferentConstraint(), drinks)
problem.addConstraint(AllDifferentConstraint(), cigarettes)
problem.addConstraint(AllDifferentConstraint(), pets)

# Contraintes du problème
problem.addConstraint(lambda brit, red: brit == red, ["Britannique", "Rouge"])
problem.addConstraint(lambda swed, dogs: swed == dogs, ["Suédois", "Chiens"])
problem.addConstraint(lambda dan, tea: dan == tea, ["Danois", "Thé"])
problem.addConstraint(lambda green, white: green == white - 1, ["Verte", "Blanche"])
problem.addConstraint(lambda green, coffee: green == coffee, ["Verte", "Café"])
problem.addConstraint(lambda pallmall, birds: pallmall == birds, ["Pall Mall", "Oiseaux"])
problem.addConstraint(lambda yellow, dunhill: yellow == dunhill, ["Jaune", "Dunhill"])
problem.addConstraint(lambda milk: milk == 3, ["Lait"])  # Maison centrale
problem.addConstraint(lambda nor: nor == 1, ["Norvégien"])  # Première maison
problem.addConstraint(lambda blend, cats: abs(blend - cats) == 1, ["Blend", "Chats"])
problem.addConstraint(lambda horse, dunhill: abs(horse - dunhill) == 1, ["Cheval", "Dunhill"])
problem.addConstraint(lambda bluemaster, beer: bluemaster == beer, ["Bluemaster", "Bière"])
problem.addConstraint(lambda german, prince: german == prince, ["Allemand", "Prince"])
problem.addConstraint(lambda nor, blue: abs(nor - blue) == 1, ["Norvégien", "Bleue"])
problem.addConstraint(lambda blend, water: abs(blend - water) == 1, ["Blend", "Eau"])

# Résoudre le problème
solution = problem.getSolution()

# Afficher la solution sous forme de tableau
if solution:
    table = [["Maison", "Nationalité", "Couleur", "Boisson", "Cigarettes", "Animal"]]
    for house in houses:
        table.append([
            house,
            next(key for key, value in solution.items() if value == house and key in nationalities),
            next(key for key, value in solution.items() if value == house and key in colors),
            next(key for key, value in solution.items() if value == house and key in drinks),
            next(key for key, value in solution.items() if value == house and key in cigarettes),
            next(key for key, value in solution.items() if value == house and key in pets)
        ])
    
    # Afficher le tableau
    for row in table:
        print("{:<10} {:<15} {:<10} {:<10} {:<15} {:<10}".format(*row))
else:
    print("Aucune solution trouvée.")
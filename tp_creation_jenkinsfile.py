import pandas as pd
import numpy as np

# Exemple de données d'employés
data = {
    'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Âge actuel': [45, 58, 52, 60, 47],
    'Année d\'embauche': [2000, 1985, 1990, 1980, 2005]
}

# Créer un DataFrame avec les données
df = pd.DataFrame(data)

# Paramètres
age_de_depart = 62  # L'âge de départ à la retraite

# Ajouter une colonne "Année de départ à la retraite" (l'année d'embauche + l'âge de départ)
df['Année de départ à la retraite'] = df['Âge actuel'].apply(
    lambda x: pd.to_datetime('today').year + (age_de_depart - x)
)

# Ajouter une colonne pour le nombre d'années restantes avant la retraite
df['Années restantes'] = df['Année de départ à la retraite'] - pd.to_datetime('today').year

# Afficher le résultat
print("\nModélisation des départs à la retraite :")
print(df)

# Sauvegarder le résultat dans un fichier CSV
df.to_csv('retirement_predictions.csv', index=False)

# Retourner un message pour Jenkins (le message indiquera si tout va bien ou non)
if df['Années restantes'].min() > 0:
    print("\nModélisation réussie ! Les départs à la retraite ont été calculés.")
else:
    print("\nErreur dans le calcul des départs à la retraite.")
    exit(1)

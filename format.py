import pandas as pd

# Charger le fichier CSV
df = pd.read_csv('fichier.csv')

# Modifier le type des colonnes
df['colonne1'] = df['colonne1'].astype(nouveau_type1)
df['colonne2'] = df['colonne2'].astype(nouveau_type2)
# Ajouter d'autres colonnes et types à modifier selon vos besoins

# Enregistrer le nouveau jeu de données avec les types modifiés
df.to_csv('fichier_modifie.csv', index=False)

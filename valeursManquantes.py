import pandas as pd
import numpy as np

# Charger le fichier CSV existant
df = pd.read_csv('Capital_Bikeshare_dataD.csv')

# Créer des valeurs manquantes
num_missing_values = 100  # Nombre de valeurs manquantes à créer
rows = df.shape[0]
cols = df.shape[1]
missingIndices = np.random.choice(rows * cols, size=num_missing_values, replace=False)
missing_rows = missingIndices // cols
missing_cols = missingIndices % cols
df.iloc[missing_rows, missing_cols] = np.nan

# Enregistrer le nouveau jeu de données avec les valeurs manquantes
df.to_csv('Capital_Bikeshare_dataDD.csv', index=False)


import pandas as pd

# Charger le fichier CSV
df = pd.read_csv('fichier.csv')

# Modifier le type des colonnes
df['colonne1'] = df['colonne1'].astype(nouveau_type1)
df['colonne2'] = df['colonne2'].astype(nouveau_type2)
# Ajouter d'autres colonnes et types à modifier selon vos besoins

# Enregistrer le nouveau jeu de données avec les types modifiés
df.to_csv('fichier_modifie.csv', index=False)

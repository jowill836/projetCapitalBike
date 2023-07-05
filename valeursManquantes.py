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

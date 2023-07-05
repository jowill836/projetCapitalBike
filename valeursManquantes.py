import pandas as pd
import numpy as np

# Charger le fichier CSV existant
df = pd.read_csv('Capital_Bikeshare_dataD.csv')

# Créer des valeurs manquantes
num_missing_values = 100  # Nombre de valeurs manquantes à créer
missing_indices = np.random.choice(df.index, size=num_missing_values, replace=False)  # Sélectionner des indices aléatoires

df.loc[missing_indices, 'temp'] = np.nan  # Remplacer les valeurs aux indices sélectionnés par NaN

# Enregistrer le nouveau jeu de données avec les valeurs manquantes
df.to_csv('Capital_Bikeshare_dataDVV.csv', index=False)
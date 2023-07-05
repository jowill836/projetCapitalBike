import pandas as pd

# Charger le fichier CSV existant
df = pd.read_csv('Capital_Bikeshare_data.csv')

# Ajouter des doublons
df_duplicates = df.sample(frac=0.1, replace=True)  # 10% des données

# Concaténer les données existantes avec les doublons
df_with_duplicates = pd.concat([df, df_duplicates], ignore_index=True)

# Enregistrer le nouveau jeu de données avec les doublons
df_with_duplicates.to_csv('Capital_Bikeshare_dataD.csv', index=False)

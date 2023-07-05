import random
import pandas as pd
import numpy as np
# Charger le fichier CSV existant
data = pd.read_csv('Capital_Bikeshare_dataD.csv', sep=";")
colonne = "temp"
pourcentage_suppression = 2

nb_enregistrements = len(data)
nb_suppressions = int(nb_enregistrements * pourcentage_suppression / 100)

indices_suppressions = np.random.choice(
    data.index, size=nb_suppressions, replace=False)
data.loc[indices_suppressions, colonne] = np.nan

colonne = "windspeed"
pourcentage_suppression = 1

nb_suppressions = int(nb_enregistrements * pourcentage_suppression / 100)

indices_suppressions = np.random.choice(
    data.index, size=nb_suppressions, replace=False)
data.loc[indices_suppressions, colonne] = np.nan

colonne = "hum"
pourcentage_suppression = 0.3

nb_suppressions = int(nb_enregistrements * pourcentage_suppression / 100)

indices_suppressions = np.random.choice(
    data.index, size=nb_suppressions, replace=False)
data.loc[indices_suppressions, colonne] = np.nan

data.to_csv('Capital_Bikeshare_dataDV.csv', index=False, sep=";")

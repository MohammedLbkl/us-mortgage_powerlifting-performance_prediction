import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer

# Nettoie les données, traite les valeurs manquantes, supprime les doublons si nécessaire et prépare les colonnes.

def preprocessing_base(df):

    df_process = df[["Age","BodyweightKg","Sex","TotalKg"]]

    return df_process




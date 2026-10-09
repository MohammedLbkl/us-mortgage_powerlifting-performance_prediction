import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer

# Sépare les variables explicatives X et la cible y, 
# puis crée les ensembles d'entraînement et de test avec train_test_split().


def split_base(df) :

    X = df.drop(columns=["TotalKg"])
    Y = df["TotalKg"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

    return X_train, X_test, Y_train, Y_test
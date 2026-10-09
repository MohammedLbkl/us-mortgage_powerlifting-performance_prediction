import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer

# Nettoie les données, traite les valeurs manquantes, supprime les doublons si nécessaire et prépare les colonnes.

def preprocessing_baseline(df):

    X = df.drop(columns=["accepted", "id"])
    X = X.dropna(axis=1)
    Y = df["accepted"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

    num_cols = X_train.select_dtypes(include=["number"]).columns
    cat_cols = X_train.select_dtypes(include=["object", "category"]).columns

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_cols),
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore", sparse_output=False),
                cat_cols,
            ),
        ]
    )


    X_train_normed = preprocessor.fit_transform(X_train)
    X_test_normed = preprocessor.transform(X_test)

    return X_train_normed, X_test_normed, Y_train, Y_test
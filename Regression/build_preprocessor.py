import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer

# Crée un pipeline Scikit-learn pour imputer les valeurs manquantes, 
# encoder les variables catégorielles et standardiser les variables numériques si nécessaire.


def build_base(X_train, X_test) :

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

    return X_train_normed, X_test_normed
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer

# Évalue les performances avec des métriques adaptées à la régression : MAE, RMSE et R^2
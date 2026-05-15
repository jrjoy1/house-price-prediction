from src.model import get_model
from sklearn.model_selection import train_test_split
import numpy as np

def train_model(train_df, features):

    X = train_df[features]
    y = np.log1p(train_df["SalePrice"])

    X_train, X_val, y_train, y_val = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    model = get_model()
    model.fit(X_train, y_train)

    return model, X_train, X_val, y_train, y_val
import pandas as pd
import numpy as np
import joblib

from src.preprocessing import preprocess
from src.features import create_features
from src.train import train_model
from src.evaluate import evaluate

# Load data
train_df = pd.read_csv("dataset/train.csv")
test_df = pd.read_csv("dataset/test.csv")

# Preprocess
train_df, test_df = preprocess(train_df, test_df)

# Feature engineering
train_df, test_df = create_features(train_df, test_df)

# Features list
features = [
    'OverallQual',
    'GrLivArea',
    'GarageCars',
    'TotalBsmtSF',
    'FullBath',
    'YearBuilt',
    'TotalArea',
    'HouseAge',
    'BathPerRoom',
    'HasGarage'
]

# Train model
model, X_train, X_val, y_train, y_val = train_model(train_df, features)

# Evaluate
evaluate(model, X_train, y_train, X_val, y_val)

# Train full model (final)
X = train_df[features]
y = np.log1p(train_df["SalePrice"])

model.fit(X, y)

# Predict test
X_test = test_df[features]
preds = model.predict(X_test)
preds = np.expm1(preds)

# Save output
output = pd.DataFrame({
    "Id": test_df["Id"],
    "SalePrice": preds
})

output.to_csv("outputs/submission.csv", index=False)

# Save model
joblib.dump(model, "models/xgb_model.pkl")

print("Project completed!")
import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("models/xgb_model.pkl")

st.title("House Price Prediction")

OverallQual = st.slider("Overall Quality", 1, 10, 5)
GrLivArea = st.number_input("Living Area (sq ft)", 500, 10000, 1500)
GarageCars = st.slider("Garage Capacity", 0, 5, 2)
TotalBsmtSF = st.number_input("Basement Area", 0, 5000, 800)
FullBath = st.slider("Full Bathrooms", 0, 5, 2)
YearBuilt = st.number_input("Year Built", 1900, 2025, 2000)

# Engineered features
TotalArea = GrLivArea + TotalBsmtSF
HouseAge = 2026 - YearBuilt
BathPerRoom = FullBath / max(1, OverallQual)
HasGarage = 1 if GarageCars > 0 else 0

features = np.array([[
    OverallQual,
    GrLivArea,
    GarageCars,
    TotalBsmtSF,
    FullBath,
    YearBuilt,
    TotalArea,
    HouseAge,
    BathPerRoom,
    HasGarage
]])

if st.button("Predict Price"):
    prediction = model.predict(features)
    prediction = np.expm1(prediction)

    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")
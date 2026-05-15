🏠 House Price Prediction using Machine Learning
📌 Project Overview

This project predicts house prices using machine learning techniques based on various housing features such as area, quality, number of rooms, and more. The final model is built using XGBoost Regressor with feature engineering and proper validation.

🚀 Workflow

Data Loading & Exploration
Data Cleaning & Missing Value Handling
Feature Engineering
Feature Selection
Model Training (Linear Regression → Random Forest → XGBoost)
Model Evaluation using R² Score
Final Prediction for Submission

⚙️ Technologies Used

Python 🐍
Pandas
NumPy
Scikit-learn
XGBoost
Matplotlib
Seaborn


📊 Model Performance

Train R² Score: ~0.94
Validation R² Score: ~0.95


🔧 Feature Engineering

Created new features:

TotalArea = GrLivArea + TotalBsmtSF
HouseAge = Current Year - YearBuilt
BathPerRoom
HasGarage


📈 Results

The XGBoost model showed strong performance and generalization ability, making it suitable for real-world housing price prediction.

📦 How to Run Project
# Clone repo
git clone https://github.com/your-username/house-price-prediction.git

# Install dependencies
pip install -r requirements.txt

# Run training
python src/train.py

# Make predictions
python src/predict.py


📦 requirements.txt
numpy
pandas
matplotlib
seaborn
scikit-learn
xgboost

🚫 .gitignore
__pycache__/
*.pyc
.ipynb_checkpoints/
model.pkl
.env


👨‍💻 Author

Md. Jillur Rahman Joy
Aspiring Machine Learning Engineer
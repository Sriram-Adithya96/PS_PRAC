import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

df = pd.read_csv("data/Housing.csv")
# print(df.head())
# print("\nShape:", df.shape)
# print("\nColumns:")
# print(df.columns)
# print("\nInfo:")
# print(df.info())
X = df.drop("price", axis=1)
y = df["price"]
# print("\nX:")
# print(X.head())
# print("\ny:")
# print(y.head())
# print("\nCategorical values:")

# for column in X.select_dtypes(include="object").columns:
#     print(f"\n{column}:")
#     print(X[column].unique())
categorical_columns = X.select_dtypes(include="object").columns
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_columns)
    ],
    remainder="passthrough"
)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

print("\ntraining samples:", len(X_train))
print("testing samples:", len(X_test))
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression())
    ]
)
model.fit(X_train, y_train)
import joblib

joblib.dump(model, "model/house_price_model.pkl")

print("\nModel saved successfully!")
y_pred = model.predict(X_test)
print("\nActual vs Predicted:")

# for actual, predicted in zip(y_test[:10], y_pred[:10]):
#     print(f"Actual: {actual:,.0f} | Predicted: {predicted:,.0f}")

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print("\nModel Evaluation")

print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)
print("R²  :", r2)
# Get the trained Linear Regression model
regressor = model.named_steps["regressor"]

# Get the preprocessor
preprocessor_fitted = model.named_steps["preprocessor"]

# Get feature names after one-hot encoding
feature_names = preprocessor_fitted.get_feature_names_out()

# Get coefficients
coefficients = regressor.coef_

# Create a DataFrame
coef_df = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": coefficients
})

# print("\nCoefficients:")
# print(coef_df)
# print("\nIntercept:", regressor.intercept_)

import matplotlib.pyplot as plt

# plt.figure(figsize=(8, 6))

# plt.scatter(y_test, y_pred)

# plt.xlabel("Actual Price")
# plt.ylabel("Predicted Price")
# plt.title("Actual vs Predicted House Prices")
# plt.plot(
#     [y_test.min(), y_test.max()],
#     [y_test.min(), y_test.max()],
#     linestyle="--"
# )
# plt.show()
# residuals = y_test - y_pred

# print("\nFirst 10 residuals:")
# print(residuals.head(10))
# plt.figure(figsize=(8, 6))

# plt.scatter(y_pred, residuals)

# plt.axhline(y=0, linestyle="--")

# plt.xlabel("Predicted Price")
# plt.ylabel("Residual")
# plt.title("Residual Plot")

# plt.show()
from sklearn.metrics import r2_score

# Training predictions
y_train_pred = model.predict(X_train)

# Test predictions
y_test_pred = model.predict(X_test)

# R² scores
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print("\nR² Comparison")
print("Training R²:", train_r2)
print("Testing R² :", test_r2)
from sklearn.model_selection import KFold, cross_val_score

kfold = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

cv_scores = cross_val_score(
    model,
    X,
    y,
    cv=kfold,
    scoring="r2"
)

print("\nCross-validation R² scores:")
print(cv_scores)

print("Mean CV R²:", cv_scores.mean())
print("Std CV R² :", cv_scores.std())
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linestyle="--"
)
plt.show()

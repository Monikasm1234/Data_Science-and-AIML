# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score


# 1️⃣ Create Sample Non-Linear Data
# y = x² + noise (curved relationship)

np.random.seed(42)

X = np.arange(1, 20).reshape(-1, 1)
y = X**2 + np.random.randn(19, 1) * 10

# Convert to dataframe (optional)
df = pd.DataFrame({"Feature": X.flatten(),
                   "Target": y.flatten()})

print("Sample Data:")
print(df.head())

# 2️⃣ Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3️⃣ Linear Regression (Original Feature)

model_linear = LinearRegression()
model_linear.fit(X_train, y_train)

y_pred_linear = model_linear.predict(X_test)

r2_linear = r2_score(y_test, y_pred_linear)

# ------------------------------------------
# 4️⃣ Polynomial Features (degree = 2)
# ------------------------------------------
poly = PolynomialFeatures(degree=2)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Train linear model on polynomial features
model_poly = LinearRegression()
model_poly.fit(X_train_poly, y_train)

y_pred_poly = model_poly.predict(X_test_poly)

r2_poly = r2_score(y_test, y_pred_poly)

# ------------------------------------------
# 5️⃣ Results
# ------------------------------------------
print("\nR² Score (Original Features):", r2_linear)
print("R² Score (Polynomial Features):", r2_poly)

if r2_poly > r2_linear:
    print("\nPolynomial (curved) features improved the model!")
else:
    print("\nolynomial features did not help.")

# ------------------------------------------
# 6️⃣ Visualization
# ------------------------------------------
plt.scatter(X, y, color="blue", label="Data")

# Linear prediction line
plt.plot(X, model_linear.predict(X), label="Linear Model")

# Polynomial curve
X_poly_full = poly.transform(X)
plt.plot(X, model_poly.predict(X_poly_full),
         label="Polynomial Model")

plt.legend()
plt.title("Linear vs Polynomial Regression")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.show()

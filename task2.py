import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

#  Create Sample Numeric Dataset
df = pd.DataFrame({
    "Age": [22, 25, 28, 35, 45, 52, 23, 40],
    "Salary": [25000, 30000, 32000, 45000, 60000, 80000, 27000, 55000]
})

print("Original Data:\n")
print(df)

#  Standardization (Mean = 0, Std = 1)

standard_scaler = StandardScaler()

df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)

print("\nStandardized Data:\n")
print(df_standardized)

# -------------------------------------
# 3️⃣ Normalization (Range 0 to 1)
# -------------------------------------
minmax_scaler = MinMaxScaler()

df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

print("\nNormalized Data:\n")
print(df_normalized)

# -------------------------------------
# 4️⃣ Histogram Comparison
# -------------------------------------
plt.figure(figsize=(12,4))

# Before scaling
plt.subplot(1, 3, 1)
plt.hist(df["Salary"], bins=5)
plt.title("Before Scaling")
plt.xlabel("Salary")

# After Standardization
plt.subplot(1, 3, 2)
plt.hist(df_standardized["Salary"], bins=5)
plt.title("After Standardization")
plt.xlabel("Scaled Salary")

# After Normalization
plt.subplot(1, 3, 3)
plt.hist(df_normalized["Salary"], bins=5)
plt.title("After Normalization")
plt.xlabel("Scaled Salary (0-1)")

plt.tight_layout()
plt.show()

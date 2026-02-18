# ============================================
# HEIGHT & WEIGHT OUTLIER EXERCISE
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# ======================================================
# 1. LOAD DATA (SEPARATE CSV FILES)
# ======================================================

# Load files
height_df = pd.read_csv("height.csv")
weight_df = pd.read_csv("weight.csv")

# Clean column names (avoid errors)
height_df.columns = height_df.columns.str.lower().str.strip()
weight_df.columns = weight_df.columns.str.lower().str.strip()

# Combine both into one dataframe
df = pd.concat([height_df, weight_df['weight']], axis=1)

print("Columns:", df.columns)
print(df.head())

# ======================================================
# 2. HISTOGRAMS
# ======================================================

# Height histogram
plt.figure(figsize=(6,4))
plt.hist(df['height'], bins=30, edgecolor='black')
plt.title("Height Distribution")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.show()

# Weight histogram
plt.figure(figsize=(6,4))
plt.hist(df['weight'], bins=30, edgecolor='black')
plt.title("Weight Distribution")
plt.xlabel("Weight")
plt.ylabel("Frequency")
plt.show()

# ======================================================
# 3. WEIGHT OUTLIERS USING IQR
# ======================================================

Q1 = df['weight'].quantile(0.25)
Q3 = df['weight'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

weight_outliers = df[
    (df['weight'] < lower_limit) |
    (df['weight'] > upper_limit)
]

print("\nWeight Outliers:")
print(weight_outliers)

# ======================================================
# 4. HEIGHT OUTLIERS USING IQR
# ======================================================

Q1 = df['height'].quantile(0.25)
Q3 = df['height'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

height_outliers = df[
    (df['height'] < lower_limit) |
    (df['height'] > upper_limit)
]

print("\nHeight Outliers:")
print(height_outliers)

print("\n===== PROGRAM COMPLETED =====")

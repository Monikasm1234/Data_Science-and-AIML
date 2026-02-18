# ==========================================
# OUTLIER REMOVAL USING STD & Z-SCORE
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# ======================================================
# 1. LOAD DATA
# ======================================================

df = pd.read_csv("bhp.csv")

# clean column names (avoid errors)
df.columns = df.columns.str.lower().str.strip()

print("Original Shape:", df.shape)
print(df.head())

# ======================================================
# 2. REMOVE OUTLIERS USING PERCENTILE METHOD
#    lower = 0.001 , upper = 0.999
# ======================================================

lower_limit = df['price_per_sqft'].quantile(0.001)
upper_limit = df['price_per_sqft'].quantile(0.999)

df2 = df[
    (df['price_per_sqft'] >= lower_limit) &
    (df['price_per_sqft'] <= upper_limit)
]

print("\nAfter Percentile Filtering:", df2.shape)

# ======================================================
# 3. REMOVE OUTLIERS USING 4 STANDARD DEVIATIONS
# ======================================================

mean = df2['price_per_sqft'].mean()
std = df2['price_per_sqft'].std()

lower_limit = mean - 4 * std
upper_limit = mean + 4 * std

df3 = df2[
    (df2['price_per_sqft'] >= lower_limit) &
    (df2['price_per_sqft'] <= upper_limit)
]

print("After 4 STD Filtering:", df3.shape)

# ======================================================
# 4. HISTOGRAM + BELL CURVE
# ======================================================

plt.figure(figsize=(8,5))

# Histogram
plt.hist(df3['price_per_sqft'],
         bins=30,
         density=True,
         edgecolor='black',
         alpha=0.6)

# Bell Curve
x = np.linspace(df3['price_per_sqft'].min(),
                df3['price_per_sqft'].max(), 100)

plt.plot(x, norm.pdf(x, mean, std), linewidth=2)

plt.title("Histogram with Bell Curve")
plt.xlabel("Price per sqft")
plt.ylabel("Density")
plt.show()

# ======================================================
# 5. REMOVE OUTLIERS USING Z-SCORE = 4
# ======================================================

df2['zscore'] = (df2['price_per_sqft'] - mean) / std

df_z = df2[df2['zscore'].abs() <= 4]

print("After Z-Score Filtering:", df_z.shape)

print("\nProgram Completed Successfully!")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# SAMPLE HOUSING DATA
# -----------------------------
data = {
    "Price": [100000,120000,130000,150000,180000,
              200000,220000,250000,300000,500000],
    "City": ["Delhi","Mumbai","Delhi","Chennai","Mumbai",
             "Delhi","Chennai","Delhi","Mumbai","Delhi"]
}

df = pd.DataFrame(data)

# -----------------------------
# 1️⃣ HISTOGRAM + KDE
# -----------------------------
plt.figure(figsize=(7,4))
sns.histplot(df["Price"], kde=True, bins=6)
plt.title("Price Distribution (Histogram + KDE)")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# 2️⃣ SKEWNESS AND KURTOSIS
# -----------------------------
print("Skewness :", df["Price"].skew())
print("Kurtosis :", df["Price"].kurt())

# -----------------------------
# 3️⃣ COUNT PLOT (Categorical)
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="City", data=df)
plt.title("City Frequency Count")
plt.show()

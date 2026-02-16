import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# SAMPLE HOUSING DATA
# -----------------------------
data = {
    "SquareFootage": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500],
    "Price": [120000, 150000, 170000, 210000, 250000, 280000, 310000, 350000],
    "Location": ["City","City","Suburb","Suburb",
                 "City","Suburb","City","Suburb"]
}

df = pd.DataFrame(data)

# -----------------------------
# 1️⃣ SCATTER PLOT
# -----------------------------
plt.figure(figsize=(6,4))
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("SquareFootage vs Price")
plt.show()

# -----------------------------
# 2️⃣ BOXPLOT
# -----------------------------
plt.figure(figsize=(6,4))
sns.boxplot(x="Location", y="Price", data=df)
plt.title("Location vs Price")
plt.show()

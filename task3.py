import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample housing dataset
data = {
    "SquareFootage": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500],
    "Bedrooms": [2, 2, 3, 3, 4, 4, 4, 5],
    "Bathrooms": [1, 2, 2, 2, 3, 3, 3, 4],
    "Price": [200000, 250000, 300000, 360000, 400000, 450000, 480000, 550000]
}

df = pd.DataFrame(data)

corr_matrix = df.corr()
print(corr_matrix)

plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

plt.figure()
sns.boxplot(y=df["Price"])
plt.title("Boxplot of Price")
plt.show()
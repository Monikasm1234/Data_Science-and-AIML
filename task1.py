import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
np.random.seed(42)
heights = np.random.normal(loc=170, scale=10, size=1000)   
incomes = np.random.lognormal(mean=10, sigma=1, size=1000) 
scores = 100 - np.random.beta(a=2, b=5, size=1000) * 100   
df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})
def analyze_distribution(data, title):
    mean_val = np.mean(data)
    median_val = np.median(data)
    plt.figure(figsize=(7,4))
    sns.histplot(data, kde=True, bins=30, color="skyblue")
    plt.axvline(mean_val, color="red", linestyle="--", label=f"Mean = {mean_val:.2f}")
    plt.axvline(median_val, color="green", linestyle="-.", label=f"Median = {median_val:.2f}")
    plt.title(title)
    plt.legend()
    plt.show()
    print(f"{title}: Mean = {mean_val:.2f}, Median = {median_val:.2f}")
    if mean_val > median_val:
        print("Observation: Right-Skewed (Mean > Median)\n")
    elif mean_val < median_val:
        print("Observation: Left-Skewed (Mean < Median)\n")
    else:
        print("Observation: Symmetric (Mean ≈ Median)\n")
analyze_distribution(df["Heights"], "Human Heights (Normal)")
analyze_distribution(df["Incomes"], "Household Incomes (Right-Skewed)")
analyze_distribution(df["Scores"], "Test Scores (Left-Skewed)")
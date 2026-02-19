import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
data = np.random.lognormal(mean=2, sigma=1.5, size=10000)
sample_means = []
for _ in range(1000):
    sample = np.random.choice(data, size=30, replace=True)
    sample_means.append(np.mean(sample))
df = pd.DataFrame(sample_means, columns=["sample_mean"])
plt.figure(figsize=(8,5))
sns.histplot(df["sample_mean"],
         kde=True, bins=30, color="skyblue")
plt.title("Distribution of Sample Means" 
          "(Central Limit Theorem)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()
import pandas as pd
import numpy as np
data = {
    "values": [10, 12, 11, 13, 12, 14, 15, 100, 11, 12, 13, 14, 12, 13]
}
df = pd.DataFrame(data)
mu = df["values"].mean()
sigma = df["values"].std()
print(f"Mean (μ): {mu:.2f}")
print(f"Standard Deviation (σ): {sigma:.2f}")
df["z_score"] = (df["values"] - mu) / sigma
outliers = df[np.abs(df["z_score"]) > 3]
print("\nDataset with z-scores:")
print(df)
print("\nOutliers (|Z| > 3):")
print(outliers)
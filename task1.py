import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Sample dataset
df = pd.DataFrame({
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red"]
})

print("Original Data:")
print(df)

# Label Encoding (Transmission)
le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])

#One-Hot Encoding (Color)
df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("\nEncoded Data:")
print(df)

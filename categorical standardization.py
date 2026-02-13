import pandas as pd

data = {
    "Location": [" New York", "new york", "NEW YORK ", "Los Angeles", " los angeles "]
}

df = pd.DataFrame(data)

print("Before cleaning:")
print(df["Location"].unique())

# Clean text
df["Location"] = df["Location"].str.strip().str.title()

print("\nAfter cleaning:")
print(df["Location"].unique())
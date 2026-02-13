import pandas as pd

# Example dataset
data = {
    "Price": ["$120", "$250", "$180", "$300"],
    "Date": ["2026-01-01", "2026-01-05", "2026-01-10", "2026-01-15"]
}

df = pd.DataFrame(data)
print(df.dtypes)
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)
print(df.dtypes)
print(df["Price"].mean())
df["Date"] = pd.to_datetime(df["Date"])
print(df.dtypes)
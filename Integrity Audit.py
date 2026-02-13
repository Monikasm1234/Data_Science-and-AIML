import pandas as pd
# Load data
df = pd.read_csv("customers_order.csv")
# Shape before cleaning
print("Shape before cleaning:", df.shape)
# Missing values report
print("\nMissing Values Report:")
print(df.isna().sum())
# Fill missing numeric values with median
numeric_cols = df.select_dtypes(include=['number']).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())
# Remove duplicate rows
df = df.drop_duplicates()
# Shape after cleaning
print("\nShape after cleaning:", df.shape)
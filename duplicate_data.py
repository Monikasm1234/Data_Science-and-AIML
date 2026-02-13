import pandas as pd

data = {
    "Customer_ID" : [101,102,102,103],
    "Name" : ["Alice","Bob","Bob","Charlie"],
    "Purchase" : [500,300,300,700]
}

df = pd.DataFrame(data)
print(df)

print(df.duplicated())
print(df[df.duplicated()])

df_clean = df.drop_duplicates()
print(df_clean)

print(df.duplicated(subset="Customer_ID"))

print(df.drop_duplicates())
print(df.drop_duplicates(keep="last"))
print(df.drop_duplicates(keep=False))
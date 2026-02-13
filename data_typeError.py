import pandas as pd
data = {
    "Name" : ["Alice","Bob","Charlie"],
    "Marks" : ["85","90","88"]
}

df = pd.DataFrame(data)
print(df.dtypes)

#Problem1 : No stored as strings
#use astype()
df["Marks"] = df["Marks"].astype(int)
print(df.dtypes)
print(df["Marks"].mean())

#Problem2 : data stored as object

data = {
    "Joining_Date": ["2024-01-10","2023-12-05"]
}
df = pd.DataFrame(data)
print(df.dtypes)

#solution
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])
print(df.dtypes)
print(df["Joining_Date"].dt.year)

#Problem3 : Mixed data types
data = {
    "Salary" : ["50000", "70000","60000"]
}
#solution
df = pd.DataFrame(data)
print(df.dtypes)
df["Salary"]
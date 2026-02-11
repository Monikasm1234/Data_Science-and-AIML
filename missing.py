import pandas as pd
data = pd.Series([10,None, 30, None])
print(data)

print(data.isnull())   # returns a boolean mask

print(data[data.isnull()])  #filter only missing values
print(data[data.notnull()])   #filter only valid values
print(data.fillna(0))     #replace missing values - fillna() with constant
print(data.fillna(data.mean()))   #replace with mean ie: very coomon in DS
print(data.dropna())    # remove missing values - dropna()
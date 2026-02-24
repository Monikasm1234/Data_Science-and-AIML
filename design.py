import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

np.random.seed(42)

# Parameters
num_batches = 30
parts_per_batch = 60   # 30 × 60 = 1800 records
machines = ['M1','M2','M3']
shifts = ['Morning','Evening','Night']

data = []

for batch in range(1, num_batches+1):
    batch_mean = 100 + np.random.normal(0,1)   # slight variation per batch
    for part in range(1, parts_per_batch+1):
        weight = np.random.normal(batch_mean,5)
        data.append([
            batch,
            f"P{batch}_{part}",
            round(weight,2),
            np.random.choice(machines),
            np.random.choice(shifts)
        ])

df = pd.DataFrame(data, columns=['batch_id','part_id','weight','machine_id','shift'])

print("Total Records:", len(df))
df.head()

#Normal distribution check
mean = df['weight'].mean()
median = df['weight'].median()
std = df['weight'].std()

print("Mean:", mean)
print("Median:", median)
print("Std Dev:", std)

plt.figure()
sns.histplot(df['weight'], stat='density')

x = np.linspace(df['weight'].min(), df['weight'].max(), 100)
plt.plot(x, stats.norm.pdf(x, mean, std))
plt.title("Weight Distribution with Normal Curve")
plt.show()

#Skewness Check
print("Skewness:", df['weight'].skew())

#Probability Calculations (Manual Z-score)
# Given values
mu = 100
sigma = 5

# P(weight < 90)
z1 = (90 - mu)/sigma
prob1 = stats.norm.cdf(z1)
print("P(weight < 90g):", prob1)

# P(95 < weight < 105)
z_low = (95 - mu)/sigma
z_high = (105 - mu)/sigma
prob2 = stats.norm.cdf(z_high) - stats.norm.cdf(z_low)
print("P(95g < weight < 105g):", prob2)

#Central Limit Theorem (Sample Size = 40)
sample_means = []

for batch in df['batch_id'].unique():
    batch_data = df[df['batch_id'] == batch]['weight']
    sample = batch_data.sample(40)
    sample_means.append(sample.mean())

plt.figure()
sns.histplot(sample_means, kde=True)
plt.title("Sampling Distribution of Sample Means (CLT)")
plt.show()

print("Mean of Sample Means:", np.mean(sample_means))

#Process Control Using Z-score
df['z_score'] = (df['weight'] - mean) / std
df['defective'] = df['z_score'].abs() > 2.5

print("Total Defective Parts:", df['defective'].sum())

df[df['defective'] == True].head()
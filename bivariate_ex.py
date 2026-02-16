import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#improve plot  apperance
sns.set(style="whitegrid")

data = {
    "Age":[25,30,35,40,28,32,45,50,23,36,29,41],

    "Salary":[30000,40000,50000,65000,42000,
              48000,80000,90000,28000,52000,
              46000,55000],

    "Experience":[1,3,7,10,2,5,15,20,1,8,4,12],

    "Department":["HR","IT","Finance","IT","HR",
                  "Finance","IT","HR","Finance",
                  "IT","HR","IT"],

    "Gender":["M","F","M","M","F","F",
              "M","M","F","F","M","F"]
}

df  = pd.DataFrame(data)
print(df)

#scater plot
plt.figure()
sns.scatterplot(x="Age", y="Salary", data=df)
plt.title("Age vs Salary")
plt.show()

plt.figure()
sns.boxplot(x="Experience", y = "Salary", data=df)
plt.title("Experience vs Salary")
plt.show()

plt.figure()
sns.boxplot(x="Department", y = "Salary", data=df)
plt.title("Department vs Salary")
plt.show()

plt.figure()
sns.boxplot(x="Gender", y = "Salary", data=df)
plt.title("Gender vs Salary")
plt.show()

#correlation heatmap
corr_matrix = df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr_matrix)

#HeatMap
plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

#outlier detection
plt.figure()
sns.boxplot(x=df["Age"])
plt.title("Age outliers")
plt.show()

plt.figure()
sns.boxplot(x=df["Experience"])
plt.title("Experience outliers")
plt.show()

#Final step - Documentation and reporting
print("\n Sample insights:")
print("1. Salary incrreases with experience and age(positive correlation).")
print("2. Finance department shows higher salary variation.")
print("3. No extreme outliers detected in Age or Experience.")
print("4. Gender-based salary differences are visible in the data.")
print("5. Experience strongly influences salary.")
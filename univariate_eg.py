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

#Histogram
plt.figure()
sns.histplot(df["Age"], kde = True)
plt.title("Age Distribution")
plt.show()

#Histogram
plt.figure()
sns.histplot(df["Salary"], kde = True)
plt.title("Salary Distribution")
plt.show()

#Boxplot
plt.figure()
sns.boxplot(x=df["Salary"])
plt.title("Salary Boxplot")
plt.show()

#Categorical plot

print("\nDepartment counts:")
print(df["Department"].value_counts())\

print("\nGender counts:")
print(df["Gender"].value_counts())

#Bar plot for Department
plt.figure()
sns.countplot(x="Department", data=df)
plt.title("Department Distribution")
plt.show()
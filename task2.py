import pandas as pd

# Create Series with missing values
grades = pd.Series([85, None, 92, 45, None, 78, 55])

# Identify missing values
missing = grades.isnull()

# Fill missing values with 0
filled_grades = grades.fillna(0)

# Filter scores greater than 60
filtered = filled_grades[filled_grades > 60]

# Output
print("Original Grades:\n")
print(grades)

print("\nMissing Values (True means missing):\n")
print(missing)

print("\nGrades After Filling Missing Values:\n")
print(filled_grades)

print("\nScores Greater Than 60:\n")
print(filtered)

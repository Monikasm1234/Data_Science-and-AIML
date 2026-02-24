#UNIVERSITY PERFORMANCE INTELLIGENCE SYSTEM

import pandas as pd
import numpy as np
import sqlite3

np.random.seed(42)

print("\n========== UNIVERSITY PERFORMANCE INTELLIGENCE SYSTEM ==========\n")
# 1️⃣ Create SQLite Database (In-Memory)

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE students(
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    year INTEGER
)
""")

cursor.execute("""
CREATE TABLE subjects(
    subject_id INTEGER PRIMARY KEY,
    subject_name TEXT,
    department TEXT
)
""")

cursor.execute("""
CREATE TABLE marks(
    student_id INTEGER,
    subject_id INTEGER,
    marks INTEGER
)
""")

# 2️⃣ Generate Sample Data

departments = ['CSE','ECE','MECH','CIVIL']

students = []
subjects = []
marks = []

student_id = 1
subject_id = 1

# Generate Students (50 per department)
for dept in departments:
    for i in range(50):
        students.append((student_id, f"Student_{student_id}", dept, np.random.randint(1,5)))
        student_id += 1

# Generate Subjects (5 per department)
for dept in departments:
    for i in range(5):
        subjects.append((subject_id, f"{dept}_Sub_{i+1}", dept))
        subject_id += 1

# Generate Marks (students take subjects from their own department)
for s in students:
    for sub in subjects:
        if s[2] == sub[2]:
            marks.append((s[0], sub[0], np.random.randint(40,100)))

cursor.executemany("INSERT INTO students VALUES (?,?,?,?)", students)
cursor.executemany("INSERT INTO subjects VALUES (?,?,?)", subjects)
cursor.executemany("INSERT INTO marks VALUES (?,?,?)", marks)

conn.commit()

print("Total Students:", len(students))
print("Total Subjects:", len(subjects))
print("Total Marks:", len(marks))

# 3️⃣ JOIN Strategy

query = """
SELECT s.student_id,
       s.name,
       s.department,
       sub.subject_name,
       m.marks
FROM students s
JOIN marks m ON s.student_id = m.student_id
JOIN subjects sub ON m.subject_id = sub.subject_id
"""

df = pd.read_sql(query, conn)

# 4️⃣ Department Performance (Mean, Variance, Std Dev)

dept_stats = df.groupby('department')['marks'].agg(
    mean='mean',
    variance='var',
    std_dev='std',
    count='count'
)

print("\nDepartment Performance Statistics:\n")
print(dept_stats)

# Department with highest average
best_dept = dept_stats['mean'].idxmax()
print("\nBest Performing Department:", best_dept)

# Department with maximum variation
max_variation_dept = dept_stats['std_dev'].idxmax()
print("Department with Maximum Variation:", max_variation_dept)

# 5️⃣ Skewness Observation (Subject Level)

subject_skew = df.groupby('subject_name')['marks'].skew()

print("\nSubject Skewness:\n")
print(subject_skew)

# 6️⃣ Identify Top 5% Students

student_avg = df.groupby(['student_id','name'])['marks'].mean().reset_index()

threshold = np.percentile(student_avg['marks'], 95)
top_students = student_avg[student_avg['marks'] >= threshold]

print("\nTop 5% Students:\n")
print(top_students)

# 7️⃣ Percentage Above 1 Standard Deviation

mean_marks = df['marks'].mean()
std_marks = df['marks'].std()

percentage_above_1sd = len(df[df['marks'] > mean_marks + std_marks]) / len(df) * 100

print("\nPercentage of Students Above 1 Standard Deviation:", percentage_above_1sd)

# 8️⃣ Z-Score Based Anomaly Detection
df['z_score'] = (df['marks'] - mean_marks) / std_marks

abnormal_students = df[df['z_score'].abs() > 3]

print("\nAbnormal Performances (|Z| > 3):\n")
print(abnormal_students.head())
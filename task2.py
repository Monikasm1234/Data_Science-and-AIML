import sqlite3

# Connect to database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# Clear table (to avoid duplicate inserts if run multiple times)
cursor.execute("DELETE FROM interns")

# Insert sample data
cursor.executemany("""
INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?)
""", [
    ('Anita', 'Data Science', 15000),
    ('Rahul', 'Web Dev', 12000),
    ('Meena', 'Data Science', 16000),
    ('Arjun', 'Cyber Security', 4000),
    ('Priya', 'Web Dev', 3000)
])

conn.commit()

print("----- FILTER: Data Science interns with stipend > 5000 -----")
cursor.execute("""
SELECT * FROM interns
WHERE track = 'Data Science' AND stipend > 5000
""")
for row in cursor.fetchall():
    print(row)


print("\n----- AGGREGATE: Average stipend per track -----")
cursor.execute("""
SELECT track, AVG(stipend) AS average_stipend
FROM interns
GROUP BY track
""")
for row in cursor.fetchall():
    print(row)


print("\n----- COUNT: Number of interns per track -----")
cursor.execute("""
SELECT track, COUNT(*) AS total_interns
FROM interns
GROUP BY track
""")
for row in cursor.fetchall():
    print(row)

conn.close()
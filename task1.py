import sqlite3

# Connect to database (creates if not exists)
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

# Insert data
cursor.execute("""
INSERT INTO interns (name, track, stipend) VALUES
('Anita', 'Data Science', 15000),
('Rahul', 'Web Dev', 12000),
('Meena', 'Data Science', 16000),
('Arjun', 'Cyber Security', 14000),
('Priya', 'Web Dev', 13000)
""")

conn.commit()

# Query specific columns
cursor.execute("SELECT name, track FROM interns")
rows = cursor.fetchall()

print("Intern Name and Track:")
for row in rows:
    print(row)

conn.close()
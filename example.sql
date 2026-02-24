DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INTEGER,
    name TEXT,
    marks INTEGER
);

INSERT INTO students VALUES (1, 'Alice', 85);
INSERT INTO students VALUES (2, 'Bob', 90);
INSERT INTO students VALUES (3, 'Charlie', 78);

SELECT * FROM students;
SELECT name, marks FROM students;
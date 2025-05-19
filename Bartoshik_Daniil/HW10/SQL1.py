import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ('Someone', 20))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ('Somebody', 22))

conn.commit()
conn.close()

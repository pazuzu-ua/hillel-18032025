import sqlite3

with sqlite3.connect('HW10.db', autocommit=False) as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS hw10 (
        i_user INTEGER PRIMARY KEY AUTOINCREMENT,
        age INTEGER  NOT NULL,
        email TEXT  NOT NULL
     );
""")
    
    conn.execute("INSERT INTO hw10 (age, email) VALUES (?, ?)", (23, 'example@example.com'))
    conn.execute("INSERT INTO hw10 (age, email) VALUES (?, ?)", (22, 'example1@example.com'))
    conn.commit()


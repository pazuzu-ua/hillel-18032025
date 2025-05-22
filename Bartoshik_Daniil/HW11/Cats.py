import sqlite3

with sqlite3.connect('Cats.db') as conn:
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cats (
            cat_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            weight INT CHECK(weight > 0)
        )
    ''')

    cursor.execute("DELETE FROM cats")
    cats = [
        ('Капучино', 12),
        ('Сырок', 8),
        ('Бублик', 15),
        ('Рыжик', 10),
        ('Уголёк', 5),
        ('Хвостик', 4),
    ]
    cursor.executemany("INSERT INTO cats (name, weight) VALUES (?, ?)", cats)
    conn.commit()

# Select cats weighing between 10 and 15 kg

#   print("Коты от 10 до 15 кг:")
#   cursor.execute("SELECT name FROM cats WHERE weight BETWEEN 10 AND 15")
#   for (name,) in cursor.fetchall():
#        print(name)

# Select all cats and sort them by weight

#   print("Все коты по весу:")
#   cursor.execute("SELECT * FROM cats ORDER BY weight")
#   for cat in cursor.fetchall():
#       print(cat)

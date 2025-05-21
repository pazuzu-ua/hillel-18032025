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

    cats = [
        ('Капучино', 12),
        ('Сырок', 8),
        ('Бублик', 15),
        ('Рыжик', 10),
        ('Уголёк', 5),
        ('Хвостик', 4),
    ]

    cursor.execute("SELECT COUNT(*) FROM cats")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO cats (name, weight) VALUES (?, ?)", cats)
        conn.commit()

    cursor.execute("SELECT * FROM cats")
    all_cats = cursor.fetchall()

    filtered_names = [name for (cat_id, name, weight) in all_cats if 10 <= weight <= 15]
    print("Коты с весом от 10 до 15 кг:")
    for name in filtered_names:
        print(name)

    sorted_cats = sorted(all_cats, key=lambda cat: cat[2])
    print("Все коты, отсортированные по весу:")
    for cat in sorted_cats:
        print(cat)

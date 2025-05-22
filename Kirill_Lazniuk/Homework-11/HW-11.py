import sqlite3


with sqlite3.connect('HW11.db')as conn:
    conn.execute('''
        CREATE TABLE IF NOT EXISTS cats (
        cat_id  INTEGER PRIMARY KEY,
        name    TEXT    NOT NULL,
        weight  INT CHECK(weight > 0)
        )
    ''')

    conn.execute("INSERT INTO cats (name, weight) VALUES (?,?)", ('Мурчик', 12))
    conn.execute("INSERT INTO cats (name, weight) VALUES (?,?)", ('Барсик', 8))
    conn.execute("INSERT INTO cats (name, weight) VALUES (?,?)", ('Сніжок', 15))
    conn.execute("INSERT INTO cats (name, weight) VALUES (?,?)", ('Рижик', 10))
    conn.execute("INSERT INTO cats (name, weight) VALUES (?,?)", ('Лакі', 5))


# Это код для вывода только колонки name у которых вес от 10 - 15 
# SELECT name
# FROM Cats
# WHERE weight BETWEEN 10 AND 15;

# Это код для вывода всех полей и отсортирования их по весу
# SELECT *
# FROM Cats
# ORDER BY weight;
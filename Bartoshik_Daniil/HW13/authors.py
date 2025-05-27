import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Authors (
    i_author INTEGER PRIMARY KEY,
    name TEXT,
    birth_year INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Books (
    i_book INTEGER PRIMARY KEY,
    title TEXT,
    pages INTEGER,
    i_author INTEGER,
    i_genre INTEGER,
    FOREIGN KEY (i_author) REFERENCES Authors(i_author)
)
''')

cursor.execute("SELECT COUNT(*) FROM Authors")
if cursor.fetchone()[0] == 0:
    cursor.executemany('INSERT INTO Authors (i_author, name, birth_year) VALUES (?, ?, ?)', [
        (1, 'Автор A', 1890),
        (2, 'Автор B', 1950),
        (3, 'Автор C', 1980),
    ])

    cursor.executemany('INSERT INTO Books (i_book, title, pages, i_author, i_genre) VALUES (?, ?, ?, ?, ?)', [
        (1, 'Книга 1', 320, 1, 1),
        (2, 'Книга 2', 340, 1, 1),
        (3, 'Книга 3', 600, 2, 2),
        (4, 'Книга 4', 550, 2, 2),
        (5, 'Книга 5', 280, 3, 1),
    ])

    conn.commit()




# 1) Автори із середньою кількістю сторінок < 350
print(f"Автори із середньою кількістю сторінок < 350:\n")
cursor.execute('''
SELECT A.name AS author,
       COUNT(B.i_book) AS books_count,
       SUM(B.pages) AS pages_sum,
       ROUND(AVG(B.pages), 1) AS avg_pages
  FROM Books B
  JOIN Authors A ON B.i_author = A.i_author
GROUP BY A.i_author, A.name
HAVING AVG(B.pages) < 350;
''')

rows = cursor.fetchall()
for row in rows:
    author, count, total, avg = row
    print(f"Автор: {author} | Книг: {count} | Усього сторінок: {total} | Середнє: {avg}")




# 2) Кількість авторів, народжених до 1900 року
print(f"Кількість авторів, народжених до 1900 року:\n")
cursor.execute('SELECT COUNT(*) FROM Authors WHERE birth_year < 1900')
count = cursor.fetchone()[0]
print(f"Кількість авторів: {count}")

conn.close()

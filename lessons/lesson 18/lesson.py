import sqlite3


with sqlite3.connect('library.db') as conn:
    # ------------- fetchall # list or []

    # result = conn.execute("SELECT * FROM Books")
    # rows = result.fetchall() # list or []
    # print(rows)

    # result = conn.execute("""
    #     SELECT  count(pages) AS 'total_books',
    #             max(pages) AS 'max_pages', 
    #             min(pages) AS 'min_pages',
    #             avg(pages) AS 'avg_pages',
    #             sum(pages) AS 'total_pages'
    #      FROM Books;
    # """)
    # rows = result.fetchall()
    # print(rows)

    # ------------- fetchone # () or None
    # result = conn.execute("SELECT * FROM Books")
    # for _ in range(22):
    #     data = result.fetchone()
    #     print(data)

    # value = result.fetchone()
    # while value:
    #     print(value)
    #     value = result.fetchone()

    # while value := result.fetchone():
    #     print(value)

    # ------------- fetchmany # list or None
    # batch == вибірка == кількість елементів
    # result = conn.execute("SELECT * FROM Books")
    # while value := result.fetchmany(7):
    #     print(value)

    # він змінює як дані повертаються
    # conn.row_factory = sqlite3.Row
    # result = conn.execute("SELECT * FROM Books")
    # rows = result.fetchall() # list or []
    # for row in rows:
    #     print(row['title'])

    ...
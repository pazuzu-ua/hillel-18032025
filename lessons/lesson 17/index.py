# імпортуємо необхідний модуль
import sqlite3

# створюємо базу даних і під'єднуємося до неї
with sqlite3.connect('library.db') as connection:
    # створюємо об'єкт курсору (необхідний для виконання запитів до БД)
    cursor = connection.cursor()
    # виконуємо "особливий" запит для підтримки зовнішніх ключів
    connection.execute("PRAGMA foreign_keys = ON;")

    # таким чином можна видалити таблиці, якщо вони вже створені
    cursor.execute("DROP TABLE IF EXISTS Books")
    cursor.execute("DROP TABLE IF EXISTS Authors")
    cursor.execute("DROP TABLE IF EXISTS Genres")

    # БД готова і створена, тепер створимо таблиці!
    cursor.execute('''
        CREATE TABLE Authors (
            i_author INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birth_year INTEGER CHECK (birth_year > 0)
        )
    ''')

    cursor.execute('''
        CREATE TABLE Genres (
            i_genre INTEGER PRIMARY KEY AUTOINCREMENT,
            genre_name TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE Books (
            i_book INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            publication_year INTEGER CHECK (publication_year BETWEEN 1500 AND 2025),
            i_author INTEGER NOT NULL,
            i_genre INTEGER NOT NULL,
            pages INTEGER CHECK (pages > 0),
            FOREIGN KEY (i_author) REFERENCES AUTHORS (i_author) ON DELETE CASCADE,
            FOREIGN KEY (i_genre) REFERENCES GENRES (i_genre) ON DELETE SET NULL
        )
    ''')

    authors = [
        ("J.K. Rowling", 1965),
        ("George Orwell", 1903),
        ("Jane Austen", 1775),
        ("Mark Twain", 1835),
        ("Agatha Christie", 1890),
        ("J.R.R. Tolkien", 1892),
        ("Stephen King", 1947),
        ("Ernest Hemingway", 1899),
        ("F. Scott Fitzgerald", 1896),
        ("Leo Tolstoy", 1828)
    ]
    cursor.executemany("INSERT INTO AUTHORS (name, birth_year) VALUES (?, ?)", authors)

    genres = [
        ("Fantasy",),
        ("Science Fiction",),
        ("Mystery",),
        ("Historical",),
        ("Horror",),
        ("Classic",),
        ("Romance",),
        ("Adventure",),
        ("Drama",),
        ("Satire",)
    ]
    cursor.executemany("INSERT INTO GENRES (genre_name) VALUES (?)", genres)

    books = [
        ("Harry Potter", 1997, 1, 1, 320),
        ("1984", 1949, 2, 2, 328),
        ("Pride and Prejudice", 1813, 3, 7, 279),
        ("Adventures of Huckleberry Finn", 1884, 4, 8, 366),
        ("Murder on the Orient Express", 1934, 5, 3, 256),
        ("The Hobbit", 1937, 6, 1, 310),
        ("The Shining", 1977, 7, 5, 447),
        ("The Old Man and the Sea", 1952, 8, 9, 127),
        ("The Great Gatsby", 1925, 9, 6, 218),
        ("War and Peace", 1869, 10, 4, 1225),
        ("Animal Farm", 1945, 2, 2, 112),
        ("Emma", 1815, 3, 7, 474),
        ("The Adventures of Tom Sawyer", 1876, 4, 8, 274),
        ("Death on the Nile", 1937, 5, 3, 333),
        ("The Lord of the Rings", 1954, 6, 1, 1178),
        ("It", 1986, 7, 5, 1138),
        ("For Whom the Bell Tolls", 1940, 8, 9, 480),
        ("Tender is the Night", 1934, 9, 6, 317),
        ("Anna Karenina", 1878, 10, 4, 864)
    ]
    cursor.executemany("""
        INSERT INTO BOOKS (title, publication_year, i_author, i_genre, pages)
        VALUES (?, ?, ?, ?, ?)
    """, books)

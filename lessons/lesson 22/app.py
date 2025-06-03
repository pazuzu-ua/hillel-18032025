import sqlite3

from pydantic import BaseModel, Field, ValidationError


DB_FILE: str = "books.db"


class Book(BaseModel):
    title: str = Field(min_length=1)
    publication_year: int = Field(gt=1500)
    pages: int = Field(gt=0)

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS Books(
                    i_book INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    publication_year INTEGER,
                    pages INTEGER
                );
            """
        )

def add_book():
    try:
        title = input("Enter title: ")
        year = input("Enter year: ")
        pages = input("Enter pages: ")
        book = Book(title=title, publication_year=year, pages=pages)

        with sqlite3.connect(DB_FILE) as conn:
            conn.execute(
                "INSERT INTO Books (title, publication_year, pages) VALUES (?, ?, ?)",
                (book.title, book.publication_year, book.pages)
            )
    except ValidationError as err:
        print(f"Validation failed: {err}")

def list_books():
    with sqlite3.connect(DB_FILE) as conn:
        result = conn.execute("SELECT title, publication_year, pages FROM Books")
        books = [ Book(title=row[0], publication_year=row[1], pages=row[2]) for row in result ]
        for book in books:
            print(book)

def run_app():
    init_db()
    while True:
        cmd = input("Enter: ")
        if cmd == "add":
            add_book()
        elif cmd == "list":
            list_books()
        elif cmd == "exit":
            break
        else:
            print("Wrong command...")

if __name__ == '__main__':
    run_app()

import sqlite3

DB = "injection_demo.db"

def setup_users_table():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id       INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT    NOT NULL UNIQUE,
                password TEXT    NOT NULL
            );
        """)
        conn.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('aa', 'bb');")


def unsafe_login():
    username = input("Username: ")
    password = input("Password: ")

    query = (
        "SELECT * FROM users "
        f"WHERE username = '{username}' "
        f"AND password = '{password}';"
    )

    # AND password = 'cc';

    # AND password = '' OR '1'='1';

    with sqlite3.connect(DB) as conn:
        cur = conn.execute(query)
        user = cur.fetchone()
        if user:
            print("Login successful!")
        else:
            print("Invalid credentials.")

def safe_login():
    username = input("Username: ")
    password = input("Password: ")

    query = """
        SELECT * FROM users 
        WHERE username = ?
        AND password = ?
    """
    with sqlite3.connect(DB) as conn:
        cur = conn.execute(query, (username, password))
        user = cur.fetchone()
        if user:
            print("Login successful!")
        else:
            print("Invalid credentials.")

setup_users_table()
safe_login()

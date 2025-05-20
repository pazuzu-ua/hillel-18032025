import sqlite3

# --------------------------------- CREATE TABLE 
# connect to the database:
# 1. В межах блоку створюється 1 під'єднання
# 2. При виході за межі блоку: все зберігається і з'єднання розривається
# 3. Починаючи з версії 3.12: autocommit=False
# транзакція: якась певна зміна бази, ви її можете або закомітити, або заролити
# за межі блоку, якщо все було ОК - комітимо, якщо НІ - ролбек

# with sqlite3.connect('lesson.db', autocommit=False) as conn:
#     conn.execute("""
#         CREATE TABLE IF NOT EXISTS Users (
#             i_user            INTEGER           PRIMARY KEY AUTOINCREMENT,
#             email             TEXT               UNIQUE  NOT NULL,
#             comment           TEXT,
#             favourite_word    TEXT                DEFAULT 'bird'
#         );
#     """)

# --------------------------------- INSERT
# with sqlite3.connect('lesson.db', autocommit=False) as conn:
#     # INSERT OR IGNORE - ігнорує помилки (запис не робиться, але і помилка не виникає)
#     result = conn.execute("INSERT OR IGNORE INTO Users(email) VALUES ('a3@gmail.com')")
#     print(result.lastrowid) # ІД останнього запису або 0 / None

# with sqlite3.connect('lesson.db', autocommit=False) as conn:
#     # більш захищени і правильний спосіб, допомагає уникнути SQL Injections
#     result = conn.execute(
#         "INSERT OR IGNORE INTO Users(email) VALUES (?)",
#         ( 'a4@gmail.com', )
#     )
#     print(result.lastrowid)

# bulk - в якихось об'ємах
# with sqlite3.connect('lesson.db', autocommit=False) as conn:
#     conn.executemany(
#         "INSERT OR IGNORE INTO Users(email) VALUES (?)",
#         [
#             ( 'a9@gmail.com', ),
#             ( 'b10@gmail.com', ),
#             ( 'b11@gmail.com', ),
#             ( 'b12@gmail.com', ),
#         ]
#     )
#     print( conn.total_changes )

# --------------------------------- DELETE
# with sqlite3.connect('lesson.db', autocommit=False) as conn:
#     conn.execute(
#         'DELETE FROM Users WHERE i_user = ?',
#         (8,)
#     )
#     print( conn.total_changes )

# with sqlite3.connect('lesson.db', autocommit=False) as conn:
#     conn.execute(
#         '''UPDATE Users
#               SET comment = 'HELLO'
#             WHERE i_user = ?
#         ''',
#         ( 10, )
#     )print( conn.total_changes )
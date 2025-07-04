import sqlite3
from models import SongInfo, AddUpdateSong

DB_PATH: str = "songs.db"

def init_db():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute('''
            CREATE TABLE IF NOT EXISTS Songs (
                i_song INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                release_date TEXT NOT NULL,
                genre TEXT NOT NULL,
                is_popular INTEGER NOT NULL,
                author_name TEXT NOT NULL
            )
        ''')
        connection.execute('''
            INSERT OR IGNORE INTO Songs (i_song, name, release_date, genre, is_popular, author_name)
            VALUES 
                (1, 'Under Your Spell', '2021-12-01', 'hyperpop', 1, 'Fortuna812'),
                (2, 'I Hate You', '2023-05-04', 'rock', 1, 'Fortuna812'),
                (3, 'Lost Angeles', '2021-03-25', 'drain', 1, 'Fortuna812')
        ''')
        connection.commit()

def fetch_song_info(i_song: int) -> SongInfo | None:
    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        row = connection.execute("SELECT * FROM Songs WHERE i_song = ?", (i_song,)).fetchone()
        return SongInfo(**row) if row else None

def fetch_all_songs() -> list[SongInfo]:
    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute("SELECT * FROM Songs").fetchall()
        return [SongInfo(**row) for row in rows]

def delete_song(i_song: int) -> bool:
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Songs WHERE i_song = ?", (i_song,))
        connection.commit()
        return cursor.rowcount > 0

def add_new_song(song: AddUpdateSong) -> SongInfo | None:
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Songs (name, release_date, genre, is_popular, author_name) VALUES (?, ?, ?, ?, ?)",
            (song.name, song.release_date, song.genre, int(song.is_popular), song.author_name)
        )
        connection.commit()
        i_song = cursor.lastrowid
        return fetch_song_info(i_song)

def update_song(i_song: int, song: AddUpdateSong) -> SongInfo | None:
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """UPDATE Songs
               SET name = ?, release_date = ?, genre = ?, is_popular = ?, author_name = ?
               WHERE i_song = ?
            """,
            (song.name, song.release_date, song.genre, int(song.is_popular), song.author_name, i_song)
        )
        connection.commit()

        if cursor.rowcount == 0:
            return None

        return fetch_song_info(i_song)

import sqlite3
from models import SongInfo

DB_PATH:str = "songs.db"

def init_db():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute('''
            CREATE TABLE IF NOT EXISTS Songs(
                i_song INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT NOT NULL,
                release_date TEXT NOT NULL,
                genre TEXT NOT NULL,
                is_popular INTEGER NOT NULL,
                author_name TEXT NOT NULL         
            )
        ''')
        connection.execute(
            '''
                INSERT OR IGNORE INTO Songs ( name, release_date, genre, is_popular, author_name)
                VALUES 
                    ('Under Your Spell', '2021-12-01', 'hyperpop', 1, 'Fortuna812'),
                    ('I Hate You', '2023-05-04', 'rock', 1, 'Fortuna812'),
                    ('Lost Angeles', '2021-03-25', 'drain', 1, 'Fortuna812')
            '''
        )
        connection.commit()


def fetch_all_songs() -> list[SongInfo]:
    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        songs = connection.execute("SELECT * FROM Songs").fetchall()
        return [ SongInfo(**song) for song in songs]

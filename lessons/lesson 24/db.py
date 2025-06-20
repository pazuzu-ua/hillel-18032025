import sqlite3

from models import PetInfo, AddUpdatePet


DB_PATH: str = "pets.db"

def init_db():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute('''
            CREATE TABLE IF NOT EXISTS Pets (
                i_pet INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date_of_birth TEXT NOT NULL,
                pet_type TEXT NOT NULL,
                vaccinated INTEGER NOT NULL        
            )
        ''')
        connection.execute(
            '''
                INSERT OR IGNORE INTO Pets ( i_pet, name, date_of_birth, pet_type, vaccinated )
                VALUES
                    ( 1, 'Mittens', '2024-06-01', 'cat', 1 ),
                    ( 2, 'Fluffy', '2023-01-11', 'dog', 1 ),
                    ( 3, 'Tweety', '2022-02-22', 'bird', 1 )
            '''
        )
        connection.commit()


def fetch_all_pets() -> list[PetInfo]:
    with sqlite3.connect(DB_PATH) as connection:
        #? --> це щоби повертало словнички
        connection.row_factory = sqlite3.Row
        pets = connection.execute("SELECT * FROM Pets").fetchall()
        # pet = { 'i_pet': 2, '': ... }
        # PetInfo( i_pet=6, ключ=значення )
        return [ PetInfo(**pet) for pet in pets ]


def fetch_pet_info( i_pet: int ) -> PetInfo | None:
    with sqlite3.connect(DB_PATH) as connection:
        #? --> це щоби повертало словнички
        connection.row_factory = sqlite3.Row
        pet = connection.execute("SELECT * FROM Pets WHERE i_pet = ?", (i_pet,) ).fetchone()
        return PetInfo(**pet) if pet else None


def add_new_pet( pet: AddUpdatePet ) -> PetInfo | None:
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Pets ( name, date_of_birth, pet_type, vaccinated ) VALUES ( ?, ?, ?, ? )",
            ( pet.name, pet.date_of_birth.isoformat(), pet.pet_type, int(pet.vaccinated) )
        )
        connection.commit()
        i_pet = cursor.lastrowid
        return fetch_pet_info( i_pet ) if i_pet else None


def delete_pet( i_pet: int ) -> bool:
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Pets WHERE i_pet = ?", ( i_pet, ))
        connection.commit() # ми хочемо впевнетися, що отримаємо результат виконання
        return cursor.rowcount > 0


def update_pet( i_pet: int, pet: AddUpdatePet ) -> PetInfo | None:
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
                UPDATE Pets
                   SET name = ?, date_of_birth = ?, pet_type = ?, vaccinated = ?
                 WHERE i_pet = ?
            """,
            ( pet.name, pet.date_of_birth.isoformat(), pet.pet_type, int(pet.vaccinated), i_pet )
        )
        connection.commit()

        if cursor.rowcount == 0:
            return None
        
        return fetch_pet_info(i_pet)
